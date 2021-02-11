import requests
import sys
import validators

def check_url(url): 
    check = validators.url(url)
    if check == True:
        return(True)    
    else:
        return(False)

def path_list():
    list_path = []
    fresh_list = []
    with open("path_login.txt") as file_path:
        list_path = file_path.readlines()
    for i in list_path:
        fresh_list.append(i[:-1])
    return fresh_list  

def check_content(content):
    check_list = [
        "username",
        "password",
        "Username",
        "Password",  
        "email",
        "mail",
        "number",
        "ID",
        "user",
        "pass",

    ]
    for c in check_list:
        if c.upper() in content or c.lower() in content or c in content:
            return(True) 

def about():
    banner = """
    ++++++++++++++++++++++++++++++++++++
    
    #   Coded By PentestoR

    #   version -----> 0.1

    #   Contact -----> t.me/nulllbyte 
    
    #   Channel -----> t.me/PrivateProgramming  

    ++++++++++++++++++++++++++++++++++++
    
    """
    print(banner)

def help():
    banner = """
    ========================================
    
    Usage :
    python admin-finder.py https://target.com

    ========================================
    """
    print(banner)

if __name__ == "__main__":
    checked_list = []
    try:
        var = sys.argv[1]
        if "-h" in var or "--help" in var:
            help()
        elif check_url(var) == True:
            list_path = path_list()
            for l in list_path:
                # Merge root site to path
                url = var +"/"+l 
                try:
                    r = requests.get(url=url)
                    status_code = r.status_code
                    print(f"[*] {url} : {status_code}")
                    if (status_code == 200 or status_code == 302 or status_code == 403 or status_code == 401) and (check_content(str(r.content)) == True):
                        checked_list.append(url)
                except requests.exceptions.ConnectionError:
                    print("[!] ERROR IN CONNECTION URL....")
            count = len(checked_list)
            print(f"[~~] {count} Results Detected")
            n = 0
            if count > 0:
                for t in checked_list:
                    n+=1
                    print(f"{n} ---> {t}")                
        elif check_url(var) == False:
            print("[#] Invalid Url! Please check Url.")

    except IndexError:
        about()
        help()        