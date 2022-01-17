# whatsonchain
A short python script to check your wallet balance.  I added a couple from Moneybutton, Volt.Id and HandCash.  Moneybutton and HandCash use rolling addresses.  When running whatsonchain_balance.py you will receieve a zero balance for HandCash and Moneybutton. 

WhatsOnChain has a rate limit of 3 requests/second. Line 15 is a loop to keep checking the wallet balance. This can be useful while you send and receive money to the wallet address. 

https://developers.whatsonchain.com/#rate-limits
https://developers.whatsonchain.com/#get-balance
