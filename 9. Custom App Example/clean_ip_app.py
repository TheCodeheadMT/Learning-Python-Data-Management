import sys
from clean_ip import CleanIP

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_ip_app.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]
    app = CleanIP(filepath)
    app.process_file()
