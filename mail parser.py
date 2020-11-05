
class AccountsParser():

    def __init__(self, filename="accounts to parse.txt"):
        self.filename = filename
        self.accounts = []


    def read_file(self):
        with open(self.filename, mode="r+") as myfile:
            self.accounts = myfile.read().split("\n")
        

    def mail_sort(self):
        for account in self.accounts:
            # split between email and password
            onlymail = account.split(":")[0]
            # split between the name and domainname
            domainmail = onlymail.split("@")[1]
            domainmail = domainmail.split(".")[0]
            with open(".\\parsed accounts\\{}.txt".format(domainmail), mode="a") as myfile:
                myfile.write(account+"\n")


def main():
    acparser = AccountsParser()
    acparser.read_file()
    acparser.mail_sort()


if __name__ == "__main__":
    import time 
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")