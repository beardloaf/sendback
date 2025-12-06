# SendBack - Ethical Return Automation

**Making returns easier to reduce waste and support consumer rights**

## Purpose

SendBack helps you return unwanted products through legitimate channels instead of letting them end up in landfills. The app automates the tedious process of finding return addresses, understanding return policies, and generating return labels.

## Features

🔍 **Quick Merchant Search**: Just type any merchant name to get return info instantly (NEW!)
✅ **Order Parsing**: Extract return information from order confirmations and receipts
✅ **Return Database**: 50+ merchants with official business return addresses
✅ **Free Label Helper**: Direct links to official merchant return portals for free prepaid labels
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

**Option 1: Quick Search**
1. **Search Merchant**: Type merchant name (e.g., "Nike", "Amazon", "Samsung")
2. **Get Instant Info**: Return address, portal URL, and instructions
3. **Get Free Label**: Click link to merchant's return portal

**Option 2: Upload Order**
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

We maintain return information for **80+ retailers** including the ones that make returns hardest:

### Major Retailers
- **Retail**: Amazon, Walmart, Target, eBay, Costco, Sam's Club
- **Clothing**: Nike, Adidas, Zara, H&M, Gap, Old Navy, Lululemon, Patagonia
- **Tech**: Apple, Samsung, Microsoft, Dell, HP, Lenovo, Sony, Best Buy
- **Department Stores**: Nordstrom, Macy's, Kohl's, JCPenney
- **Home**: Home Depot, Lowe's, Wayfair, IKEA
- **Beauty**: Sephora, Ulta, Glossier, The Ordinary
- **Outdoor**: REI, The North Face
- **Pets**: Chewy, Petco, PetSmart

### Hard-to-Find Brands (The ones that obscure their return addresses!)
- **International**: SHEIN, Temu, AliExpress, Wish
- **Fast Fashion**: Fashion Nova, PrettyLittleThing, Boohoo, ZAFUL, ROMWE
- **DTC Brands**: Allbirds, Warby Parker, Casper, Purple, Gymshark, Fabletics
- **Subscriptions**: Stitch Fix, FabFitFun, Ipsy, Blue Apron, HelloFresh
- **Health/Beauty**: Hims, Keeps, Curology, Dollar Shave Club

All addresses are **publicly available business addresses** only.

**Fighting corporate opacity - making it impossible for companies to hide from returns!**

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
