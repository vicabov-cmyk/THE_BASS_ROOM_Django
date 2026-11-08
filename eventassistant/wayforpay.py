import hashlib
import hmac

def create_signature(values, secret_key):
    message = ";".join(str(value) for value in values)

    return hmac.new(
        secret_key.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.md5
    ).hexdigest()

def verify_signature(values, signature, secret_key):
    expected = create_signature(values, secret_key)
    return hmac.compare_digest(expected, signature)

def build_payment_data(ticket, merchant_domain):

    from django.conf import settings

    account = settings.WAYFORPAY_MERCHANT_ACCOUNT

    secret = settings.WAYFORPAY_SECRET_KEY

    if not account or not secret:

        raise ValueError("WayForPay не налаштовано")

    if ticket.is_paid:

        raise ValueError("Квиток уже оплачено")

    amount = f"{ticket.price:.2f}"

    order_date = int(ticket.created_at.timestamp())

    order_ref = str(ticket.order_reference)

    product = f"THE BASS ROOM - {ticket.event.title}"

    values = [

        account, merchant_domain, order_ref,

        order_date, amount, "UAH",

        product, 1, amount

    ]

    return {

        "merchantAccount": account,

        "merchantDomainName": merchant_domain,

        "merchantTransactionSecureType": "AUTO",

        "orderReference": order_ref,

        "orderDate": order_date,

        "amount": amount,

        "currency": "UAH",

        "productName[]": product,

        "productCount[]": 1,

        "productPrice[]": amount,

        "merchantSignature": create_signature(

            values, secret

        ),

    }