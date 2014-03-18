# sublime-enlister

Enlister is a plugin that can launch project specific tools. Typically, this is used to launch build environments that vary depending on the project. The plugin looks for the project setting `enlister` which is an array of objects that have three properties:
* name - The display name in the command palette
* command - The command to launch. This is passed directly to `subprocess`. It can be an array of strings if arguments need to be split out.
* working_dir - The working directory.

See `enlister.sublime-project` for samples, or look below.

## Samples

    {
        "enlister": [
            {
                "name": "terminal",
                "command": "gnome-terminal",
                "working_dir": "/home/kael/Documents/code"
            },{
                "name": "python",
                "command": "gnome-terminal --tab --maximize --command python",
                "working_dir": "/home/kael/Documents/code"
            },{
                "name": "windows",
                "command": "c:\\Windows\\System32\\cmd.exe /k \"d:\\env\\project1\\start.cmd\"",
                "working_dir": "d:\\env\\project1"
            },{
                "name": "conemu",
                "command": "c:\\Windows\\System32\\cmd.exe /k \"d:\\Tools\\ConEmu\\ConEmu\\ConEmuC64.exe /ATTACH /NOCMD & d:\\env\\project1\\start.cmd\"",
                "working_dir": "d:\\env\\project1"
            }
        ]
    }
