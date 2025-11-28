import requests, time

def xrp_omen():
    print("Ripple XRP — An Omen Just Flashed Across the Ledger")
    seen = set()
    while True:
        r = requests.get("https://data.ripple.com/v2/transactions?limit=50&descending=true")
        for tx in r.json().get("transactions", []):
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Catch exact 999,999 XRP transfer — legendary omen amount
            if tx.get("TransactionType") != "Payment": continue
            amount = tx["Amount"]
            if isinstance(amount, dict): continue  # skip issued currency
            if amount != "999999000000": continue  # exactly 999999 XRP

            src = tx["Account"][:12]
            dst = tx["Destination"][:12]
            print(f"THE OMEN HAS SPOKEN\n"
                  f"Exactly 999,999 XRP just crossed the ledger\n"
                  f"From: {src}...\n"
                  f"To:   {dst}...\n"
                  f"Ledger: {tx['ledger_index']}\n"
                  f"https://livenet.xrpl.org/transactions/{h}\n"
                  f"→ This number is never random\n"
                  f"→ Every time this happens, something breaks or moons\n"
                  f"→ The ledger itself just blinked\n"
                  f"{'◉̅'*60}\n")
        time.sleep(2.4)

if __name__ == "__main__":
    xrp_omen()
