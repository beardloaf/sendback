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

    "gap": ReturnInfo(
        merchant_name="Gap",
        return_address="Gap Returns (use in-store or online portal)",
        return_portal_url="https://www.gap.com/customerService/info.do?cid=35433",
        return_window_days=45,
        free_return_label=True,
        instructions="Return to any Gap, Old Navy, Banana Republic or Athleta store, or request free prepaid label online.",
        customer_service="1-800-427-7895"
    ),

    "oldnavy": ReturnInfo(
        merchant_name="Old Navy",
        return_address="Old Navy Returns (use in-store or online portal)",
        return_portal_url="https://oldnavy.gap.com/customerService/info.do?cid=35433",
        return_window_days=45,
        free_return_label=True,
        instructions="Return to any Old Navy, Gap, Banana Republic or Athleta store, or request free prepaid label online.",
        customer_service="1-800-653-6289"
    ),

    "kohls": ReturnInfo(
        merchant_name="Kohl's",
        return_address="Kohl's Returns (use in-store or online portal)",
        return_portal_url="https://www.kohls.com/ecomweb/pglanding.jsp?destPage=account/myaccount.jsp",
        return_window_days=180,
        free_return_label=True,
        instructions="Kohl's offers 180-day returns! Return to any Kohl's store or request free Amazon returns at Kohl's.",
        customer_service="1-855-564-5705"
    ),

    "jcpenney": ReturnInfo(
        merchant_name="JCPenney",
        return_address="JCPenney Returns (use in-store or online portal)",
        return_portal_url="https://www.jcpenney.com/m/return-policy",
        return_window_days=60,
        free_return_label=True,
        instructions="Return to any JCPenney store or request prepaid label online. 60 days for most items.",
        customer_service="1-800-322-1189"
    ),

    "sephora": ReturnInfo(
        merchant_name="Sephora",
        return_address="Sephora Returns (use in-store or online portal)",
        return_portal_url="https://www.sephora.com/returns-exchanges",
        return_window_days=60,
        free_return_label=True,
        instructions="Return to any Sephora store or by mail with prepaid label. Beauty Insider members get free returns.",
        customer_service="1-877-737-4672"
    ),

    "ulta": ReturnInfo(
        merchant_name="Ulta Beauty",
        return_address="Ulta Returns (use in-store or online portal)",
        return_portal_url="https://www.ulta.com/guest/returns-exchanges/",
        return_window_days=60,
        free_return_label=True,
        instructions="Return to any Ulta store or request prepaid label online. 60 days with receipt.",
        customer_service="1-866-983-8582"
    ),

    "homedepot": ReturnInfo(
        merchant_name="Home Depot",
        return_address="Home Depot Returns (use in-store or online portal)",
        return_portal_url="https://www.homedepot.com/c/Return_Policy",
        return_window_days=90,
        free_return_label=True,
        instructions="Return to any Home Depot store or request online return. 90 days for most items.",
        customer_service="1-800-466-3337"
    ),

    "lowes": ReturnInfo(
        merchant_name="Lowe's",
        return_address="Lowe's Returns (use in-store or online portal)",
        return_portal_url="https://www.lowes.com/l/returns-and-refunds",
        return_window_days=90,
        free_return_label=True,
        instructions="Return to any Lowe's store or request prepaid label for online orders. 90 days for most items.",
        customer_service="1-800-445-6937"
    ),

    "wayfair": ReturnInfo(
        merchant_name="Wayfair",
        return_address="Wayfair Returns (use online portal)",
        return_portal_url="https://www.wayfair.com/help/article/return_policy",
        return_window_days=30,
        free_return_label=True,
        instructions="Request return online. Free return shipping for most items. Large items may have pickup arranged.",
        customer_service="1-844-932-9324"
    ),

    "ikea": ReturnInfo(
        merchant_name="IKEA",
        return_address="IKEA Returns (use in-store or online portal)",
        return_portal_url="https://www.ikea.com/us/en/customer-service/returns-claims/",
        return_window_days=365,
        free_return_label=False,
        instructions="IKEA offers 365-day returns! Return to any IKEA store with receipt. Online orders may qualify for pickup.",
        customer_service="1-888-888-4532"
    ),

    "costco": ReturnInfo(
        merchant_name="Costco",
        return_address="Costco Returns (return to warehouse)",
        return_portal_url="https://www.costco.com/returns.html",
        return_window_days=90,  # Most items unlimited
        free_return_label=False,
        instructions="Most items can be returned anytime! Electronics 90 days. Return to any Costco warehouse.",
        customer_service="1-800-774-2678"
    ),

    "samsclub": ReturnInfo(
        merchant_name="Sam's Club",
        return_address="Sam's Club Returns (return to club)",
        return_portal_url="https://www.samsclub.com/content/return-policy",
        return_window_days=90,
        free_return_label=False,
        instructions="Most items can be returned to any Sam's Club. Electronics 90 days. Membership required.",
        customer_service="1-888-746-7726"
    ),

    "chewy": ReturnInfo(
        merchant_name="Chewy",
        return_address="Chewy Returns\n3940 Royal Drive NW\nKennesaw, GA 30144",
        return_portal_url="https://www.chewy.com/app/account/orders",
        return_window_days=365,
        free_return_label=True,
        instructions="Contact customer service for return. 365-day return policy! Free prepaid label provided.",
        customer_service="1-800-672-4399"
    ),

    "petco": ReturnInfo(
        merchant_name="Petco",
        return_address="Petco Returns (use in-store or online portal)",
        return_portal_url="https://www.petco.com/shop/OrderHistoryView",
        return_window_days=60,
        free_return_label=True,
        instructions="Return to any Petco store or request prepaid label online. 60 days with receipt.",
        customer_service="1-877-738-6742"
    ),

    "petsmart": ReturnInfo(
        merchant_name="PetSmart",
        return_address="PetSmart Returns (use in-store)",
        return_portal_url="https://www.petsmart.com/help/returns-and-refunds/",
        return_window_days=60,
        free_return_label=False,
        instructions="Return to any PetSmart store within 60 days with receipt. Online orders eligible for return.",
        customer_service="1-888-839-9638"
    ),

    "macbook": ReturnInfo(
        merchant_name="Apple MacBook",
        return_address="Apple Returns Center\nATTN: Returns\n1 Infinite Loop\nCupertino, CA 95014",
        return_portal_url="https://www.apple.com/shop/help/returns_refund",
        return_window_days=14,
        free_return_label=True,
        instructions="Request return through Apple website. Free prepaid label provided. Can also return to Apple Store.",
        customer_service="1-800-275-2273"
    ),

    "samsung": ReturnInfo(
        merchant_name="Samsung",
        return_address="Samsung Returns (use online portal)",
        return_portal_url="https://www.samsung.com/us/support/returns/",
        return_window_days=15,
        free_return_label=True,
        instructions="Request return through Samsung website. Free prepaid label provided for most items.",
        customer_service="1-800-726-7864"
    ),

    "sony": ReturnInfo(
        merchant_name="Sony",
        return_address="Sony Returns (use online portal)",
        return_portal_url="https://www.sony.com/electronics/support/orders-returns-exchanges",
        return_window_days=30,
        free_return_label=True,
        instructions="Request return online. Free prepaid label provided. 30 days for unopened items.",
        customer_service="1-800-942-7669"
    ),

    "microsoft": ReturnInfo(
        merchant_name="Microsoft",
        return_address="Microsoft Returns (use online portal)",
        return_portal_url="https://account.microsoft.com/orders",
        return_window_days=60,
        free_return_label=True,
        instructions="Request return through Microsoft account. Free prepaid label provided. Can also return to Microsoft Store.",
        customer_service="1-877-696-7786"
    ),

    "dell": ReturnInfo(
        merchant_name="Dell",
        return_address="Dell Returns (use online portal)",
        return_portal_url="https://www.dell.com/support/contents/en-us/article/order-support/order-tracking/return-policy",
        return_window_days=30,
        free_return_label=True,
        instructions="Contact Dell to initiate return. Free prepaid label provided for most items.",
        customer_service="1-800-624-9897"
    ),

    "hp": ReturnInfo(
        merchant_name="HP",
        return_address="HP Returns (use online portal)",
        return_portal_url="https://www.hp.com/us-en/shop/cv/returns",
        return_window_days=30,
        free_return_label=True,
        instructions="Request return through HP website. Free prepaid label provided.",
        customer_service="1-800-474-6836"
    ),

    "lenovo": ReturnInfo(
        merchant_name="Lenovo",
        return_address="Lenovo Returns (use online portal)",
        return_portal_url="https://www.lenovo.com/us/en/returns/",
        return_window_days=30,
        free_return_label=True,
        instructions="Request return online. Free prepaid label provided for most items.",
        customer_service="1-855-253-6686"
    ),

    "patagonia": ReturnInfo(
        merchant_name="Patagonia",
        return_address="Patagonia Returns\n8550 White Fir Street\nReno, NV 89523",
        return_portal_url="https://www.patagonia.com/returns.html",
        return_window_days=60,
        free_return_label=True,
        instructions="Request return online or mail to address. Free prepaid label available. Ironclad Guarantee for defects.",
        customer_service="1-800-638-6464"
    ),

    "rei": ReturnInfo(
        merchant_name="REI",
        return_address="REI Returns (use in-store or online portal)",
        return_portal_url="https://www.rei.com/help/return-policy",
        return_window_days=365,
        free_return_label=True,
        instructions="REI members get 1 year to return! Return to any REI store or request free label online.",
        customer_service="1-800-426-4840"
    ),

    "northface": ReturnInfo(
        merchant_name="The North Face",
        return_address="The North Face Returns\nc/o Geodis\n100 Misty Meadow Drive\nMartinsville, VA 24112",
        return_portal_url="https://www.thenorthface.com/help/returns.html",
        return_window_days=60,
        free_return_label=True,
        instructions="Request return online. Free prepaid label provided. Lifetime warranty on manufacturing defects.",
        customer_service="1-888-888-7732"
    ),

    "underarmour": ReturnInfo(
        merchant_name="Under Armour",
        return_address="Under Armour Returns\n1000 Tilghman Drive\nMt. Airy, MD 21771",
        return_portal_url="https://www.underarmour.com/en-us/help/returns",
        return_window_days=60,
        free_return_label=True,
        instructions="Request return online. Free prepaid label provided via email. 60 days from delivery.",
        customer_service="1-888-727-6687"
    ),

    "lululemon": ReturnInfo(
        merchant_name="lululemon",
        return_address="lululemon Returns (use in-store or online portal)",
        return_portal_url="https://shop.lululemon.com/help/returns",
        return_window_days=30,
        free_return_label=True,
        instructions="Return to any lululemon store or request free prepaid label online. Quality Promise for defects.",
        customer_service="1-877-263-9300"
    ),

    "forever21": ReturnInfo(
        merchant_name="Forever 21",
        return_address="Forever 21 Returns (use online portal)",
        return_portal_url="https://www.forever21.com/us/shop/info/returns",
        return_window_days=30,
        free_return_label=False,
        instructions="Return by mail within 30 days. Return shipping fees may apply. Check website for details.",
        customer_service="1-888-494-3837"
    ),

    "urbanoutfitters": ReturnInfo(
        merchant_name="Urban Outfitters",
        return_address="Urban Outfitters Returns (use in-store or online portal)",
        return_portal_url="https://www.urbanoutfitters.com/help/returns",
        return_window_days=30,
        free_return_label=True,
        instructions="Return to any Urban Outfitters store or request prepaid label online. 30 days from delivery.",
        customer_service="1-800-282-2200"
    ),

    "anthropologie": ReturnInfo(
        merchant_name="Anthropologie",
        return_address="Anthropologie Returns (use in-store or online portal)",
        return_portal_url="https://www.anthropologie.com/help/returns-exchanges",
        return_window_days=60,
        free_return_label=True,
        instructions="Return to any Anthropologie store or request free label online. 60 days from purchase.",
        customer_service="1-800-309-2500"
    ),

    "freepeople": ReturnInfo(
        merchant_name="Free People",
        return_address="Free People Returns (use in-store or online portal)",
        return_portal_url="https://www.freepeople.com/help/returns-exchanges/",
        return_window_days=60,
        free_return_label=True,
        instructions="Return to any Free People store or request prepaid label online. 60 days from purchase.",
        customer_service="1-800-309-1500"
    ),

    # Hard-to-find DTC and international brands
    "shein": ReturnInfo(
        merchant_name="SHEIN",
        return_address="SHEIN Returns\nc/o SHEIN Distribution Corporation\n1750 E 6th Street\nCorona, CA 92879",
        return_portal_url="https://us.shein.com/returns-refunds-a-359.html",
        return_window_days=45,
        free_return_label=False,
        instructions="Request return through SHEIN account. Return fees may apply ($7.99). Follow online instructions carefully. Processing can take 2-3 weeks.",
        customer_service="support@shein.com"
    ),

    "temu": ReturnInfo(
        merchant_name="Temu",
        return_address="Temu Returns\nP.O. Box 411046\nBoston, MA 02241",
        return_portal_url="https://www.temu.com/customer-service/return-refund-policy.html",
        return_window_days=90,
        free_return_label=True,
        instructions="Request return through Temu app or website. Free prepaid label provided. 90-day return window. Keep packaging and tags.",
        customer_service="https://www.temu.com/contact-us.html"
    ),

    "aliexpress": ReturnInfo(
        merchant_name="AliExpress",
        return_address="Varies by seller - contact seller first through dispute system",
        return_portal_url="https://www.aliexpress.com/p/order/index.html",
        return_window_days=15,
        free_return_label=False,
        instructions="Open dispute through AliExpress within 15 days. Contact seller first. Return shipping usually buyer's responsibility. May need to ship internationally.",
        customer_service="https://customerservice.aliexpress.com/"
    ),

    "wish": ReturnInfo(
        merchant_name="Wish",
        return_address="Varies by merchant - check order details",
        return_portal_url="https://www.wish.com/settings/order-history",
        return_window_days=30,
        free_return_label=False,
        instructions="Request refund through Wish app within 30 days. May need to contact merchant directly. Return shipping often buyer's responsibility.",
        customer_service="https://www.wish.com/help"
    ),

    "fashionnova": ReturnInfo(
        merchant_name="Fashion Nova",
        return_address="Fashion Nova Returns\n2801 East 46th Street\nVernon, CA 90058",
        return_portal_url="https://www.fashionnova.com/pages/returns",
        return_window_days=30,
        free_return_label=False,
        instructions="Email customer service for return authorization. Must include all tags. Return shipping at customer expense. Store credit only.",
        customer_service="support@fashionnova.com"
    ),

    "prettylittlething": ReturnInfo(
        merchant_name="PrettyLittleThing",
        return_address="PrettyLittleThing Returns\nc/o Inmar Returns\n2 Inmar Drive\nWinston-Salem, NC 27101",
        return_portal_url="https://www.prettylittlething.us/returns.html",
        return_window_days=28,
        free_return_label=False,
        instructions="Create return through account. Return label costs $5.99 (deducted from refund). Items must have tags attached.",
        customer_service="customercare@prettylittlething.com"
    ),

    "boohoo": ReturnInfo(
        merchant_name="boohoo",
        return_address="boohoo Returns\nc/o Inmar Returns\n2 Inmar Drive\nWinston-Salem, NC 27101",
        return_portal_url="https://www.boohoo.com/customer-care/delivery-returns",
        return_window_days=30,
        free_return_label=False,
        instructions="Request return label online ($5.99 fee). Must return within 30 days. Keep tags attached. Processing takes 10-14 days.",
        customer_service="customercare@boohoo.com"
    ),

    "zaful": ReturnInfo(
        merchant_name="ZAFUL",
        return_address="ZAFUL Returns\n1750 E 6th Street\nCorona, CA 92879",
        return_portal_url="https://www.zaful.com/m-return-policy.html",
        return_window_days=30,
        free_return_label=False,
        instructions="Submit return request through account within 30 days. Return shipping at customer expense. Items must be unworn with tags.",
        customer_service="service@zaful.com"
    ),

    "romwe": ReturnInfo(
        merchant_name="ROMWE",
        return_address="ROMWE Returns\n1750 E 6th Street\nCorona, CA 92879",
        return_portal_url="https://www.romwe.com/Return-Policy-a-359.html",
        return_window_days=45,
        free_return_label=False,
        instructions="Request return within 45 days. Return shipping fee applies. Process through online account. Allow 2-3 weeks for processing.",
        customer_service="service@romwe.com"
    ),

    "gymshark": ReturnInfo(
        merchant_name="Gymshark",
        return_address="Gymshark Returns\nc/o Inmar Returns\n2 Inmar Drive\nWinston-Salem, NC 27101",
        return_portal_url="https://www.gymshark.com/pages/returns",
        return_window_days=90,
        free_return_label=True,
        instructions="Create return through Gymshark account. Free prepaid label provided. 90-day return window. Items must be unworn.",
        customer_service="help@gymshark.com"
    ),

    "fabletics": ReturnInfo(
        merchant_name="Fabletics",
        return_address="Fabletics Returns\n3401 NW 159th Street\nMiami Gardens, FL 33014",
        return_portal_url="https://www.fabletics.com/returns",
        return_window_days=45,
        free_return_label=True,
        instructions="VIP members get free returns. Non-members pay return shipping. 45-day window. Process through account online.",
        customer_service="1-844-322-5384"
    ),

    "allbirds": ReturnInfo(
        merchant_name="Allbirds",
        return_address="Allbirds Returns\nc/o Optoro\n4201 Parliament Place Suite L\nLanham, MD 20706",
        return_portal_url="https://www.allbirds.com/pages/returns",
        return_window_days=30,
        free_return_label=True,
        instructions="Free returns within 30 days. Request label through Allbirds website. Even if worn, as long as not damaged. Sustainable returns.",
        customer_service="support@allbirds.com"
    ),

    "casper": ReturnInfo(
        merchant_name="Casper",
        return_address="Casper Returns (contact for pickup)",
        return_portal_url="https://casper.com/returns/",
        return_window_days=100,
        free_return_label=True,
        instructions="100-night trial! Contact Casper for free pickup. They donate returned mattresses to charity. Full refund guaranteed.",
        customer_service="1-888-498-0003"
    ),

    "purple": ReturnInfo(
        merchant_name="Purple",
        return_address="Purple Returns (contact for pickup)",
        return_portal_url="https://purple.com/return-policy",
        return_window_days=100,
        free_return_label=True,
        instructions="100-night trial period. Contact Purple to arrange free pickup. Mattresses donated or recycled. Full refund provided.",
        customer_service="1-888-848-2305"
    ),

    "warbyparker": ReturnInfo(
        merchant_name="Warby Parker",
        return_address="Warby Parker Returns\n233 Spring Street\nNew York, NY 10013",
        return_portal_url="https://www.warbyparker.com/returns",
        return_window_days=30,
        free_return_label=True,
        instructions="Free returns within 30 days. Prepaid label included with order. Can also return at any Warby Parker retail location.",
        customer_service="1-888-492-7297"
    ),

    "glossier": ReturnInfo(
        merchant_name="Glossier",
        return_address="Glossier Returns\n233 Spring Street Floor 8 East\nNew York, NY 10013",
        return_portal_url="https://www.glossier.com/help",
        return_window_days=30,
        free_return_label=False,
        instructions="Email gTEAM for return authorization within 30 days. Return shipping at customer expense. Must be unused/unopened.",
        customer_service="gteam@glossier.com"
    ),

    "theordinary": ReturnInfo(
        merchant_name="The Ordinary",
        return_address="Deciem Returns\n517 Richmond Street East\nToronto, ON M5A 1R4, Canada",
        return_portal_url="https://deciem.com/en-us/returns.html",
        return_window_days=365,
        free_return_label=False,
        instructions="365-day return policy! Contact customer care for return. Must be in original condition. Return shipping at customer expense.",
        customer_service="care@deciem.com"
    ),

    "dollar shave club": ReturnInfo(
        merchant_name="Dollar Shave Club",
        return_address="Dollar Shave Club\n3130 Wilshire Blvd\nSanta Monica, CA 90403",
        return_portal_url="https://www.dollarshaveclub.com/terms",
        return_window_days=60,
        free_return_label=False,
        instructions="Contact customer service within 60 days if not satisfied. They may offer replacement or refund. Return shipping may be required.",
        customer_service="1-800-927-5288"
    ),

    "fabfitfun": ReturnInfo(
        merchant_name="FabFitFun",
        return_address="FabFitFun Returns\n11100 Santa Monica Blvd Suite 600\nLos Angeles, CA 90025",
        return_portal_url="https://support.fabfitfun.com/",
        return_window_days=0,
        free_return_label=False,
        instructions="Subscription boxes generally non-returnable. Contact support for damaged/defective items. May offer replacement or credit.",
        customer_service="support@fabfitfun.com"
    ),

    "ipsy": ReturnInfo(
        merchant_name="Ipsy",
        return_address="Ipsy\n155 5th Street\nSan Francisco, CA 94103",
        return_portal_url="https://www.ipsy.com/help",
        return_window_days=0,
        free_return_label=False,
        instructions="Beauty boxes not returnable. Contact care team for damaged/wrong items within 30 days. May send replacement.",
        customer_service="care@ipsy.com"
    ),

    "blue apron": ReturnInfo(
        merchant_name="Blue Apron",
        return_address="Blue Apron\n5 Crosby Street Floor 3\nNew York, NY 10013",
        return_portal_url="https://www.blueapron.com/pages/contact",
        return_window_days=0,
        free_return_label=False,
        instructions="Meal kits cannot be returned. Contact within 7 days if box arrives damaged or spoiled. Credit may be issued.",
        customer_service="1-646-504-1577"
    ),

    "hellofresh": ReturnInfo(
        merchant_name="HelloFresh",
        return_address="HelloFresh\n1 Harrison Street Suite 175\nSan Francisco, CA 94105",
        return_portal_url="https://www.hellofresh.com/contact-us/",
        return_window_days=0,
        free_return_label=False,
        instructions="Meal boxes not returnable. Report quality issues within 7 days. May receive credit or replacement ingredients.",
        customer_service="1-800-733-2414"
    ),

    "stitch fix": ReturnInfo(
        merchant_name="Stitch Fix",
        return_address="Stitch Fix Returns\n1 Montgomery Street Suite 1500\nSan Francisco, CA 94104",
        return_portal_url="https://www.stitchfix.com/faq/returns",
        return_window_days=3,
        free_return_label=True,
        instructions="3-day try-on period. Free prepaid return bag included. Check out items you want, return the rest. Simple process.",
        customer_service="1-800-449-8641"
    ),

    "curology": ReturnInfo(
        merchant_name="Curology",
        return_address="Curology Returns\n2045 Broadway\nRedwood City, CA 94063",
        return_portal_url="https://curology.com/return-policy",
        return_window_days=60,
        free_return_label=False,
        instructions="Contact within 60 days if not satisfied. May offer different formula or refund. Return shipping at customer expense.",
        customer_service="support@curology.com"
    ),

    "keeps": ReturnInfo(
        merchant_name="Keeps",
        return_address="Keeps\n214 Sullivan Street Suite 4C\nNew York, NY 10012",
        return_portal_url="https://www.keeps.com/help",
        return_window_days=90,
        free_return_label=False,
        instructions="90-day money-back guarantee on first order. Contact support for refund. Unopened products may need to be returned.",
        customer_service="support@keeps.com"
    ),

    "hims": ReturnInfo(
        merchant_name="Hims",
        return_address="Hims & Hers\n150 Spear Street Suite 900\nSan Francisco, CA 94105",
        return_portal_url="https://www.forhims.com/help",
        return_window_days=30,
        free_return_label=False,
        instructions="Contact support within 30 days if not satisfied. Refund policies vary by product. May need to return unopened items.",
        customer_service="support@forhims.com"
    ),
}


