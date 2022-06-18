from Payment import Payment
from HdfcBank import HdfcBank
from  CitiBank import CitiBank

payment = Payment()

# Process payment in HDFC bank file
payment.pay(HdfcBank(200, "87676656562"))

# Process refund in HDFC bank file
payment.refund(CitiBank(150, "6864365856526"))