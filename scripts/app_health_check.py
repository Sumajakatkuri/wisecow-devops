import sys
import urllib.request
import urllib.error

url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8080"

print("===== APPLICATION HEALTH CHECK =====")
print("Checking:", url)

try:
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request, timeout=5) as response:
        print("Application Status: UP")
        print("HTTP Status Code:", response.status)
except Exception as error:
    print("Application Status: DOWN")
    print("Error:", error)
    sys.exit(1)

print("===== HEALTH CHECK COMPLETED =====")
