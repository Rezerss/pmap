import socket
import requests

target = input("Enter the target domain or IP address: ")

try:
    ip = socket.gethostbyname(target)
    print(f"Target IP: {ip}")

except socket.gaierror:
    print("Invalid target!")
    exit()


def port_scanner(ip):

    important_ports = [
        20,
        21,
        22,
        23,
        25,
        53,
        67,
        68,
        69,
        80,
        110,
        111,
        119,
        123,
        135,
        137,
        138,
        139,
        143,
        161,
        389,
        443,
        445,
        465,
        587,
        636,
        993,
        1433,
        1521,
        2049,
        2375,
        2376,
        3000,
        3306,
        3389,
        5000,
        5432,
        6379,
        6443,
        8000,
        8080,
        8443,
        8888,
        9000,
        9090,
        9200,
        27017
    ]

    open_ports = []
    closed_ports = []

    print("\n=== PORT SCANNER ===")

    for port in important_ports:

        sock = socket.socket()
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[OPEN] port {port}")
            open_ports.append(port)

        else:
            print(f"[CLOSED] port {port}")
            closed_ports.append(port)

        sock.close()

    print("\n=== PORT SCAN RESULT ===")
    print(f"Open ports: {open_ports}")
    print(f"Closed ports: {closed_ports}")

def subfinder(domain):

    subdomains = [
        "www",
        "mail",
        "api",
        "app",
        "admin",
        "portal",
        "login",
        "auth",
        "account",
        "accounts",
        "dev",
        "development",
        "test",
        "testing",
        "stage",
        "staging",
        "beta",
        "demo",
        "blog",
        "shop",
        "store",
        "support",
        "help",
        "docs",
        "status",
        "cdn",
        "static",
        "assets",
        "media",
        "img",
        "images",
        "vpn",
        "remote",
        "git",
        "gitlab",
        "github",
        "jenkins",
        "db",
        "database",
        "mysql",
        "postgres",
        "redis",
        "monitor",
        "monitoring",
        "grafana",
        "prometheus",
        "internal",
        "intranet",
        "devops",
        "dashboard",
        "server"
    ]

    print("\n=== SUBDOMAIN SCANNER ===")

    found_subdomains = []

    for subdomain in subdomains:

        full_domain = subdomain + "." + domain

        try:
            sub_ip = socket.gethostbyname(full_domain)

            print(f"[FOUND] {full_domain} -> {sub_ip}")

            found_subdomains.append(full_domain)

        except socket.gaierror:
            pass

    print("\n=== SUBDOMAIN RESULT ===")
    print(f"Found: {found_subdomains}")

def web_recon(domain):

    print("\n=== WEB RECON ===")

    url = "https://" + domain

    try:
        response = requests.get(
            url,
            timeout=5
        )

        print(f"Status: {response.status_code}")
        print(f"Final URL: {response.url}")
        print(f"Server: {response.headers.get('Server')}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")

    except requests.RequestException:

        print("HTTPS unavailable")

        url = "http://" + domain

        try:
            response = requests.get(
                url,
                timeout=5
            )

            print(f"Status: {response.status_code}")
            print(f"Final URL: {response.url}")
            print(f"Server: {response.headers.get('Server')}")
            print(f"Content-Type: {response.headers.get('Content-Type')}")

        except requests.RequestException:

            print("HTTP unavailable")


print("\n==============================")
print("        PMAP RECON")
print("==============================")

port_scanner(ip)

subfinder(target)

web_recon(target)

print("\n==============================")
print("        SCAN COMPLETE")
print("==============================")