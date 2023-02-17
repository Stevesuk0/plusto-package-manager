import sys, os, json, platform

del sys.argv[0] # delete launch filename from the arg list

configdir = ".config/plusto"

def launch():
    if not os.path.isdir(configdir):
        print("First using Plusto? I know, I know.")
        reset()
        
    
# --------------------------------
# bulit-in funtion

def license():
    print("""MIT License

Copyright (c) 2023 Stevesuk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")

def stdpt(type: str, text: str):
    if type == "err":
        infotyp = "!E!"
    elif type == "inf":
        infotyp = "[ ]"
    elif type == "inf_d":
        infotyp = "[√]"
    elif type == "warn":
        infotyp = "[!]"
    

    print(infotyp, text)



# --------------------------------
# program funtion

def about(): # show version
    print("Plusto Package Manager")
    print("\nA simple, easy-to-use software package manager") 
    print("v0.0.1 Alpha @Stevesuk")
    print("This program provide MIT License. Launch with --license arg to show it.")
    exit(0)
    


def helps(): # show help
    print("Plusto Package Manager")
    print("\nOptions:")
    print("\t-v/--version\tShuow plupm version and about.")
    print("\t   --test\tTest stuck")
    print("\t   --reset\tReset/Generate config, lang")
    exit(0)

def reset(): # generate config for ppm.

    

    configdir = ".config/plusto"

    os.makedirs(configdir + "/locale", exist_ok=True)
    os.makedirs(configdir + "/user", exist_ok=True)
    
    os.chdir(configdir)    

    os.chdir("user")

    # config
    config_template = {
        "version": "v0.0.1",
        "lang": "defualt",
        "repo_url": {
            "main": "https://mirrors.plusto.stevesuk-official.ml/" + platform.system().title() + "/" + platform.machine().lower(),
        }
    }

    lang = {
        "name": "English",
        "author": "Stevesuk",
        "email": "steveubuntu@outlook.com",
        "version": "v0.0.1",
        "content": {
            "text_process_start": "User's changes will be process",
            "text_process_success": "Complete!",
            "text_process_error": "Error at processing:",
            "text_main_main": "Plusto Package Manager",
            "text_main_options": "Options",
            "text_main_generate_complete": "We just generated the config, Please relaunch the plusto.",
            "text_version_comment": "A simple, easy-to-use software package manager",
            "text_test_test": "Plupkg stuck test",
            "text_exception_KeyboardInterrupt": "SIGINT Delected.",
            "text_set": "Set new value",
            "text_set_key": "key",
            "command_version": "Show plupm version and about.",
            "command_test": "Test stuck"
        }  
    }

    
    with open("config.json", "w", encoding="utf8") as f:
        f.write(json.dumps(config_template, indent=4))
        f.close()
    
    stdpt("inf", lang["content"]["text_set"] +" \"config-lang\" to \""+ config_template["lang"] +"\"")
    stdpt("inf", lang["content"]["text_set"] +" \"config-repo_url\" "+lang["content"]["text_set_key"]+" \"main\" to \""+ config_template["repo_url"]["main"] +"\"")

    os.chdir("../locale/")
    

    with open("defualt.json", "w", encoding="utf8") as f:
        f.write(json.dumps(lang, indent=4))
        f.close()

    


    stdpt("inf_d", lang["content"]["text_process_success"])

    print(lang["content"]["text_main_generate_complete"])
    

    os.chdir("../..")
    exit()



# ----------------------------------

def main():
    try:
        if sys.argv[0] in ("-v", "--version"): # match parameters, else exit with return 127
            about()
        elif sys.argv[0] in ("--test"):
            print("Plupkg stuck test demooooo")
            input()
        elif sys.argv[0] in ("--reset"):
            reset()
        elif sys.argv[0] in ("--license"):
            license()
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

launch()
main()


