from __future__ import print_function
import gdax as GDAX
from datetime import datetime, timedelta
from pytz import timezone
from dateutil.parser import parse
import boto3
import os
import base64

# Credentials or GDAX. Doesn't need to be able to trade or transfer!
b64secret = base64.b64encode(base64.b64decode(os.environ['secret']))
key = os.environ['key']
pass_phrase = os.environ['pass_phrase']

# Standard AWS credentials
aws_access_key_id = os.environ['aws_access_key_id']
aws_secret_access_key = os.environ['aws_secret_access_key']
region_name = os.environ['region_name']  # example 'us-east-1'

# The phone number to send a text too
phone_number = os.environ['phone_number']  # example +15556667777
SECONDS_TO_CHECK = 61
PAIR = 'ETH-USD'

authClient = GDAX.AuthenticatedClient(key, b64secret, pass_phrase)
print('client generated')

sns = boto3.client(
    'sns',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)


def handler(event, context):
    if context == 'test' or event == 'test':
        # This is a test
        sns.publish(PhoneNumber=phone_number, Message='This is a test')
        print('Test Text sent')

    # GDAX is in the US/Eastern timezone
    now = datetime.now(timezone('US/Eastern'))
    earlier = now - timedelta(seconds=SECONDS_TO_CHECK)

    fills = authClient.get_fills(product_id=PAIR, limit=20)
    recent_trades = [fill
                     for fill in fills[0]
                     if parse(fill['created_at']) >= earlier
                     and fill['settled']]
    if recent_trades:
        for trade in recent_trades:
            print(trade)
            message = "your {side} of {size} for {price} has been settled".format(side=trade['side'],
                                                                                  size=round(float(trade['size']), 2),
                                                                                  price=round(float(trade['price']), 2))
            sns.publish(PhoneNumber=phone_number, Message=message)


handler(None, None)
