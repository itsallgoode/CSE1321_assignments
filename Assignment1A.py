print("[Let's make a website (URL)!]")

scheme = input("Scheme: ")
subdomain = input("Subdomain: ")
second_level_domain = input("Second-level domain: ")
top_level_domain = input("Top-level domain: ")
subdirectory = input("Subdirectory: ")
print("Your URL is:")
print(scheme + "://" + subdomain + "." + second_level_domain + "." + top_level_domain + "/" + subdirectory)
