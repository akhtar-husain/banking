import Payment
from HdfcBank import HdfcBank
from  CitiBank import CitiBank

# Process payment in HDFC bank file
Payment.pay(HdfcBank(200, "87676656562"))

# Process refund in CITI bank file
Payment.refund(CitiBank(150, "6864365856526"))