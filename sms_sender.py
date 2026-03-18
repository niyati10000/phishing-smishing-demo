#!/usr/bin/env python3
"""
SMS Message Generator for Smishing Simulation
Generates realistic smishing messages for educational demonstrations
"""

import random
import argparse
from datetime import datetime

class SmishingMessageGenerator:
    """Generate realistic smishing message templates"""
    
    def __init__(self):
        self.templates = {
            'delivery': [
                "📦 {courier}: Your package #{tracking} could not be delivered. Update delivery preferences: {url}",
                "🚚 {courier} - Delivery Failed: We tried to deliver your package but need address confirmation. Visit: {url}",
                "📮 Shipping Update: Your item #{tracking} is on hold. Verify details: {url}",
                "⚠️ {courier}: Delivery exception for package #{tracking}. Resolve here: {url}"
            ],
            'bank': [
                "🏦 {bank}: Suspicious transaction detected on your account. Verify immediately: {url}",
                "⚠️ {bank} Alert: Your account has been limited. Restore access: {url}",
                "🔐 {bank}: New device login detected. If not you, secure account: {url}",
                "💰 {bank}: Your statement is ready. View online: {url}"
            ],
            'government': [
                "📋 IRS Notice: You have a pending tax refund of ${amount}. Claim now: {url}",
                "⚖️ Court Notification: Notice of appearance required. View citation: {url}",
                "💉 Health Dept: COVID-19 vaccine record update required: {url}"
            ],
            'verification': [
                "🔑 {service}: Your account requires verification. Complete now: {url}",
                "📱 {service}: Unusual sign-in attempt. Secure your account: {url}",
                "⚠️ {service}: Your password expires today. Update here: {url}"
            ]
        }
        
        self.couriers = ["FedEx", "UPS", "USPS", "DHL", "Amazon Logistics"]
        self.banks = ["Chase", "Bank of America", "Wells Fargo", "Citibank", "Capital One"]
        self.services = ["Netflix", "PayPal", "Apple ID", "Microsoft", "Google"]
        
    def generate_tracking(self):
        """Generate fake tracking number"""
        return f"{random.choice(['1Z', 'EZ', '94'])}{random.randint(100000000, 999999999)}"
    
    def generate_message(self, attack_type=None):
        """Generate a single smishing message"""
        if not attack_type:
            attack_type = random.choice(list(self.templates.keys()))
        
        template = random.choice(self.templates[attack_type])
        
        # Fill in template variables
        url = f"bit.ly/{random.choice(['verify', 'track', 'secure', 'update'])}{random.randint(100, 999)}"
        
        message = template.format(
            courier=random.choice(self.couriers),
            bank=random.choice(self.banks),
            service=random.choice(self.services),
            tracking=self.generate_tracking(),
            amount=random.choice([str(x) for x in range(50, 1000, 50)]),
            url=f"http://{url}"
        )
        
        return message, attack_type
    
    def generate_batch(self, count=10):
        """Generate multiple messages"""
        messages = []
        for i in range(count):
            msg, type_ = self.generate_message()
            messages.append((i+1, type_, msg))
        return messages

def main():
    parser = argparse.ArgumentParser(description="Smishing Message Generator (Educational)")
    parser.add_argument("-c", "--count", type=int, default=5, help="Number of messages to generate")
    parser.add_argument("-t", "--type", choices=['delivery', 'bank', 'government', 'verification', 'all'], 
                       default='all', help="Type of smishing attack")
    parser.add_argument("-o", "--output", help="Save to file")
    
    args = parser.parse_args()
    
    generator = SmishingMessageGenerator()
    
    print("\n" + "="*60)
    print("SMISHING MESSAGE GENERATOR - EDUCATIONAL USE ONLY")
    print("="*60)
    print("\nThese are examples of REALISTIC smishing messages:")
    print("-" * 60)
    
    messages = []
    if args.type == 'all':
        for type_ in ['delivery', 'bank', 'government', 'verification']:
            for i in range(args.count // 4 + 1):
                msg, t = generator.generate_message(type_)
                messages.append((len(messages)+1, t, msg))
    else:
        for i in range(args.count):
            msg, t = generator.generate_message(args.type)
            messages.append((i+1, t, msg))
    
    # Display messages
    for num, type_, msg in messages[:args.count]:
        print(f"\n[{num}] {type_.upper()} LURE:")
        print(f"    📱 SMS: {msg}")
        print(f"    🔍 Red Flag: Creates urgency + shortened URL")
    
    # Save to file if requested
    if args.output:
        with open(args.output, 'w') as f:
            f.write("SMISHING MESSAGE EXAMPLES - EDUCATIONAL USE\n")
            f.write("="*60 + "\n\n")
            for num, type_, msg in messages:
                f.write(f"[{num}] Type: {type_}\n")
                f.write(f"SMS: {msg}\n")
                f.write("-" * 40 + "\n")
        print(f"\n✅ Messages saved to: {args.output}")
    
    print("\n" + "="*60)
    print("⚠️  DISCLAIMER: For educational purposes only")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()