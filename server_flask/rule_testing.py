import re
def rule111_ip(url):
    # \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
    print 'rule01_ip function -> ' + url
    regex = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    matchObj = re.search(regex, url);
    print matchObj
    if matchObj:
        return 1
    else:
        return -1

def rule112_length(url):
    print 'rule02_length function -> ' + url

    if len(url) < 54:
      return -1
    elif len(url) >= 54 and len(url) <= 75:
      return 0
    else:
      return 1
      
def rule113_tinyurl(url):
    print 'rule03_tinyurl function -> ' + url
    regex = re.compile(r"(?:https?:\/\/)?(?:(?:0rz\.tw)|(?:1link\.in)|(?:1url\.com)|(?:2\.gp)|(?:2big\.at)|(?:2tu\.us)|(?:3\.ly)|(?:307\.to)|(?:4ms\.me)|(?:4sq\.com)|(?:4url\.cc)|(?:6url\.com)|(?:7\.ly)|(?:a\.gg)|(?:a\.nf)|(?:aa\.cx)|(?:abcurl\.net)|(?:ad\.vu)|(?:adf\.ly)|(?:adjix\.com)|(?:afx\.cc)|(?:all\.fuseurl.com)|(?:alturl\.com)|(?:amzn\.to)|(?:ar\.gy)|(?:arst\.ch)|(?:atu\.ca)|(?:azc\.cc)|(?:b23\.ru)|(?:b2l\.me)|(?:bacn\.me)|(?:bcool\.bz)|(?:binged\.it)|(?:bit\.ly)|(?:bizj\.us)|(?:bloat\.me)|(?:bravo\.ly)|(?:bsa\.ly)|(?:budurl\.com)|(?:canurl\.com)|(?:chilp\.it)|(?:chzb\.gr)|(?:cl\.lk)|(?:cl\.ly)|(?:clck\.ru)|(?:cli\.gs)|(?:cliccami\.info)|(?:clickthru\.ca)|(?:clop\.in)|(?:conta\.cc)|(?:cort\.as)|(?:cot\.ag)|(?:crks\.me)|(?:ctvr\.us)|(?:cutt\.us)|(?:dai\.ly)|(?:decenturl\.com)|(?:dfl8\.me)|(?:digbig\.com)|(?:digg\.com)|(?:disq\.us)|(?:dld\.bz)|(?:dlvr\.it)|(?:do\.my)|(?:doiop\.com)|(?:dopen\.us)|(?:easyuri\.com)|(?:easyurl\.net)|(?:eepurl\.com)|(?:eweri\.com)|(?:fa\.by)|(?:fav\.me)|(?:fb\.me)|(?:fbshare\.me)|(?:ff\.im)|(?:fff\.to)|(?:fire\.to)|(?:firsturl\.de)|(?:firsturl\.net)|(?:flic\.kr)|(?:flq\.us)|(?:fly2\.ws)|(?:fon\.gs)|(?:freak\.to)|(?:fuseurl\.com)|(?:fuzzy\.to)|(?:fwd4\.me)|(?:fwib\.net)|(?:g\.ro.lt)|(?:gizmo\.do)|(?:gl\.am)|(?:go\.9nl.com)|(?:go\.ign.com)|(?:go\.usa.gov)|(?:goo\.gl)|(?:goshrink\.com)|(?:gurl\.es)|(?:hex\.io)|(?:hiderefer\.com)|(?:hmm\.ph)|(?:href\.in)|(?:hsblinks\.com)|(?:htxt\.it)|(?:huff\.to)|(?:hulu\.com)|(?:hurl\.me)|(?:hurl\.ws)|(?:icanhaz\.com)|(?:idek\.net)|(?:ilix\.in)|(?:is\.gd)|(?:its\.my)|(?:ix\.lt)|(?:j\.mp)|(?:jijr\.com)|(?:kl\.am)|(?:klck\.me)|(?:korta\.nu)|(?:krunchd\.com)|(?:l9k\.net)|(?:lat\.ms)|(?:liip\.to)|(?:liltext\.com)|(?:linkbee\.com)|(?:linkbun\.ch)|(?:liurl\.cn)|(?:ln-s\.net)|(?:ln-s\.ru)|(?:lnk\.gd)|(?:lnk\.ms)|(?:lnkd\.in)|(?:lnkurl\.com)|(?:lru\.jp)|(?:lt\.tl)|(?:lurl\.no)|(?:macte\.ch)|(?:mash\.to)|(?:merky\.de)|(?:migre\.me)|(?:miniurl\.com)|(?:minurl\.fr)|(?:mke\.me)|(?:moby\.to)|(?:moourl\.com)|(?:mrte\.ch)|(?:myloc\.me)|(?:myurl\.in)|(?:n\.pr)|(?:nbc\.co)|(?:nblo\.gs)|(?:nn\.nf)|(?:not\.my)|(?:notlong\.com)|(?:nsfw\.in)|(?:nutshellurl\.com)|(?:nxy\.in)|(?:nyti\.ms)|(?:o-x\.fr)|(?:oc1\.us)|(?:om\.ly)|(?:omf\.gd)|(?:omoikane\.net)|(?:on\.cnn.com)|(?:on\.mktw.net)|(?:onforb\.es)|(?:orz\.se)|(?:ow\.ly)|(?:ping\.fm)|(?:pli\.gs)|(?:pnt\.me)|(?:politi\.co)|(?:post\.ly)|(?:pp\.gg)|(?:profile\.to)|(?:ptiturl\.com)|(?:pub\.vitrue.com)|(?:qlnk\.net)|(?:qte\.me)|(?:qu\.tc)|(?:qy\.fi)|(?:r\.im)|(?:rb6\.me)|(?:read\.bi)|(?:readthis\.ca)|(?:reallytinyurl\.com)|(?:redir\.ec)|(?:redirects\.ca)|(?:redirx\.com)|(?:retwt\.me)|(?:ri\.ms)|(?:rickroll\.it)|(?:riz\.gd)|(?:rt\.nu)|(?:ru\.ly)|(?:rubyurl\.com)|(?:rurl\.org)|(?:rww\.tw)|(?:s4c\.in)|(?:s7y\.us)|(?:safe\.mn)|(?:sameurl\.com)|(?:sdut\.us)|(?:shar\.es)|(?:shink\.de)|(?:shorl\.com)|(?:short\.ie)|(?:short\.to)|(?:shortlinks\.co.uk)|(?:shorturl\.com)|(?:shout\.to)|(?:show\.my)|(?:shrinkify\.com)|(?:shrinkr\.com)|(?:shrt\.fr)|(?:shrt\.st)|(?:shrten\.com)|(?:shrunkin\.com)|(?:simurl\.com)|(?:slate\.me)|(?:smallr\.com)|(?:smsh\.me)|(?:smurl\.name)|(?:sn\.im)|(?:snipr\.com)|(?:snipurl\.com)|(?:snurl\.com)|(?:sp2\.ro)|(?:spedr\.com)|(?:srnk\.net)|(?:srs\.li)|(?:starturl\.com)|(?:su\.pr)|(?:surl\.co.uk)|(?:surl\.hu)|(?:t\.cn)|(?:t\.co)|(?:t\.lh.com)|(?:ta\.gd)|(?:tbd\.ly)|(?:tcrn\.ch)|(?:tgr\.me)|(?:tgr\.ph)|(?:tighturl\.com)|(?:tiniuri\.com)|(?:tiny\.cc)|(?:tiny\.ly)|(?:tiny\.pl)|(?:tinylink\.in)|(?:tinyuri\.ca)|(?:tinyurl\.com)|(?:tl\.gd)|(?:tmi\.me)|(?:tnij\.org)|(?:tnw\.to)|(?:tny\.com)|(?:to\.ly)|(?:togoto\.us)|(?:totc\.us)|(?:toysr\.us)|(?:tpm\.ly)|(?:tr\.im)|(?:tra\.kz)|(?:trunc\.it)|(?:twhub\.com)|(?:twirl\.at)|(?:twitclicks\.com)|(?:twitterurl\.net)|(?:twitterurl\.org)|(?:twiturl\.de)|(?:twurl\.cc)|(?:twurl\.nl)|(?:u\.mavrev.com)|(?:u\.nu)|(?:u76\.org)|(?:ub0\.cc)|(?:ulu\.lu)|(?:updating\.me)|(?:ur1\.ca)|(?:url\.az)|(?:url\.co.uk)|(?:url\.ie)|(?:url360\.me)|(?:url4\.eu)|(?:urlborg\.com)|(?:urlbrief\.com)|(?:urlcover\.com)|(?:urlcut\.com)|(?:urlenco\.de)|(?:urli\.nl)|(?:urls\.im)|(?:urlshorteningservicefortwitter\.com)|(?:urlx\.ie)|(?:urlzen\.com)|(?:usat\.ly)|(?:use\.my)|(?:vb\.ly)|(?:vgn\.am)|(?:vl\.am)|(?:vm\.lc)|(?:w55\.de)|(?:wapo\.st)|(?:wapurl\.co.uk)|(?:wipi\.es)|(?:wp\.me)|(?:x\.vu)|(?:xr\.com)|(?:xrl\.in)|(?:xrl\.us)|(?:xurl\.es)|(?:xurl\.jp)|(?:y\.ahoo.it)|(?:yatuc\.com)|(?:ye\.pe)|(?:yep\.it)|(?:yfrog\.com)|(?:yhoo\.it)|(?:yiyd\.com)|(?:youtu\.be)|(?:yuarel\.com)|(?:z0p\.de)|(?:zi\.ma)|(?:zi\.mu)|(?:zipmyurl\.com)|(?:zud\.me)|(?:zurl\.ws)|(?:zz\.gd)|(?:zzang\.kr))\/[a-z0-9]*")

    matchObj = re.search(regex, url);
    print matchObj
    if matchObj:
        return 1
    else:
        return -1


