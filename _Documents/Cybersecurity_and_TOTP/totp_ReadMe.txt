Stefan Ene, CS370 Assignment 3: TOTP

This is a guide to how to run the totp.py file to correctly generate a QR code for the Google Authenticator app (as tested on IOS) and generate one-time passwords every 30 seconds.

How to run? Make sure you perform the following terminal command:
    $ python3 totp.py [flag]
    
Where [flag] can be "--generate-qr [user_id]" or "--get-otp". The [user_id] is the gmail address used for the GA app required only if running with the "--generate-qr" flag.


NOTE: This implementation uses the Segno library for generating QR codes and the TQDM library for progress/loading bars; these libaraies have to be installed first like so:
    $ pip install segno tqdm

NOTE2: When running with the [--get-otp] flag, the program will forever loop and generate a new OTP every 30 seconds, so to exit this running program the user needs to use a keyboard interrupt (CTRL+C or close terminal).