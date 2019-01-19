
# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

def fun(s):
    try:
        uname, url = s.split("@")
        web, ext = url.split(".")
    except ValueError:
        return False
    
    if not uname.replace("-", "").replace("_", "").isalnum():
        return False
    if not web.isalnum():
        return False
    if len(ext) > 3:
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
