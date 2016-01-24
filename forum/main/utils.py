import re

def bbcode(content):
    bold_open = re.compile(r'\[b:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = bold_open.sub(r'<b>', content)
    bold_close = re.compile(r'\[\/b:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = bold_close.sub(r'</b>', content)
    
    italic_open = re.compile(r'\[i:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = italic_open.sub(r'<i>', content)
    italic_close = re.compile(r'\[\/i:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = italic_close.sub(r'</i>', content)
    
    underline_open = re.compile(r'\[u:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = underline_open.sub(r'<u>', content)
    underline_close = re.compile(r'\[\/u:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = underline_close.sub(r'</u>', content)
    
    size_open = re.compile(r'\[size=([0-9]+):([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = size_open.sub(r'<span style="font-size:\1px;">', content)
    size_close = re.compile(r'\[\/size:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = size_close.sub(r'</span>', content)
    
    color_open = re.compile(r'\[color=([a-zA-Z]+):([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = color_open.sub(r'<span style="color:\1;">', content)
    color_close = re.compile(r'\[\/color:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = color_close.sub(r'</span>', content)
    
    quote_open = re.compile(r'\[quote:([a-zA-Z0-9]+)=\"([a-zA-Z0-9-._ ]+)\"\]', re.IGNORECASE)
    content = quote_open.sub(r'<blockquote><div class="quote-name">\2</div>', content)
    quote_open = re.compile(r'\[quote:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = quote_open.sub(r'<blockquote>', content)
    quote_close = re.compile(r'\[\/quote:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = quote_close.sub(r'</blockquote>', content)
    
    youtube = re.compile(r'\[youtube\]http://(.+)youtube.com/watch\?v=([0-9A-Za-z-_]{11})(.*?)\[/youtube\]', re.IGNORECASE)
    content = youtube.sub(r'<iframe src="https://www.youtube.com/embed/\2" frameborder="0" allowfullscreen></iframe>', content)
    
    img = re.compile(r'\[img:([a-zA-Z0-9]+)\](.*?)\[\/img:([a-zA-Z0-9]+)\]', re.IGNORECASE)
    content = img.sub(r'<img src="\2" alt="">', content)
    
    url = re.compile(r'todoslosforos', re.IGNORECASE)
    content = url.sub(r'topicazo', content)
    
    #link = re.compile(r"(http://[^ ]+)")
    #content = link.sub(r'<a href="\1" rel="nofollow" target="_blank">\1</a>', content)
    
    url_open = re.compile(r'\[url=(.*?)\](.*?)\[\/url\]', re.IGNORECASE)
    content = url_open.sub(r'<a href="\1" rel="nofollow" target="_blank">\2</a>', content)
    
    return content

def emojis(content):
    smilies = [
        [1,":D","grinning.png","Very Happy"],
        [2,":-D","grinning.png","Very Happy"],
        [3,":grin:","grinning.png","Very Happy"],
        [4,":)","grinning.png","Smile"],
        [5,":-)","grinning.png","Smile"],
        [6,":smile:","grinning.png","Smile"],
        [7,":(","icon_sad.gif","Sad"],
        [8,":-(","icon_sad.gif","Sad"],
        [9,":sad:","icon_sad.gif","Sad"],
        [10,":o","open_mouth.png","Surprised"],
        [11,":-o","open_mouth.png","Surprised"],
        [12,":eek:","icon_surprised.gif","Surprised"],
        [13,":shock:","flushed.png","Shocked"],
        [14,":?","confused.png","Confused"],
        [15,":-?","confused.png","Confused"],
        [16,":???:","confused.png","Confused"],
        [17,"8)","sunglasses.png","Cool"],
        [18,"8-)","sunglasses.png","Cool"],
        [19,":cool:","sunglasses.png","Cool"],
        [20,":lol:","satisfied.png","Laughing"],
        [21,":x","icon_mad.gif","Mad"],
        [22,":-x","icon_mad.gif","Mad"],
        [23,":mad:","icon_mad.gif","Mad"],
        [24,":P","stuck_out_tongue.png","Razz"],
        [25,":-P","stuck_out_tongue.png","Razz"],
        [26,":razz:","stuck_out_tongue.png","Razz"],
        [27,":oops:","icon_redface.gif","Embarassed"],
        [28,":cry:","cry.png","Cry"],
        [29,":evil:","imp.png","Evil"],
        [30,":twisted:","imp.png","Twisted Evil"],
        [31,":roll:","relieved.png","Relieved"],
        [32,":wink:","wink.png","Wink"],
        [33,";)","wink.png","Wink"],
        [34,";-)","wink.png","Wink"],
        [35,":!:","exclamation.png","Exclamation"],
        [36,":?:","question.png","Question"],
        [37,":idea:","icon_idea.gif","Idea"],
        [38,":arrow:","icon_arrow.gif","Arrow"],
        [39,":|","icon_neutral.gif","Neutral"],
        [40,":-|","icon_neutral.gif","Neutral"],
        [41,":neutral:","icon_neutral.gif","Neutral"],
        [42,":mrgreen:","grin.png","Mr. Green"],
        [43,":-#","no_mouth.png","Silenced"],
        [44,":-s","eusa_eh.gif","Eh?"],
        [45,":aiwebs_001:","aiwebs_001.gif","aiwebs_001"],
        [46,":aiwebs_002:","aiwebs_002.gif","aiwebs_002"],
        [47,":aiwebs_003:","disappointed.png","Disappointed"],
        [48,":aiwebs_004:","blush.png","Blush"],
        [49,":aiwebs_005:","aiwebs_005.gif","aiwebs_005"],
        [50,":aiwebs_006:","aiwebs_006.gif","aiwebs_006"],
        [51,":aiwebs_007:","aiwebs_007.gif","aiwebs_007"],
        [52,":aiwebs_008:","aiwebs_008.gif","aiwebs_008"],
        [53,":aiwebs_009:","aiwebs_009.gif","aiwebs_009"],
        [54,":aiwebs_010:","flushed.png","Flushed"],
        [55,":aiwebs_011:","grin.png","Grin"],
        [56,":aiwebs_012:","aiwebs_012.gif","aiwebs_012"],
        [57,":aiwebs_014:","relieved.png","Relieved"],
        [58,":aiwebs_015:","aiwebs_015.gif","aiwebs_015"],
        [59,":aiwebs_016:","anguished.png","Anguished"],
        [60,":aiwebs_017:","smile.png","Smile"],
        [61,":aiwebs_018:","triumph.png","Triumph"],
        [62,":aiwebs_019:","aiwebs_019.gif","aiwebs_019"],
        [63,":aiwebs_020:","aiwebs_020.gif","aiwebs_020"],
        [64,":aiwebs_021:","aiwebs_021.gif","aiwebs_021"],
        [65,":aiwebs_022:","relaxed.png","Relaxed"],
        [66,":aiwebs_023:","aiwebs_023.gif","aiwebs_023"],
        [67,":aiwebs_024:","aiwebs_024.gif","aiwebs_024"],
        [68,":aiwebs_025:","aiwebs_025.gif","aiwebs_025"],
        [69,":aiwebs_026:","aiwebs_026.gif","aiwebs_026"],
        [70,":aiwebs_027:","aiwebs_027.gif","aiwebs_027"],
        [71,":aiwebs_028:","laughing.png","Laughing"],
        [72,":aiwebs_029:","confounded.png","Confounded"],
        [73,":aiwebs_030:","aiwebs_030.gif","aiwebs_030"],
        [74,":aiwebs_033:","innocent.png","Innocent.png"]
    ]
    
    for pack in smilies:
        img_url = '<img src="/static/img/emojis/%s" class="emoji" alt="%s">' % (pack[2], pack[3])
        content = content.replace(pack[1], img_url)
    
    return content