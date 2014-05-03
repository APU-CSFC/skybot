'''
'''

from util import http, hook

@hook.command
def wechall(inp):
    ".wechall <username> -- poll user statistics."

    main_url = 'https://www.wechall.net/wechall.php?'
    cmds = inp.split(' ', 2)[1:]
    query_url = ''
    if (len(cmds) == 2):
        query_url = main_url+'username='+cmds[0]+' '+cmds[1]
    elif (len(cmds) == 1):
        query_url = main_url+'username='+cmds
    h = http.get_html(query_url)
    return h
