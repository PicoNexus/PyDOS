from pye_pydos import pye

if __name__ != "PyDOS":
    passedIn = ""

if passedIn == "":
    passedIn = input("Enter filename:")

ret = pye(passedIn)
