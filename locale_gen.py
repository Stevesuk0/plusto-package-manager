import json

lang = {
    "lang": "en_US",
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
        "command_test": "Test stuck",
        
    }
}

with open("lang.json", "w") as f:
    f.write(json.dumps(lang, indent=4))
    f.close()
        
