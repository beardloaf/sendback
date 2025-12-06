# SendBack - Quick Start Guide

Get started with SendBack in 3 easy ways: Web Interface, CLI, or API.

## Prerequisites

### Install Python Dependencies

```bash
# Install Tesseract OCR (for image parsing)
# Ubuntu/Debian:
sudo apt-get install tesseract-ocr

# macOS:
brew install tesseract

# Install Python packages
pip install -r requirements.txt
```

## Option 1: Web Interface (Easiest)

### Start the Backend API

```bash
python app.py
```

The API will start on `http://localhost:5000`

### Start the Web Interface

In a new terminal:

```bash
python web_server.py
```

Visit `http://localhost:8000` in your browser!

### Using the Web Interface

**Quick Search** (NEW!):
1. **Type** any merchant name (e.g., "Nike", "Amazon", "Apple")
2. **Click** Search to get instant return info
3. **Click** "Get Free Return Label" to go to their portal
4. **View** return address and instructions

**OR Upload Order**:
1. **Upload** your order confirmation (PDF, screenshot, or text file)
   - OR paste the text directly
2. **Review** extracted information
3. **Get return address** and instructions
4. **Click** "Open Return Portal" for free prepaid label
5. **Follow** step-by-step instructions

## Option 2: Command Line

### Quick Merchant Search (NEW!)

Just type any merchant name to get return info instantly:

```bash
# Search for any merchant
python cli.py search nike
python cli.py search macbook
python cli.py search samsung
python cli.py search target
```

### Parse an Order Confirmation

```bash
python cli.py parse examples/amazon_order.txt
```

### Look Up Merchant Information (Exact Match)

```bash
python cli.py merchant nike
```

### List All Supported Merchants

```bash
python cli.py list
```

## Option 3: Use as Python Library

```python
from order_parser import parse_order_confirmation
from merchant_database import find_merchant

# Parse order confirmation
parsed = parse_order_confirmation('path/to/order.pdf')

print(f"Merchant: {parsed.merchant_name}")
print(f"Order #: {parsed.order_number}")
print(f"Return by: {parsed.return_by_date}")

# Get merchant return info
merchant = find_merchant(parsed.merchant_name)
if merchant:
    print(f"Return Address: {merchant.return_address}")
    print(f"Portal: {merchant.return_portal_url}")
    print(f"Instructions: {merchant.instructions}")
```

## Try the Examples

We've included sample order confirmations to test:

```bash
# Parse Amazon order
python cli.py parse examples/amazon_order.txt

# Parse Nike order
python cli.py parse examples/nike_order.txt
```

## Common Use Cases

### 1. Return an Amazon Order

```bash
# Parse your order confirmation
python cli.py parse ~/Downloads/amazon_order.pdf

# Or look up Amazon's return info directly
python cli.py merchant amazon
```

Then visit the return portal URL shown to get your free prepaid label!

### 2. Check Return Deadline

Upload any order confirmation and SendBack will:
- Extract the order date
- Calculate the return deadline based on merchant policy
- Warn you if deadline is approaching

### 3. Find Return Address for Any Merchant

```bash
python cli.py merchant walmart
python cli.py merchant target
python cli.py merchant nike
```

### 4. Bulk Process Multiple Orders

```python
import glob
from order_parser import parse_order_confirmation

# Parse all PDFs in a folder
for order_file in glob.glob('~/Downloads/orders/*.pdf'):
    parsed = parse_order_confirmation(order_file)

    # Check if return deadline is soon
    if parsed.return_by_date:
        days_left = (parsed.return_by_date - datetime.now()).days
        if days_left < 14:
            print(f"⚠️  Return {parsed.order_number} soon! ({days_left} days left)")
```

## API Endpoints

If you want to integrate SendBack into your own app:

### Parse Order File
```bash
curl -X POST http://localhost:5000/api/parse \
  -F "file=@order.pdf"
```

### Parse Text
```bash
curl -X POST http://localhost:5000/api/parse/text \
  -H "Content-Type: application/json" \
  -d '{"text": "Order #123... Amazon.com..."}'
```

### Get Merchant Info
```bash
curl http://localhost:5000/api/merchant/amazon
```

### List All Merchants
```bash
curl http://localhost:5000/api/merchants
```

## Tips for Best Results

### Order Parsing

- **PDFs work best** - Most reliable for text extraction
- **Clear screenshots** - Ensure text is readable
- **Complete confirmations** - Include merchant name, order #, date
- **Copy-paste** - For emails, copying text directly works great

### Getting Free Return Labels

1. Most major retailers offer FREE prepaid labels
2. Visit the return portal URL provided by SendBack
3. Log in with your account
4. Select your order and items to return
5. Download and print the label
6. Drop off at specified carrier (UPS, USPS, FedEx)

### Merchant Database

We maintain return information for **50+ major retailers**:
- **Retail**: Amazon, Walmart, Target, Costco, Sam's Club
- **Clothing**: Nike, Adidas, Zara, H&M, Gap, Old Navy, Lululemon, Patagonia
- **Tech**: Apple, Samsung, Microsoft, Dell, HP, Lenovo, Sony, Best Buy
- **Department**: Nordstrom, Macy's, Kohl's, JCPenney
- **Home**: Home Depot, Lowe's, Wayfair, IKEA
- **Beauty**: Sephora, Ulta
- **Outdoor**: REI, Patagonia, The North Face
- **Pets**: Chewy, Petco, PetSmart
- And more!

All addresses are **official business addresses** (public record).

**Just search for any merchant name to get started!**

## Environmental Impact

By making returns easier:
- ✅ Products don't end up in landfills
- ✅ Items can be resold or refurbished
- ✅ You get your money back
- ✅ Make better purchasing decisions next time

**Resistance to consumerism through consumer rights!**

## Need Help?

- Check `README.md` for full documentation
- Example files in `examples/` folder
- All merchant return policies in `merchant_database.py`

## Legal & Ethical Use

SendBack is designed for **legitimate returns only**:
- ✅ Use official merchant return processes
- ✅ Follow return policies and timeframes
- ✅ Only use business addresses (no personal addresses)
- ❌ Do not abuse return policies
- ❌ Do not harass companies or individuals

**Use responsibly and ethically.**
