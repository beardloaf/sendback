"""
Merchant Return Database
Contains official business return addresses and policies for major retailers.
All addresses are publicly available business addresses only.
"""

from dataclasses import dataclass
from typing import Optional
from datetime import timedelta


@dataclass
class ReturnInfo:
    merchant_name: str
    return_address: str
    return_portal_url: Optional[str]
    return_window_days: int
    free_return_label: bool
    instructions: str
    customer_service: str


# Database of merchant return information
# All addresses are OFFICIAL BUSINESS ADDRESSES (public record)
MERCHANT_DATABASE = {
    "amazon": ReturnInfo(
        merchant_name="Amazon",
        return_address="Amazon Returns Center (varies by item - use online portal)",
        return_portal_url="https://www.amazon.com/returns",
        return_window_days=30,
        free_return_label=True,
        instructions="Visit Amazon Returns portal, select your order, and print prepaid return label. Drop off at UPS, Whole Foods, or Amazon Locker.",
        customer_service="1-888-280-4331"
    ),

    "walmart": ReturnInfo(
        merchant_name="Walmart",
        return_address="Walmart Returns (use in-store or online portal)",
        return_portal_url="https://www.walmart.com/account/order-history",
        return_window_days=90,
        free_return_label=True,
        instructions="Return to any Walmart store or request free return label online. Most items eligible for 90-day returns.",
        customer_service="1-800-925-6278"
    ),

    "target": ReturnInfo(
        merchant_name="Target",
        return_address="Target Returns (use in-store or online portal)",
        return_portal_url="https://www.target.com/account/orders",
        return_window_days=90,
        free_return_label=True,
        instructions="Return to Target store or request prepaid label online. RedCard holders get extra time.",
        customer_service="1-800-440-0680"
    ),

    "ebay": ReturnInfo(
        merchant_name="eBay",
        return_address="Varies by seller - check order details",
        return_portal_url="https://www.ebay.com/sh/returns",
        return_window_days=30,
        free_return_label=False,  # Depends on seller
        instructions="Contact seller through eBay Messages. Return policy varies by seller. Check listing for details.",
        customer_service="1-866-540-3229"
    ),

    "bestbuy": ReturnInfo(
        merchant_name="Best Buy",
        return_address="Best Buy Returns (use in-store or online portal)",
        return_portal_url="https://www.bestbuy.com/profile/ss/orderlookup",
        return_window_days=15,
        free_return_label=True,
        instructions="Return to any Best Buy store or request prepaid shipping label. Elite/Elite Plus members get extended return windows.",
        customer_service="1-888-237-8289"
    ),

    "apple": ReturnInfo(
        merchant_name="Apple",
        return_address="Apple Returns Center\nATTN: Returns\n1 Infinite Loop\nCupertino, CA 95014",
        return_portal_url="https://www.apple.com/shop/help/returns_refund",
        return_window_days=14,
        free_return_label=True,
        instructions="Request return through Apple website. Free prepaid label provided. Can also return to Apple Store.",
        customer_service="1-800-275-2273"
    ),

    "nike": ReturnInfo(
        merchant_name="Nike",
        return_address="Nike Returns\nc/o Cintas Corporation #19\n6700 Melton Road\nGary, IN 46403",
        return_portal_url="https://www.nike.com/orders",
        return_window_days=60,
        free_return_label=True,
        instructions="Request return online. Free prepaid label provided via email. Nike Members get 60 days, others 30 days.",
        customer_service="1-800-806-6453"
    ),

    "adidas": ReturnInfo(
        merchant_name="Adidas",
        return_address="adidas Returns\n3401 NW 159th Street\nMiami Gardens, FL 33014",
        return_portal_url="https://www.adidas.com/us/help/returns-exchanges",
        return_window_days=30,
        free_return_label=True,
        instructions="Request return online. Free prepaid label provided. Adiclub members may have extended windows.",
        customer_service="1-800-982-9337"
    ),

    "zara": ReturnInfo(
        merchant_name="Zara",
        return_address="Zara Returns (use in-store or online portal)",
        return_portal_url="https://www.zara.com/us/en/help-center/my-account/returns",
        return_window_days=30,
        free_return_label=True,
        instructions="Return to any Zara store or request free prepaid label online. 30 days from shipping date.",
        customer_service="1-855-635-9272"
    ),

    "hm": ReturnInfo(
        merchant_name="H&M",
        return_address="H&M Returns (use in-store or online portal)",
        return_portal_url="https://www2.hm.com/en_us/customer-service/returns.html",
        return_window_days=30,
        free_return_label=True,
        instructions="Return to H&M store or request prepaid label online. Keep tags attached.",
        customer_service="1-855-466-7467"
    ),

    "etsy": ReturnInfo(
        merchant_name="Etsy",
        return_address="Varies by seller - check order details",
        return_portal_url="https://www.etsy.com/your/purchases",
        return_window_days=0,  # Varies by seller
        instructions="Contact seller directly through Etsy Messages. Each shop sets their own return policy. Check listing for details.",
        customer_service="https://www.etsy.com/help/contact"
    ),

    "macys": ReturnInfo(
        merchant_name="Macy's",
        return_address="Macy's Returns (use in-store or online portal)",
        return_portal_url="https://www.macys.com/service/returns",
        return_window_days=90,
        free_return_label=True,
        instructions="Return to any Macy's store or request prepaid label online. Most items 90 days, some exclusions apply.",
        customer_service="1-800-289-6229"
    ),

    "nordstrom": ReturnInfo(
        merchant_name="Nordstrom",
        return_address="Nordstrom Returns (use in-store or online portal)",
        return_portal_url="https://www.nordstrom.com/browse/customer-service/returns-exchanges",
        return_window_days=90,  # Flexible policy
        free_return_label=True,
        instructions="Nordstrom has very flexible returns. Return to any Nordstrom/Nordstrom Rack or request free label online.",
        customer_service="1-888-282-6060"
    ),
}


def find_merchant(merchant_name: str) -> Optional[ReturnInfo]:
    """
    Find merchant return information by name.
    Uses fuzzy matching to handle variations in merchant names.
    """
    merchant_lower = merchant_name.lower().strip()

    # Direct lookup
    if merchant_lower in MERCHANT_DATABASE:
        return MERCHANT_DATABASE[merchant_lower]

    # Fuzzy matching
    for key, info in MERCHANT_DATABASE.items():
        if key in merchant_lower or merchant_lower in key:
            return info
        if info.merchant_name.lower() in merchant_lower:
            return info

    return None


def get_all_merchants():
    """Get list of all supported merchants"""
    return [info.merchant_name for info in MERCHANT_DATABASE.values()]
