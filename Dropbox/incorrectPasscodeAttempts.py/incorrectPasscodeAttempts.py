# Opening the Dropbox mobile app on the VIU's tablet requires a four-digit passcode.
# To ensure the confidentiality of the stored information, the device is locked out of Dropbox
# after 10 consecutive failed passcode attempts.
# We need to implement a function that given an array of attempts made throughout
# the day and the correct passcode checks to see if the device should be locked, i.e.
# 10 or more consecutive failed passcode attempts were made.


def incorrectPasscodeAttempts(passcode, attempts):
    count_wrong_attempt = 0
    for attempt in attempts:
        if attempt == passcode:
            count_wrong_attempt = 0
        else:
            count_wrong_attempt += 1
            if count_wrong_attempt == 10:
                return True
    return False
