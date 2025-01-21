import os
from dotenv import load_dotenv
import sys
from datetime import datetime
from typing import Optional


# [*] Default Environment Variables:
# PWD=/tmp/msmowz/20241121173033774104/001
# OLDPWD=/var/task
# LC_CTYPE=C.UTF-8

# [*] Creator Defined Environment Variables:
# SOMETHING=value

def main() -> None:
    # Load environment variables from .env file
    load_dotenv()

    # Access and validate environment variables
    try:
        secret_key = os.environ['SECRET_KEY']
        database_url = os.environ['DATABASE_URL']
        api_key = os.environ['API_KEY']
    except KeyError as e:
        print(f"Error: Required environment variable {e} is not set", file=sys.stderr)
        sys.exit(1)

    # Handle debug flag with proper boolean conversion
    debug = os.getenv('DEBUG', 'false').lower() in ('true', '1', 'yes')

    # Print the values
    print(f"Secret Key: {secret_key}")
    print(f"Database URL: {database_url}")
    print(f"API Key: {api_key}")
    print(f"Debug Mode: {debug}")

    # Echo command line arguments if any exist
    if len(sys.argv) > 1:
        print("\n[*] Command line arguments:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"[*] Argument {i}: {arg}")
        print()  # Empty line for better formatting
    
    # Write to stdout (standard output)
    print("[*] This is a normal message going to stdout")
    print(f"[*] Current time is: {datetime.now()}")
    
    # Write to stderr (standard error)
    print("[*] This is an error message going to stderr", file=sys.stderr)
    print("[*] Another error occurred!", file=sys.stderr)
    
    # You can also use sys.stdout and sys.stderr directly
    sys.stdout.write("[*] Direct write to stdout\n")
    sys.stderr.write("[*] Direct write to stderr\n")
    
    # Print environment variables
    print("\n[*] Environment Variables:")
    for key, value in os.environ.items():
        print(f"[*] {key}={value}")
    
    # ... existing code ...

if __name__ == "__main__":
    main()