def rule114_atsymbol(url):
    # \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
    print 'rule114_atsymbol function -> ' + url
    regex = re.compile(r"[@]")
    matchObj = re.search(regex, url);
    print matchObj
    if matchObj:
        return 1
    else:
        return -1

def rule115_doubleslash(url):
    # \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
    print 'rule115_doubleslash function -> ' + url
    regex = re.compile(r"[\/][\/]")
    matchObj = re.search(regex, url);
    print matchObj
    print matchObj.start()
    if matchObj.start() > 6:
        return 1
    else:
        return -1

def rule116_prefix(url):
    # \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
    print 'rule116_prefix function -> ' + url
    regex = re.compile(r"[-]")
    matchObj = re.search(regex, url);
    print matchObj

    if matchObj:
        return 1
    else:
        return -1


def rule117_subdomain(url):
    # \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
    print 'rule117_prefix function -> ' + url
    regex = re.compile(r"(\.ac/|\.ad/|\.ae/|\.af/|\.ag/|\.ai/|\.al/|\.am/|\.an/|\.ao/|\.aq/|\.ar/|\.as/|\.at/|\.au/|\.aw/|\.ax/|\.az/|\.ba/|\.bb/|\.bd/|\.be/|\.bf/|\.bg/|\.bh/|\.bi/|\.bj/|\.bl/|\.bm/|\.bn/|\.bo/|\.br/|\.bs/|\.bt/|\.bv/|\.bw/|\.by/|\.bz/|\.ca/|\.cc/|\.cd/|\.cf/|\.cg/|\.ch/|\.ci/|\.ck/|\.cl/|\.cm/|\.cn/|\.co/|\.cr/|\.cu/|\.cv/|\.cx/|\.cy/|\.cz/|\.de/|\.dj/|\.dk/|\.dm/|\.do/|\.dz/|\.ec/|\.ee/|\.eg/|\.eh/|\.er/|\.es/|\.et/|\.eu/|\.fi/|\.fj/|\.fk/|\.fm/|\.fo/|\.fr/|\.ga/|\.gb/|\.gd/|\.ge/|\.gf/|\.gg/|\.gh/|\.gi/|\.gl/|\.gm/|\.gn/|\.gp/|\.gq/|\.gr/|\.gs/|\.gt/|\.gu/|\.gw/|\.gy/|\.hk/|\.hm/|\.hn/|\.hr/|\.ht/|\.hu/|\.id/|\.ie/|\.il/|\.im/|\.in/|\.io/|\.iq/|\.ir/|\.is/|\.it/|\.je/|\.jm/|\.jo/|\.jp/|\.ke/|\.kg/|\.kh/|\.ki/|\.km/|\.kn/|\.kp/|\.kr/|\.kw/|\.ky/|\.kz/|\.la/|\.lb/|\.lc/|\.li/|\.lk/|\.lr/|\.ls/|\.lt/|\.lu/|\.lv/|\.ly/|\.ma/|\.mc/|\.md/|\.me/|\.mg/|\.mh/|\.mk/|\.ml/|\.mm/|\.mn/|\.mo/|\.mp/|\.mq/|\.mr/|\.ms/|\.mt/|\.mu/|\.mv/|\.mw/|\.mx/|\.my/|\.mz/|\.na/|\.nc/|\.ne/|\.nf/|\.ng/|\.ni/|\.nl/|\.no/|\.np/|\.nr/|\.nu/|\.nz/|\.om/|\.pa/|\.pe/|\.pf/|\.pg/|\.ph/|\.pk/|\.pl/|\.pm/|\.pn/|\.pr/|\.ps/|\.pt/|\.pw/|\.py/|\.qa/|\.re/|\.ro/|\.rs/|\.ru/|\.rw/|\.sa/|\.sb/|\.sc/|\.sd/|\.se/|\.sg/|\.sh/|\.si/|\.sj/|\.sk/|\.sl/|\.sm/|\.sn/|\.so/|\.sr/|\.st/|\.su/|\.sv/|\.sy/|\.sz/|\.tc/|\.td/|\.tf/|\.tg/|\.th/|\.tj/|\.tk/|\.tl/|\.tm/|\.tn/|\.to/|\.tp/|\.tr/|\.tt/|\.tv/|\.tw/|\.tz/|\.ua/|\.ug/|\.uk/|\.um/|\.us/|\.uy/|\.uz/|\.va/|\.vc/|\.ve/|\.vg/|\.vi/|\.vn/|\.vu/|\.wf/|\.ws/|\.ye/|\.yt/|\.yu/|\.za/|\.zm/|\.zw/|\.aero/|\.asia/|\.biz/|\.cat/|\.com/|\.coop/|\.edu/|\.gov/|\.info/|\.int/|\.jobs/|\.mil/|\.mobi/|\.museum/|\.name/|\.net/|\.org/|\.pro/|\.tel/|\.travel/)(.*)")
    matchObj = re.search(regex, url);
    print matchObj

    if matchObj:
        return 1
    else:
        return -1



#  http://88.204.202.98/2/paypal.ca/index.html
# url = '88.204.202.98'
url = 'http://88.204.202.98/2/paypal.ca/index.html'
print (rule111_ip(url))
print (rule112_length(url))

mylist = [1,2,3]
mylist.append(4)
print mylist

url2 = 'bit.ly/19DXSk4'
print (rule113_tinyurl(url2))

url3 = 'http://bit.l-y/19DX@Sk4'
print (rule114_atsymbol(url3))
print (rule115_doubleslash(url3))
print (rule116_prefix(url3))

url4 = 'http://hun.ac.uk'
print (rule117_prefix(url4))


