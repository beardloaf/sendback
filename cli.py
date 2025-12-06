#!/usr/bin/env python3
"""
SendBack CLI - Command-line interface for return automation
"""

import sys
import argparse
from datetime import datetime

from order_parser import parse_order_confirmation
from merchant_database import find_merchant, get_all_merchants, MERCHANT_DATABASE


def print_header():
    """Print app header"""
    print("=" * 60)
    print("SendBack - Ethical Return Automation")
    print("=" * 60)
    print()


def print_order_info(parsed_order):
    """Print parsed order information"""
    print("📦 ORDER DETAILS")
    print("-" * 60)

    if parsed_order.merchant_name:
        print(f"Merchant:      {parsed_order.merchant_name.upper()}")

    if parsed_order.order_number:
        print(f"Order Number:  {parsed_order.order_number}")

    if parsed_order.order_date:
        print(f"Order Date:    {parsed_order.order_date.strftime('%B %d, %Y')}")

    if parsed_order.return_by_date:
        days_left = (parsed_order.return_by_date - datetime.now()).days
        urgency = "⚠️ URGENT" if days_left < 7 else "✅"
        print(f"Return By:     {parsed_order.return_by_date.strftime('%B %d, %Y')} ({days_left} days left) {urgency}")

    if parsed_order.total_amount:
        print(f"Total:         {parsed_order.total_amount}")

    if parsed_order.items:
        print(f"\nItems ({len(parsed_order.items)}):")
        for i, item in enumerate(parsed_order.items[:5], 1):
            print(f"  {i}. {item}")
        if len(parsed_order.items) > 5:
            print(f"  ... and {len(parsed_order.items) - 5} more")

    print()


def print_merchant_info(merchant_info):
    """Print merchant return information"""
    print("📮 RETURN INFORMATION")
    print("-" * 60)
    print(f"Merchant:        {merchant_info.merchant_name}")
    print(f"Return Window:   {merchant_info.return_window_days} days")
    print(f"Free Label:      {'✅ Yes' if merchant_info.free_return_label else '❌ No (varies)'}")
    print(f"Customer Service: {merchant_info.customer_service}")
    print()

    print("📍 RETURN ADDRESS")
    print("-" * 60)
    print(merchant_info.return_address)
    print()

    if merchant_info.return_portal_url:
        print("🌐 RETURN PORTAL")
        print("-" * 60)
        print(merchant_info.return_portal_url)
        print()

    print("📋 INSTRUCTIONS")
    print("-" * 60)
    print(merchant_info.instructions)
    print()


def cmd_parse(args):
    """Parse order confirmation file"""
    print_header()

    try:
        parsed_order = parse_order_confirmation(args.file)
        print_order_info(parsed_order)

        # Get merchant info if identified
        if parsed_order.merchant_name:
            merchant_info = find_merchant(parsed_order.merchant_name)
            if merchant_info:
                print_merchant_info(merchant_info)
            else:
                print(f"⚠️  Merchant '{parsed_order.merchant_name}' not in database")
                print("   You can still return using the address from your order confirmation")
                if parsed_order.extracted_return_address:
                    print(f"\n   Extracted address: {parsed_order.extracted_return_address}")
        else:
            print("⚠️  Could not identify merchant")
            print("   Try using the 'merchant' command to look up return info manually")

    except Exception as e:
        print(f"❌ Error parsing file: {e}")
        sys.exit(1)


def cmd_merchant(args):
    """Look up merchant return information"""
    print_header()

    merchant_info = find_merchant(args.name)

    if merchant_info:
        print_merchant_info(merchant_info)
    else:
        print(f"❌ Merchant '{args.name}' not found in database")
        print("\nSupported merchants:")
        cmd_list_merchants(args)


def cmd_list_merchants(args):
    """List all supported merchants"""
    print_header()
    print("SUPPORTED MERCHANTS")
    print("-" * 60)

    merchants = sorted(MERCHANT_DATABASE.items(), key=lambda x: x[1].merchant_name)

    for key, info in merchants:
        free_label = "✅" if info.free_return_label else "  "
        print(f"{free_label} {info.merchant_name:<20} ({info.return_window_days} days)")

    print()
    print(f"Total: {len(merchants)} merchants")
    print("✅ = Free return label available")


def main():
    parser = argparse.ArgumentParser(
        description='SendBack - Automate product returns ethically',
        epilog='For legitimate returns only. Visit official return portals for free labels.'
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Parse command
    parse_parser = subparsers.add_parser('parse', help='Parse order confirmation file')
    parse_parser.add_argument('file', help='Order confirmation file (PDF, image, or text)')
    parse_parser.set_defaults(func=cmd_parse)

    # Merchant command
    merchant_parser = subparsers.add_parser('merchant', help='Look up merchant return info')
    merchant_parser.add_argument('name', help='Merchant name (e.g., "amazon", "walmart")')
    merchant_parser.set_defaults(func=cmd_merchant)

    # List command
    list_parser = subparsers.add_parser('list', help='List all supported merchants')
    list_parser.set_defaults(func=cmd_list_merchants)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == '__main__':
    main()
