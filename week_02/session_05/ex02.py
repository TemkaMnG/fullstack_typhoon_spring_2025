import sys
import io
print("Алдааны мессеж", file=sys.stderr)

# Standart garalt (stdout)
sys.stdout.write("Ene bol standart garalt\n")

# Standart aldaa (stderr)
sys.stderr.write("Ene bol aldaanii message\n")

# Standart orolt (stdin)
print("Ymar negen zvil bicheed Enter darna uu:")
user_input = sys.stdin.readline().strip()
print(f"Ta bichsen: {user_input}")

# stdout-g tvr chigluuleh
original_stdout = sys.stdout
string_io = io.StringIO()
sys.stdout = string_io

print("ene barigdsan")
print("ene ch bas")

sys.stdout = original_stdout
capture_output = string_io.getvalue()
print(f"Barigdsan: {capture_output}")
