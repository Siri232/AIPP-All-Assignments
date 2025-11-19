#!/usr/bin/env python3
"""
TGNPDCL Bill Generator
Interactive CLI with optional command-line args.

Inputs:
 - PU: Price per unit (float)
 - CU: Consumption units (float)
 - type: customer type (domestic/commercial/industrial)
Optional overrides:
 - FC: Fixed Charges
 - CC: Customer Charges
 - ED: Electricity Duty percent

Calculation:
 EC = PU * CU
 subtotal = EC + FC + CC
 ED_amount = subtotal * ED/100
 total_bill = subtotal + ED_amount

Outputs printed: EC, FC, CC, ED (amount and %), Total Bill

Assumptions (reasonable defaults):
 Domestic: FC=50, CC=20, ED=5%
 Commercial : FC=100, CC=50, ED=12%
 Industrial : FC=200, CC=100, ED=18%

"""
import argparse
import sys
from typing import Dict

DEFAULTS = {
    'domestic': {'FC': 50.0, 'CC': 20.0, 'ED': 5.0},
    'commercial':  {'FC': 100.0, 'CC': 50.0, 'ED': 12.0},
    'industrial':  {'FC': 200.0, 'CC': 100.0, 'ED': 18.0},
}


def calculate_bill(pu: float, cu: float, cust_type: str, fc: float = None, cc: float = None, ed_percent: float = None) -> Dict[str, float]:
    """Calculate bill breakdown.

    Returns a dict with EC, FC, CC, ED_percent, ED_amount, subtotal, total.
    """
    t = cust_type.lower()
    if t not in DEFAULTS:
        raise ValueError(f"Unknown customer type: {cust_type}. Choose from {list(DEFAULTS.keys())}")

    defaults = DEFAULTS[t]
    FC = float(fc) if fc is not None else defaults['FC']
    CC = float(cc) if cc is not None else defaults['CC']
    ED = float(ed_percent) if ed_percent is not None else defaults['ED']

    EC = float(pu) * float(cu)
    subtotal = EC + FC + CC
    ED_amount = subtotal * (ED / 100.0)
    total = subtotal + ED_amount

    return {
        'PU': float(pu),
        'CU': float(cu),
        'CustomerType': t,
        'EC': round(EC, 2),
        'FC': round(FC, 2),
        'CC': round(CC, 2),
        'ED_percent': round(ED, 2),
        'ED_amount': round(ED_amount, 2),
        'subtotal': round(subtotal, 2),
        'total': round(total, 2),
    }


def print_bill(b: Dict[str, float]):
    print("\n===== TGNPDCL Energy Bill =====")
    print(f"Customer type : {b['CustomerType'].capitalize()}")
    print(f"Units consumed: {b['CU']:.2f} units")
    print(f"Price per unit: ₹{b['PU']:.2f} /unit")
    print("-------------------------------")
    print(f"EC (Energy Charges) : ₹{b['EC']:.2f}")
    print(f"FC (Fixed Charges)  : ₹{b['FC']:.2f}")
    print(f"CC (Customer Charges): ₹{b['CC']:.2f}")
    print(f"Subtotal            : ₹{b['subtotal']:.2f}")
    print(f"ED ({b['ED_percent']}%)            : ₹{b['ED_amount']:.2f}")
    print("-------------------------------")
    print(f"Total Bill Amount   : ₹{b['total']:.2f}")
    print("===============================\n")


def parse_args(argv=None):
    p = argparse.ArgumentParser(description='TGNPDCL Bill Generator')
    p.add_argument('--pu', type=float, help='Price per unit (₹)')
    p.add_argument('--cu', type=float, help='Consumed units')
    p.add_argument('--type', choices=list(DEFAULTS.keys()), help='Customer type')
    p.add_argument('--fc', type=float, help='Fixed Charges (override)')
    p.add_argument('--cc', type=float, help='Customer Charges (override)')
    p.add_argument('--ed', type=float, help='Electricity Duty % (override)')
    return p.parse_args(argv)


def interactive_input():
    """Prompt user for inputs after the program runs.

    The user may press Enter to accept default FC/CC/ED values shown for the chosen customer type.
    Returns: pu, cu, cust_type, fc_override, cc_override, ed_override
    """
    while True:
        try:
            pu = float(input('Enter Price per Unit (₹): ').strip())
            break
        except ValueError:
            print('Please enter a valid number for Price per Unit.')

    while True:
        try:
            cu = float(input('Enter Consumed Units: ').strip())
            break
        except ValueError:
            print('Please enter a valid number for Consumed Units.')

    while True:
        t = input('Enter Customer Type (domestic/commercial/industrial): ').strip().lower()
        if t in DEFAULTS:
            cust_type = t
            break
        print('Invalid type, choose from domestic/commercial/industrial')

    # show defaults and allow overrides
    defaults = DEFAULTS[cust_type]
    def read_optional(prompt, cast=float):
        val = input(prompt).strip()
        if val == '':
            return None
        try:
            return cast(val)
        except ValueError:
            print('Invalid number, ignoring and using default.')
            return None

    fc_override = read_optional(f"Enter Fixed Charges (FC) [press Enter for default ₹{defaults['FC']}] : ")
    cc_override = read_optional(f"Enter Customer Charges (CC) [press Enter for default ₹{defaults['CC']}] : ")
    ed_override = read_optional(f"Enter Electricity Duty % (ED) [press Enter for default {defaults['ED']}%] : ")

    return pu, cu, cust_type, fc_override, cc_override, ed_override


def main(argv=None):
    # Always prompt the user for inputs after the program starts.
    try:
        pu, cu, cust_type, fc_override, cc_override, ed_override = interactive_input()
    except Exception as e:
        print('Input aborted or invalid:', e)
        sys.exit(1)

    bill = calculate_bill(pu=pu, cu=cu, cust_type=cust_type, fc=fc_override, cc=cc_override, ed_percent=ed_override)
    print_bill(bill)


if __name__ == '__main__':
    main()
