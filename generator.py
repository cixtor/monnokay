#!/usr/bin/env python
import sys, json
from collections import OrderedDict

if len(sys.argv) < 2:
    print("Usage: generator.py [syntax.json]")
    sys.exit(1)

with open(sys.argv[1]) as resource:
    data = json.load(resource, object_pairs_hook=OrderedDict)
    required = [
        'theme',
        'author_name',
        'description',
        'author_link',
        'project_link',
        'options',
        'settings',
    ]

    for name in required:
        if name not in data:
            print("Missing JSON property: " + name)
            sys.exit(1)

    print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    print("<!DOCTYPE plist PUBLIC \"-//Apple Computer//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">")

    print("<!-- author: %s -->" % data['author_name'])
    print("<!-- project: %s -->" % data['description'])
    print("<!-- link: %s -->" % data['author_link'])
    print("<!-- code: %s -->" % data['project_link'])
    print("<!-- see: Scope Naming - Sublime Text 3 Documentation -->")
    print("<!-- see: http://www.sublimetext.com/docs/3/scope_naming.html -->")

    print("<plist version=\"1.0\">")
    print("<dict>")
    print("\t<key>name</key>")
    print("\t<string>%s</string>" % data['theme'])
    print("\t<key>settings</key>")
    print("\t<array>")

    print("\t\t<dict>")
    print("\t\t\t<key>settings</key>")
    print("\t\t\t<dict>")
    for key, value in data['options'].iteritems():
        print("\t\t\t\t<key>%s</key>" % key)
        print("\t\t\t\t<string>%s</string>" % value)
    print("\t\t\t</dict>")
    print("\t\t</dict>")

    for option in data['settings']:
        if "scope" not in option: continue
        hasSettings = False
        print("\t\t<dict>")
        if "name" in option and option['name'] != "":
            print("\t\t\t<key>name</key>")
            print("\t\t\t<string>%s</string>" % option['name'])
        if "scope" in option:
            print("\t\t\t<key>scope</key>")
            print("\t\t\t<string>%s</string>" % option['scope'])
        if "background" in option and option['background'] != "": hasSettings = True
        if "foreground" in option and option['foreground'] != "": hasSettings = True
        if "fontStyle"  in option and option['fontStyle']  != "": hasSettings = True
        if hasSettings:
            print("\t\t\t<key>settings</key>")
            print("\t\t\t<dict>")
            if "background" in option and option['background'] != "":
                print("\t\t\t\t<key>background</key>")
                print("\t\t\t\t<string>%s</string>" % option['background'])
            if "foreground" in option and option['foreground'] != "":
                print("\t\t\t\t<key>foreground</key>")
                print("\t\t\t\t<string>%s</string>" % option['foreground'])
            if "fontStyle"  in option and option['fontStyle']  != "":
                print("\t\t\t\t<key>fontStyle</key>")
                print("\t\t\t\t<string>%s</string>" % option['fontStyle'])
            print("\t\t\t</dict>")
        print("\t\t</dict>")

    print("\t</array>")
    print("\t<key>colorSpaceName</key>")
    print("\t<string>sRGB</string>")
    print("</dict>")
    print("</plist>")

    sys.exit(0)
