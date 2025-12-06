"""
Order Confirmation Parser
Extracts return-relevant information from order confirmations, receipts, and emails.
"""

import re
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from dataclasses import dataclass
import PyPDF2
from PIL import Image
import pytesseract


@dataclass
class ParsedOrder:
    merchant_name: Optional[str]
    order_number: Optional[str]
    order_date: Optional[datetime]
    return_by_date: Optional[datetime]
    items: List[str]
    total_amount: Optional[str]
    extracted_return_address: Optional[str]
    raw_text: str


class OrderParser:
    """Parse order confirmations to extract return information"""

    # Common merchant patterns
    MERCHANT_PATTERNS = [
        (r'amazon\.com', 'amazon'),
        (r'walmart\.com', 'walmart'),
        (r'target\.com', 'target'),
        (r'ebay\.com', 'ebay'),
        (r'bestbuy\.com', 'bestbuy'),
        (r'apple\.com', 'apple'),
        (r'nike\.com', 'nike'),
        (r'adidas\.com', 'adidas'),
        (r'zara\.com', 'zara'),
        (r'hm\.com|h&m', 'hm'),
        (r'etsy\.com', 'etsy'),
        (r'macys\.com', 'macys'),
        (r'nordstrom\.com', 'nordstrom'),
    ]

    # Order number patterns
    ORDER_PATTERNS = [
        r'order\s*#?\s*:?\s*([A-Z0-9-]{6,})',
        r'order\s+number\s*:?\s*([A-Z0-9-]{6,})',
        r'order\s+id\s*:?\s*([A-Z0-9-]{6,})',
        r'confirmation\s*#?\s*:?\s*([A-Z0-9-]{6,})',
    ]

    # Date patterns
    DATE_PATTERNS = [
        r'order\s+date\s*:?\s*(\w+ \d{1,2},? \d{4})',
        r'placed\s+on\s*:?\s*(\w+ \d{1,2},? \d{4})',
        r'(\d{1,2}/\d{1,2}/\d{4})',
        r'(\d{4}-\d{2}-\d{2})',
    ]

    # Return address patterns
    RETURN_ADDRESS_PATTERNS = [
        r'return\s+(?:to|address)\s*:?\s*([^\n]{20,})',
        r'returns?\s+center\s*:?\s*([^\n]{20,})',
        r'send\s+returns?\s+to\s*:?\s*([^\n]{20,})',
    ]

    def parse_text(self, text: str) -> ParsedOrder:
        """Parse text content from order confirmation"""

        # Extract merchant
        merchant = self._extract_merchant(text)

        # Extract order number
        order_number = self._extract_order_number(text)

        # Extract dates
        order_date = self._extract_order_date(text)
        return_by_date = self._calculate_return_deadline(order_date, merchant)

        # Extract items
        items = self._extract_items(text)

        # Extract total
        total = self._extract_total(text)

        # Extract return address if present
        return_address = self._extract_return_address(text)

        return ParsedOrder(
            merchant_name=merchant,
            order_number=order_number,
            order_date=order_date,
            return_by_date=return_by_date,
            items=items,
            total_amount=total,
            extracted_return_address=return_address,
            raw_text=text
        )

    def parse_pdf(self, pdf_path: str) -> ParsedOrder:
        """Extract text from PDF and parse"""
        text = ""

        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
        except Exception as e:
            print(f"Error reading PDF: {e}")
            text = ""

        return self.parse_text(text)

    def parse_image(self, image_path: str) -> ParsedOrder:
        """Extract text from image using OCR and parse"""
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
        except Exception as e:
            print(f"Error reading image: {e}")
            text = ""

        return self.parse_text(text)

    def _extract_merchant(self, text: str) -> Optional[str]:
        """Identify merchant from text"""
        text_lower = text.lower()

        for pattern, merchant_key in self.MERCHANT_PATTERNS:
            if re.search(pattern, text_lower):
                return merchant_key

        # Try to find merchant name in common positions
        lines = text.split('\n')
        if lines:
            # Often merchant name is in first few lines
            for line in lines[:5]:
                line_clean = line.strip()
                if len(line_clean) > 3 and len(line_clean) < 50:
                    # Check if it matches known merchants
                    for pattern, merchant_key in self.MERCHANT_PATTERNS:
                        if re.search(pattern, line_clean.lower()):
                            return merchant_key

        return None

    def _extract_order_number(self, text: str) -> Optional[str]:
        """Extract order number"""
        for pattern in self.ORDER_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return None

    def _extract_order_date(self, text: str) -> Optional[datetime]:
        """Extract order date"""
        for pattern in self.DATE_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                date_str = match.group(1)
                try:
                    # Try various date formats
                    for fmt in ['%B %d, %Y', '%b %d, %Y', '%m/%d/%Y', '%Y-%m-%d',
                               '%B %d %Y', '%b %d %Y']:
                        try:
                            return datetime.strptime(date_str, fmt)
                        except ValueError:
                            continue
                except Exception:
                    pass
        return None

    def _calculate_return_deadline(self, order_date: Optional[datetime],
                                   merchant: Optional[str]) -> Optional[datetime]:
        """Calculate return deadline based on merchant policy"""
        if not order_date:
            return None

        # Import here to avoid circular dependency
        from merchant_database import find_merchant

        merchant_info = find_merchant(merchant) if merchant else None

        if merchant_info:
            return order_date + timedelta(days=merchant_info.return_window_days)
        else:
            # Default to 30 days if unknown
            return order_date + timedelta(days=30)

    def _extract_items(self, text: str) -> List[str]:
        """Extract item names (basic implementation)"""
        items = []

        # Look for lines that might be items
        # This is a simplified version - could be enhanced with ML
        lines = text.split('\n')
        in_items_section = False

        for line in lines:
            line_clean = line.strip()

            # Detect items section
            if re.search(r'items?|products?|order\s+details', line_clean, re.IGNORECASE):
                in_items_section = True
                continue

            # Exit items section
            if re.search(r'total|subtotal|shipping|tax', line_clean, re.IGNORECASE):
                in_items_section = False

            # Collect items
            if in_items_section and len(line_clean) > 5 and len(line_clean) < 100:
                # Filter out likely non-item lines
                if not re.search(r'^\$|^quantity|^price|^qty', line_clean, re.IGNORECASE):
                    items.append(line_clean)

        return items[:10]  # Limit to first 10 items

    def _extract_total(self, text: str) -> Optional[str]:
        """Extract order total"""
        # Look for total amount
        patterns = [
            r'order\s+total\s*:?\s*\$?([\d,]+\.\d{2})',
            r'total\s*:?\s*\$?([\d,]+\.\d{2})',
            r'amount\s+charged\s*:?\s*\$?([\d,]+\.\d{2})',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return f"${match.group(1)}"

        return None

    def _extract_return_address(self, text: str) -> Optional[str]:
        """Extract return address if mentioned in confirmation"""
        for pattern in self.RETURN_ADDRESS_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                address = match.group(1).strip()
                # Clean up and validate
                if len(address) > 20 and len(address) < 200:
                    return address
        return None


# Convenience function
def parse_order_confirmation(file_path: str) -> ParsedOrder:
    """
    Parse an order confirmation file (PDF, image, or text)
    Returns ParsedOrder with extracted information
    """
    parser = OrderParser()

    if file_path.lower().endswith('.pdf'):
        return parser.parse_pdf(file_path)
    elif file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        return parser.parse_image(file_path)
    elif file_path.lower().endswith('.txt'):
        with open(file_path, 'r') as f:
            return parser.parse_text(f.read())
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
