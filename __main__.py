import ltmddos
import sys

if __name__ == "__main__":
    try:
        ltmddos.main_interactivo()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Saliendo...\033[0m")
        sys.exit()
