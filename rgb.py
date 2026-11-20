import argparse
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
p=argparse.ArgumentParser(); p.add_argument('color', help='Six-digit RGB hex'); p.add_argument('--host',default='127.0.0.1'); a=p.parse_args()
try:
    c=bytes.fromhex(a.color.removeprefix('#'))
    if len(c)!=3: raise ValueError()
except ValueError: p.error('Use a six-digit hex color')
for device in OpenRGBClient(a.host).devices:
    device.set_color(RGBColor(*c))