# Merchant aliases and alternative names for better search
MERCHANT_ALIASES = {
    "amazon.com": "amazon",
    "amazon prime": "amazon",
    "bestbuy": "bestbuy",
    "best buy": "bestbuy",
    "h&m": "hm",
    "h and m": "hm",
    "old navy": "oldnavy",
    "kohl's": "kohls",
    "jc penney": "jcpenney",
    "home depot": "homedepot",
    "lowe's": "lowes",
    "sam's club": "samsclub",
    "sams club": "samsclub",
    "mac": "apple",
    "iphone": "apple",
    "ipad": "apple",
    "macbook": "apple",
    "macbook pro": "apple",
    "macbook air": "apple",
    "north face": "northface",
    "the north face": "northface",
    "under armour": "underarmour",
    "urban outfitters": "urbanoutfitters",
    "free people": "freepeople",
    "pet smart": "petsmart",
    "ulta beauty": "ulta",
    # DTC and international brands
    "she in": "shein",
    "ali express": "aliexpress",
    "fashion nova": "fashionnova",
    "pretty little thing": "prettylittlething",
    "warby parker": "warbyparker",
    "the ordinary": "theordinary",
    "dollar shave": "dollar shave club",
    "dsc": "dollar shave club",
    "fab fit fun": "fabfitfun",
    "blue apron": "blue apron",
    "hello fresh": "hellofresh",
    "stitch fix": "stitch fix",
    "hims & hers": "hims",
    "for hims": "hims",
}


