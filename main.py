import sys, os, json, platform

del sys.argv[0] # delete filename from the arg list
configdir = ".config/plusto"

# --------------------------------

def about():
    print("Plusto Package Manager")
    print("\nA simple, easy-to-use software package manager") 
    print("v0.0.1 Alpha @Stevesuk")
    exit(0)
    

def helps():
    print("Plusto Package Manager")
    print("\nOptions:")
    print("\t-v/--version\tShuow plupm version and about.")
    print("\t   --test\tTest stuck")
    exit(0)

def generate(): # generate the defualt config for ppm.
    os.makedirs(configdir + "/locale", exist_ok=True)
    os.makedirs(configdir + "/user", exist_ok=True)
    
    os.chdir(configdir)    

    os.chdir("user")

    # config
    config_template = {
        "version": "v0.0.1",
        "lang": "defualt",
        "repo_url": {
            "main": "https://mirrors.plusto.stevesuk-official.ml/" + platform.system().lower() + "/" + platform.machine().lower(),
        }
    }
    
    with open("config.json", "w", encoding="utf8") as f:
        f.write(json.dumps(config_template, indent=4))
        f.close()
    
    # lang
    lang_template = {
        "name": "English",
        "author": "Stevesuk",
        "email": "steveubuntu@outlook.com",
        "version": "v0.0.1",
        "content": {
            "text_main_main": "Plusto Package Manager",
            "text_main_options": "Options",
            "text_version_comment": "A simple, easy-to-use software package manager",
            "text_test_test": "Plupkg stuck test",
            "text_exception_KeyboardInterrupt": "SIGINT Delected.",
            "command_version": "Show plupm version and about.",
            "command_test": "Test stuck"
        }
    }
    
    os.chdir("../locale/")
    

    with open("defualt.json", "w", encoding="utf8") as f:
        f.write(json.dumps(lang_template))
        f.close()

    os.chdir("../..")



# ----------------------------------

def main():
    try:
        if sys.argv[0] in ("-v", "--version"): # match parameters, else exit with return 127
            about()
        elif sys.argv[0] in ("--test"):
            print("Plupkg stuck test demooooo")
            input()
        elif sys.argv[0] in ("-g", "--generate"):
            generate()
        else:
            exit(127)    

    except IndexError:
        helps()
    except KeyboardInterrupt:
        print("SIGINT Delected.")
        exit(127)
    finally:
        exit(0)

        
##########################

main()


