URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = []
for url in URLs:
    dominio = url[4:-4]
    dominios.append(dominio)

print(f"domínios:{dominios}")