def find_merchant(merchant_name: str) -> Optional[ReturnInfo]:
    """
    Find merchant return information by name.
    Uses fuzzy matching to handle variations in merchant names.
    """
    if not merchant_name:
        return None

    merchant_lower = merchant_name.lower().strip()

    # Check aliases first
    if merchant_lower in MERCHANT_ALIASES:
        return MERCHANT_DATABASE.get(MERCHANT_ALIASES[merchant_lower])

    # Direct lookup
    if merchant_lower in MERCHANT_DATABASE:
        return MERCHANT_DATABASE[merchant_lower]

    # Fuzzy matching
    for key, info in MERCHANT_DATABASE.items():
        if key in merchant_lower or merchant_lower in key:
            return info
        if info.merchant_name.lower() in merchant_lower:
            return info

    # Check if any alias matches
    for alias, key in MERCHANT_ALIASES.items():
        if alias in merchant_lower:
            return MERCHANT_DATABASE.get(key)

    return None


def search_merchants(query: str, limit: int = 10) -> list[ReturnInfo]:
    """
    Search for merchants by name.
    Returns list of matching merchants sorted by relevance.
    """
    if not query:
        return []

    query_lower = query.lower().strip()
    results = []
    scores = []

    for key, info in MERCHANT_DATABASE.items():
        score = 0

        # Exact match
        if query_lower == key or query_lower == info.merchant_name.lower():
            score = 100

        # Starts with
        elif key.startswith(query_lower) or info.merchant_name.lower().startswith(query_lower):
            score = 80

        # Contains
        elif query_lower in key or query_lower in info.merchant_name.lower():
            score = 60

        # Word boundary match
        elif any(word.startswith(query_lower) for word in info.merchant_name.lower().split()):
            score = 50

        if score > 0:
            results.append(info)
            scores.append(score)

    # Sort by score (descending)
    sorted_results = [x for _, x in sorted(zip(scores, results), reverse=True)]

    return sorted_results[:limit]


def get_all_merchants():
    """Get list of all supported merchants"""
    return sorted([info.merchant_name for info in MERCHANT_DATABASE.values()])


def get_merchant_count():
    """Get total number of merchants in database"""
    return len(MERCHANT_DATABASE)
