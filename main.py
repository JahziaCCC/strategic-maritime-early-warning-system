from datetime import datetime

SYSTEM_NAME = "Strategic Maritime Early Warning System"

def main():
    print("=" * 50)
    print(SYSTEM_NAME)
    print("=" * 50)

    print("🌐 Maritime Strategic Monitoring")
    print()

    print("Monitoring Chokepoints:")
    print("✓ Strait of Hormuz")
    print("✓ Bab el Mandeb")
    print("✓ Suez Canal")
    print()

    print("System Status:")
    print("🟢 Initialized")

    print()
    print("Last Update:")
    print(datetime.now())


if __name__ == "__main__":
    main()
