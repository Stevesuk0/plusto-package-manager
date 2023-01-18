from sys import argv, exit

# ----------------------------------

def about():
    print("Plusto Package Manager")
    print("\nA simple, easy-to-use software package manager") 
    print("v0.1 Alpha @Stevesuk")
    exit(0)
    

def helps():
    print("Plusto Package Manager")
    print("\nOptions:")
    print("\t-v/--version\tShow plupm version and about.")
    exit(0)

# ----------------------------------

def main():
    del argv[0]

    try:
        if argv[0] in ("v", "ver", "version", "--v", "-version", "-v", "--version"):
            if argv[0] in ("-v", "--version"):
                about()
            else:
                if input("Unknown command, are you want to still execute [-v/--version] (y/N(n))? ") == "y":
                    about()
                else:
                    exit(127)

    except IndexError:
        helps()
    except KeyboardInterrupt:
        print("SIGINT Delected.")
        exit(127)

# ----------------------------------


main()


