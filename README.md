# SendBack - Ethical Return Automation

**Making returns easier to reduce waste and support consumer rights**

## Purpose

SendBack helps you return unwanted products through legitimate channels instead of letting them end up in landfills. The app automates the tedious process of finding return addresses, understanding return policies, and generating return labels.

## Features

✅ **Order Parsing**: Extract return information from order confirmations and receipts
✅ **Return Database**: Access official business return addresses for major retailers
✅ **Label Helper**: Direct links to official merchant return portals for free labels
✅ **Deadline Tracking**: Never miss a return window again
✅ **Policy Lookup**: Understand each merchant's return requirements

## Ethical Guidelines

This tool is designed for **legitimate returns only**:
- Uses only official business return addresses
- Directs users to authorized return label services
- Respects merchant return policies and timeframes
- Does NOT facilitate harassment or fraud

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+ (for web interface)

### Installation

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install web dependencies
cd web && npm install

# Start the backend
python app.py

# Start the frontend (in another terminal)
cd web && npm run dev
```

### Usage

1. **Upload Order Confirmation**: Email, PDF, or screenshot
2. **Review Extracted Info**: Merchant, order date, return window
3. **Get Return Address**: Official business return address
4. **Generate Label**: Link to merchant's official return portal
5. **Track Your Return**: Monitor status and deadlines

## How It Works

### 1. Order Parsing
Uses OCR and text extraction to find:
- Merchant name and order number
- Purchase date and return deadline
- Product details
- Existing return addresses from confirmation

### 2. Return Address Lookup
Maintains a database of official return addresses:
- Corporate return centers
- Official business addresses (public record)
- Return portal URLs
- Customer service contacts

### 3. Label Generation
Provides direct links to:
- Merchant return portals (most offer free prepaid labels)
- Official return request forms
- Customer service for assistance

## Merchant Database

We maintain return information for major retailers including:
- Amazon, eBay, Walmart, Target
- Clothing retailers (Zara, H&M, Nike, etc.)
- Electronics (Best Buy, Apple, etc.)
- Direct-to-consumer brands

All addresses are **publicly available business addresses** only.

## Privacy

- All processing happens locally on your device
- No order data is stored on external servers
- Optional cloud sync (encrypted, user-controlled)

## Contributing

Help expand the merchant database with official return information:
1. Only public business addresses
2. Verify through official merchant websites
3. Include return policy links

## License

MIT License - Use responsibly and ethically

## Disclaimer

This tool is for legitimate product returns only. Users are responsible for complying with merchant return policies and shipping regulations. Misuse for harassment or fraud is prohibited and may be illegal.

---

**Anti-consumerism through consumer rights**: The best way to resist wasteful consumption is to make it easy to return products, get refunds, and choose more carefully next time.
