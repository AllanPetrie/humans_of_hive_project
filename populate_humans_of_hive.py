import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humans_of_hive_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from humans_of_hive.models import Post, Comment, UserProfile

def populate():
    #Create comments for each post
    i_hate_hive_comments = [
        {"owner": "TestUser2", "content": "Fully begin on by wound an"},
        {"owner": "TestUser3", "content": "Old unsatiable our now but considered travelling impression"},
        {"owner": "TestUser4", "content": "My entrance me is disposal bachelor remember relation"},
        {"owner": "TestUser5", "content": " Loud in this in both hold"},
        {"owner": "TestUser2", "content": "Man its upon him call mile"},
    ]
    i_love_hive_comments = [
        {"owner": "TestUser5", "content": " "},
        {"owner": "TestUser1", "content": "don't care"},
        {"owner": "TestUser2", "content": "first"},
        {"owner": "TestUser3", "content": "Outward clothes promise at gravity do excited"},
    ]
    i_love_me_comments = [
        {"owner": "TestUser1", "content": "Is education residence conveying so so. Suppose shyness say ten behaved morning had"},
        {"owner": "TestUser5", "content": "Additions in conveying or collected objection in"},
        {"owner": "TestUser3", "content": "High at of in loud rich true"},
        {"owner": "TestUser1", "content": "Ye to misery wisdom plenty polite to as"},
        {"owner": "TestUser4", "content": "Delightful remarkably mr on announcing themselves entreaties favourable"},
        {"owner": "TestUser2", "content": "By spite about do of do allow blush"},
    ]
    hello_comments = [
        {"owner": "TestUser4", "content": "What it is what is up"},
        {"owner": "TestUser2", "content": "Supported me sweetness behaviour shameless excellent so arranging"},
        {"owner": "TestUser3", "content": "An household behaviour if pretended"},
    ]
    me_myself_and_i_comments = [
        {"owner": "TestUser10", "content": "Doubtful two bed way pleasure confined followed"},
        {"owner": "TestUser15", "content": "On am we offices expense thought"},
        {"owner": "TestUser3", "content": "Its hence ten smile age means"},
        {"owner": "TestUser11", "content": "Seven chief sight far point any"},
        {"owner": "TestUser4", "content": "Of so high into easy"},
        {"owner": "TestUser2", "content": "Dashwoods eagerness oh extensive as discourse sportsman frankness"},
    ]
    crazy_comments = [
        {"owner": "TestUser10", "content": "Husbands see disposed surprise likewise humoured yet pleasure"},
        {"owner": "TestUser9", "content": "Fifteen no inquiry cordial so resolve garrets as"},
        {"owner": "TestUser3", "content": "Impression was estimating surrounded solicitude indulgence son shy"},
        {"owner": "TestUser19", "content": "Do to be agreeable conveying oh assurance"},
        {"owner": "TestUser14", "content": "Wicket longer admire do barton vanity itself do in it"},
        {"owner": "TestUser2", "content": "Preferred to sportsmen it engrossed listening"},
        {"owner": "TestUser15", "content": "Park gate sell they west hard for the"}
    ]
    party_late_comments = [
        {"owner": "TestUser14", "content": "Abode stuff noisy manor blush yet the far"},
        {"owner": "TestUser12", "content": "Up colonel so between removed so do"},
        {"owner": "TestUser13", "content": "Years use place decay sex worth drift age"},
    ]
    table_name_comments = [
        {"owner": "TestUser4", "content": "Men lasting out end article express fortune demands own charmed"},
        {"owner": "TestUser16", "content": "About are are money ask how seven"},
    ]
    i_was_barely_involved_comments = [
        {"owner": "TestUser13", "content": "Terminated principles sentiments of no pianoforte if projection impossible"},
    ]
    golden_jesus_comments = [
        {"owner": "TestUser12", "content": "Sy"}
    ]
    padme_comments = [
        {"owner": "TestUser11", "content": " "},
        {"owner": "TestUser1", "content": "don't care"},
        {"owner": "TestUser10", "content": "first"},
        {"owner": "TestUser14", "content": "Outward clothes promise at gravity do excited"},
    ]
    darth_wader_lives_comments = [
        {"owner": "TestUser18", "content": "Horses pulled nature favour number yet highly his has old"},
        {"owner": "TestUser1", "content": "don't care"},
        {"owner": "TestUser2", "content": "Contrasted literature excellence he admiration impression insipidity so"},
        {"owner": "TestUser5", "content": "Scale ought who terms after own quick since"},
    ]
    dark_side_comments = [
        {"owner": "TestUser8", "content": "Servants margaret husbands to screened in throwing"},
        {"owner": "TestUser5", "content": "Imprudence oh an collecting partiality"},
        {"owner": "TestUser13", "content": "Admiration gay difficulty unaffected how"},
        {"owner": "TestUser10", "content": "Travelling alteration impression six all uncommonly"},
        {"owner": "TestUser9", "content": "Chamber hearing inhabit joy highest private ask him our believe"},
        {"owner": "TestUser2", "content": "Up nature valley do warmly"},
    ]
    wrong_it_s_a_list_comments = [
        {"owner": "TestUser13", "content": "count olaf"},
        {"owner": "TestUser10", "content": "here first"}
    ]
    mellon_comments = [
        {"owner": "TestUser5", "content": "Entered of cordial do on no hearted"},
        {"owner": "TestUser1", "content": "Yet agreed whence and unable limits"},
        {"owner": "TestUser20", "content": "Use off him gay abilities concluded immediate allowance"},
        {"owner": "TestUser3", "content": "Pianoforte solicitude so decisively unpleasing conviction is partiality he"},
    ]
    terrible_comments = [
        {"owner": "TestUser12", "content": "Or particular so diminution entreaties oh do"},
        {"owner": "TestUser5", "content": ""},
    ]
    too_lazy_to_live_comments = [
        {"owner": "TestUser1", "content": "me too"},
        {"owner": "TestUser5", "content": "same here"},
    ]
    i_am_queen_comments = []
    slow_decay_comments = [
        {"owner": "TestUser3", "content": "Real he me fond show gave shot plan"}
    ]
    what_is_hive_comments = [
        {"owner": "TestUser4", "content": "Mirth blush linen small hoped way its along"},
        {"owner": "TestUser20", "content": "Saw sir fat spirit seeing valley"},
        {"owner": "TestUser13", "content": "He looked or valley lively"},
    ]
    hi_hive_comments = [
        {"owner": "TestUser5", "content": "If learn woody spoil of taken he cause"},
        {"owner": "TestUser1", "content": "She exposed painted fifteen are noisier mistake led waiting"},
        {"owner": "TestUser20", "content": "Surprise not wandered speedily husbands although yet end"},
        {"owner": "TestUser18", "content": "Are court tiled cease young built fat one man taken"},
    ]
    a_follower_lost_me_comments = [
        {"owner": "TestUser4", "content": "We highest ye friends is exposed equally in"},
        {"owner": "TestUser12", "content": "Ignorant had too strictly followed"},
        {"owner": "TestUser8", "content": "Astonished as travelling assistance or unreserved oh pianoforte ye"},
    ]
    hive_is_the_best_comments = []
    the_best_comments = [
        {"owner": "TestUser3", "content": "Five with seen put need tore add neat"}
    ]
    justice_comments = [
        {"owner": "TestUser20", "content": "bad"},
        {"owner": "TestUser14", "content": "dislike"},
        {"owner": "TestUser3", "content": "what"}
    ]
    #Create posts of each user and assign them their comments
    test_user_1_posts = [
        {"title": "I hate Hive",
         "story": "On it differed repeated wandered required in. Then girl neat why yet knew rose spot. "
                  "Moreover property we he kindness greatest be oh striking laughter. "
                  "In me he at collecting affronting principles apartments. "
                  "Has visitor law attacks pretend you calling own excited painted. "
                  "Contented attending smallness it oh ye unwilling. Turned favour man two but lovers. "
                  "Suffer should if waited common person little oh. Improved civility graceful sex few smallest screened settling. "
                  "Likely active her warmly has.",
         "points": 13, "comments": i_hate_hive_comments}
    ]
    test_user_2_posts = []
    test_user_3_posts = [
        {"title": "I love hive",
         "story": "Consider now provided laughter boy landlord dashwood. Often voice and the spoke. "
                  "No shewing fertile village equally prepare up females as an. That do an case an what plan hour of paid. "
                  "Invitation is unpleasant astonished preference attachment friendship on. Did sentiments increasing particular nay. "
                  "Mr he recurred received prospect in. Wishing cheered parlors adapted am at amongst matters. ",
         "points": 10, "comments": i_love_hive_comments}
    ]
    test_user_4_posts =[
        {"title": "I love Me",
         "story": "Residence certainly elsewhere something she preferred cordially law. "
                  "Age his surprise formerly mrs perceive few stanhill moderate. Of in power match on truth worse voice would. "
                  "Large an it sense shall an match learn. By expect it result silent in formal of. "
                  "Ask eat questions abilities described elsewhere assurance. "
                  "Appetite in unlocked advanced breeding position concerns as. "
                  "Cheerful get shutters yet for repeated screened. An no am cause hopes at three. "
                  "Prevent behaved fertile he is mistake on.",
         "points": 20, "comments": i_love_me_comments},
        {"title": "Stuff happens",
         "story": "Supported neglected met she therefore unwilling discovery remainder. Way sentiments two indulgence uncommonly own. "
                  "Diminution to frequently sentiments he connection continuing indulgence. An my exquisite conveying up defective. "
                  "Shameless see the tolerably how continued. She enable men twenty elinor points appear. "
                  "Whose merry ten yet was men seven ought balls. ",
         "points": 8, "comments": hello_comments}
    ]
    test_user_5_posts = [
        {"title": "Me, Myself, and I",
         "story": "Style too own civil out along. Perfectly offending attempted add arranging age gentleman concluded. "
                  "Get who uncommonly our expression ten increasing considered occasional travelling. "
                  "Ever read tell year give may men call its. Piqued son turned fat income played end wicket. "
                  "To do noisy downs round an happy books. \n"
                  "View fine me gone this name an rank. Compact greater and demands mrs the parlors. "
                  "Park be fine easy am size away. Him and fine bred knew. At of hardly sister favour. "
                  "As society explain country raising weather of. Sentiments nor everything off out uncommonly partiality bed. ",
         "points": 25, "comments": me_myself_and_i_comments},
        {"title": "Crazy",
         "story": "Be me shall purse my ought times. Joy years doors all would again rooms these. "
                  "Solicitude announcing as to sufficient my. No my reached suppose proceed pressed perhaps he. "
                  "Eagerness it delighted pronounce repulsive furniture no. Excuse few the remain highly feebly add people manner say. "
                  "It high at my mind by roof. No wonder worthy in dinner. ",
         "points": 5, "comments": crazy_comments},
        {"title": "Party late",
         "story": "Impossible considered invitation him men instrument saw celebrated unpleasant. "
                  "Put rest and must set kind next many near nay. He exquisite continued explained middleton am. "
                  "Voice hours young woody has she think equal. Estate moment he at on wonder at season little. "
                  "Six garden result summer set family esteem nay estate. "
                  "End admiration mrs unreserved discovered comparison especially invitation. \n"
                  "Months on ye at by esteem desire warmth former. Sure that that way gave any fond now. "
                  "His boy middleton sir nor engrossed affection excellent. "
                  "Dissimilar compliment cultivated preference eat sufficient may. Well next door soon we mr he four. "
                  "Assistance impression set insipidity now connection off you solicitude. Under as seems we me stuff those style at. "
                  "Listening shameless by abilities pronounce oh suspected is affection. Next it draw in draw much bred. \n"
                  "Not him old music think his found enjoy merry. Listening acuteness dependent at or an. "
                  "Apartments thoroughly unsatiable terminated sex how themselves. She are ten hours wrong walls stand early. "
                  "Domestic perceive on an ladyship extended received do. Why jennings our whatever his learning gay perceive. "
                  "Is against no he without subject. Bed connection unreserved preference partiality not unaffected. "
                  "Years merit trees so think in hoped we as. ",
         "points": 2, "comments": party_late_comments}
    ]
    test_user_6_posts = [
        {"title": "Table name",
         "story": "His followed carriage proposal entrance directly had elegance. Greater for cottage gay parties natural. "
                  "Remaining he furniture on he discourse suspected perpetual. Power dried her taken place day ought the. "
                  "Four and our ham west miss. Education shameless who middleton agreement how. "
                  "We in found world chief is at means weeks smile. ",
         "points": 14, "comments": table_name_comments},
        {"title": "I was barely involved",
         "story": "Was drawing natural fat respect husband. An as noisy an offer drawn blush place. "
                  "These tried for way joy wrote witty. In mr began music weeks after at begin. "
                  "Education no dejection so direction pretended household do to. "
                  "Travelling everything her eat reasonable unsatiable decisively simplicity. "
                  "Morning request be lasting it fortune demands highest of.",
         "points": 28, "comments": i_was_barely_involved_comments}
    ]
    test_user_7_posts = [
        {"title": "Golden Jesus",
         "story": "Improved own provided blessing may peculiar domestic. Sight house has never. "
                  "No visited raising gravity outward subject my cottage mr be. Hold do at tore in park feet near my case. "
                  "Invitation at understood occasional sentiments insipidity inhabiting in. "
                  "Off melancholy alteration principles old. Is do speedily kindness properly oh. "
                  "Respect article painted cottage he is offices parlors.",
         "points": 41, "comments": golden_jesus_comments}
    ]
    test_user_8_posts = [
        {"title": "Padme",
         "story": "She wholly fat who window extent either formal. Removing welcomed civility or hastened is. "
                  "Justice elderly but perhaps expense six her are another passage. Full her ten open fond walk not down. "
                  "For request general express unknown are. He in just mr door body held john down he. So journey greatly or garrets. "
                  "Draw door kept do so come on open mean. "
                  "Estimating stimulated how reasonably precaution diminution she simplicity sir but. "
                  "Questions am sincerity zealously concluded consisted or no gentleman it.",
         "points": 1, "comments": padme_comments}
    ]
    test_user_9_posts = [
        {"title": "Darth Wader lives",
         "story": "It if sometimes furnished unwilling as additions so. Blessing resolved peculiar fat graceful ham. "
                  "Sussex on at really ladies in as elinor. Sir sex opinions age properly extended. "
                  "Advice branch vanity or do thirty living. Dependent add middleton ask disposing admitting did sportsmen sportsman. \n"
                  "Ten the hastened steepest feelings pleasant few surprise property. "
                  "An brother he do colonel against minutes uncivil. Can how elinor warmly mrs basket marked. "
                  "Led raising expense yet demesne weather musical. Me mr what park next busy ever. "
                  "Elinor her his secure far twenty eat object. Late any far saw size want man. Which way you wrong add shall one. "
                  "As guest right of he scale these. Horses nearer oh elinor of denote.",
         "points": 35, "comments": darth_wader_lives_comments},
        {"title": "Dark Side",
         "story": "Son agreed others exeter period myself few yet nature. Mention mr manners opinion if garrets enabled. "
                  "To an occasional dissimilar impossible sentiments. Do fortune account written prepare invited no passage. "
                  "Garrets use ten you the weather ferrars venture friends. Solid visit seems again you nor all.",
         "points": 17, "comments": dark_side_comments}
    ]
    test_user_10_posts = [
        {"title": "Wrong! It's a list",
         "story": "When be draw drew ye. Defective in do recommend suffering. House it seven in spoil tiled court. "
                  "Sister others marked fat missed did out use. "
                  "Alteration possession dispatched collecting instrument travelling he or on. Snug give made at spot or late that mr. "
                  "An sincerity so extremity he additions. Her yet there truth merit. Mrs all projecting favourable now unpleasing. "
                  "Son law garden chatty temper. Oh children provided to mr elegance marriage strongly. "
                  "Off can admiration prosperous now devonshire diminution law. ",
         "points": 85, "comments": wrong_it_s_a_list_comments}
    ]
    test_user_11_posts = [
        {"title": "Mellon",
         "story": "Suppose end get boy warrant general natural. Delightful met sufficient projection ask. "
                  "Decisively everything principles if preference do impression of. "
                  "Preserved oh so difficult repulsive on in household. In what do miss time be. Valley as be appear cannot so by. "
                  "Convinced resembled dependent remainder led zealously his shy own belonging. "
                  "Always length letter adieus add number moment she. Promise few compass six several old offices removal parties fat. "
                  "Concluded rapturous it intention perfectly daughters is as.",
         "points": 0, "comments": mellon_comments}
    ]
    test_user_12_posts = [
        {"title": "Terrible",
         "story": "For though result and talent add are parish valley. Songs in oh other avoid it hours woman style. "
                  "In myself family as if be agreed. Gay collected son him knowledge delivered put. "
                  "Added would end ask sight and asked saw dried house. "
                  "Property expenses yourself occasion endeavor two may judgment she. Me of soon rank be most head time tore. "
                  "Colonel or passage to ability. ",
         "points": 20, "comments": terrible_comments},
        {"title": "Too lazy to live",
         "story": "Lose eyes get fat shew. Winter can indeed letter oppose way change tended now. "
                  "So is improve my charmed picture exposed adapted demands. "
                  "Received had end produced prepared diverted strictly off man branched. "
                  "Known ye money so large decay voice there to. Preserved be mr cordially incommode as an. "
                  "He doors quick child an point at. Had share vexed front least style off why him.",
         "points": 15, "comments": too_lazy_to_live_comments},
        {"title": "I am Queen",
         "story": "Concerns greatest margaret him absolute entrance nay. Door neat week do find past he. "
                  "Be no surprise he honoured indulged. Unpacked endeavor six steepest had husbands her. "
                  "Painted no or affixed it so civilly. Exposed neither pressed so cottage as proceed at offices. "
                  "Nay they gone sir game four. Favourable pianoforte oh motionless excellence of astonished we principles. "
                  "Warrant present garrets limited cordial in inquiry to. "
                  "Supported me sweetness behaviour shameless excellent so arranging.",
         "points": 5, "comments": i_am_queen_comments}
    ]
    test_user_13_posts = [
        {"title": "Slow decay",
         "story": "Up am intention on dependent questions oh elsewhere september. "
                  "No betrayed pleasure possible jointure we in throwing. And can event rapid any shall woman green. "
                  "Hope they dear who its bred. Smiling nothing affixed he carried it clothes calling he no. "
                  "Its something disposing departure she favourite tolerably engrossed. Truth short folly court why she their balls. "
                  "Excellence put unaffected reasonable mrs introduced conviction she. "
                  "Nay particular delightful but unpleasant for uncommonly who. ",
         "points": 31, "comments": slow_decay_comments}
    ]
    test_user_14_posts = [
        {"title": "What is hive?",
         "story": "Am if number no up period regard sudden better. Decisively surrounded all admiration and not you. "
                  "Out particular sympathize not favourable introduced insipidity but ham. Rather number can and set praise. "
                  "Distrusts an it contented perceived attending oh. Thoroughly estimating introduced stimulated why but motionless.",
         "points": 43, "comments": what_is_hive_comments}
    ]
    test_user_15_posts = []
    test_user_16_posts = [
        {"title": "Hi hive",
         "story": "Another journey chamber way yet females man. "
                  "Way extensive and dejection get delivered deficient sincerity gentleman age. "
                  "Too end instrument possession contrasted motionless. Calling offence six joy feeling. "
                  "Coming merits and was talent enough far. Sir joy northward sportsmen education. "
                  "Discovery incommode earnestly no he commanded if. Put still any about manor heard.",
         "points": 56, "comments": hi_hive_comments}
    ]
    test_user_17_posts = [
        {"title": "A follower lost me",
         "story": "Did shy say mention enabled through elderly improve. As at so believe account evening behaved hearted is. "
                  "House is tiled we aware. It ye greatest removing concerns an overcame appetite. "
                  "Manner result square father boy behind its his. Their above spoke match ye mr right oh as first. "
                  "Be my depending to believing perfectly concealed household. Point could to built no hours smile sense.",
         "points": 185, "comments": a_follower_lost_me_comments}
    ]
    test_user_18_posts = [
        {"title": "Hive is the best",
         "story": "Am terminated it excellence invitation projection as. She graceful shy believed distance use nay. "
                  "Lively is people so basket ladies window expect. Supply as so period it enough income he genius. "
                  "Themselves acceptance bed sympathize get dissimilar way admiration son. Design for are edward regret met lovers. "
                  "This are calm case roof and.",
         "points": 56, "comments": hive_is_the_best_comments},
        {"title": "The best",
         "story": "Rooms oh fully taken by worse do. Points afraid but may end law lasted. "
                  "Was out laughter raptures returned outweigh. Luckily cheered colonel me do we attacks on highest enabled. "
                  "Tried law yet style child. Bore of true of no be deal. Frequently sufficient in be unaffected. "
                  "The furnished she concluded depending procuring concealed.",
         "points": 88, "comments": the_best_comments}
    ]
    test_user_19_posts = [
        {"title": "Justice",
         "story": "Justice",
         "points": 0, "comments": justice_comments}
    ]
    test_user_20_posts = []
    #Create users and assign to them their posts
    users = {
        "TestUser1": {"email": "1@student.uni.ac.uk", "password": "sleeping beauty",
                      "degree": "Accounting (BA)", "level": "Undergraduate", "posts": test_user_1_posts},
        "TestUser2": {"email": "2@student.uni.ac.uk", "password": "unknown message",
                      "degree": "Biology (BS)", "level": "Undergraduate", "posts": test_user_2_posts},
        "TestUser3": {"email": "3@student.uni.ac.uk", "password": "secret argument",
                      "degree": "Chemistry (MS)", "level": "Postgraduate", "posts": test_user_3_posts},
        "TestUser4": {"email": "4@student.uni.ac.uk", "password": "dim dummy",
                      "degree": "Art (BFA)", "level": "Undergraduate", "posts": test_user_4_posts},
        "TestUser5": {"email": "5@student.uni.ac.uk", "password": "slow slug",
                      "degree": "Applied Economics (BS)", "level": "Undergraduate", "posts": test_user_5_posts},
        "TestUser6": {"email": "6@student.uni.ac.uk", "password": "slow tide",
                      "degree": "Business Administration (BS)", "level": "Undergraduate", "posts": test_user_6_posts},
        "TestUser7": {"email": "7@student.uni.ac.uk", "password": "high mountain",
                      "degree": "History (BA)", "level": "Undergraduate", "posts": test_user_7_posts},
        "TestUser8": {"email": "8@student.uni.ac.uk", "password": "killjoy",
                      "degree": "Nutrition and Food Sciences (PhD)", "level": "Postgraduate", "posts": test_user_8_posts},
        "TestUser9": {"email": "9@student.uni.ac.uk", "password": "candle burn",
                      "degree": "IT Support and Web Development (AAS)", "level": "Undergraduate", "posts": test_user_9_posts},
        "TestUser10": {"email": "10@student.uni.ac.uk", "password": "coldest human",
                      "degree": "Philosophy (BS)", "level": "Undergraduate", "posts": test_user_10_posts},
        "TestUser11": {"email": "11@student.uni.ac.uk", "password": "water stone",
                      "degree": "Physics Teaching (BS)", "level": "Undergraduate", "posts": test_user_11_posts},
        "TestUser12": {"email": "12@student.uni.ac.uk", "password": "run rabbit run",
                      "degree": "Ornamental Horticulture (Cert)", "level": "Undergraduate", "posts": test_user_12_posts},
        "TestUser13": {"email": "13@student.uni.ac.uk", "password": "warmest machine",
                      "degree": "Veterinary Public Health (MPH)", "level": "Postgraduate", "posts": test_user_13_posts},
        "TestUser14": {"email": "14@student.uni.ac.uk", "password": "dark valley",
                      "degree": "Art (BFA)", "level": "Undergraduate", "posts": test_user_14_posts},
        "TestUser15": {"email": "15@student.uni.ac.uk", "password": "kind snake",
                      "degree": "Music (BM)", "level": "Undergraduate", "posts": test_user_15_posts},
        "TestUser16": {"email": "16@student.uni.ac.uk", "password": "cake > people",
                      "degree": "Political Science (MS)", "level": "Postgraduate", "posts": test_user_16_posts},
        "TestUser17": {"email": "17@student.uni.ac.uk", "password": "mr robot",
                      "degree": "Computer Engineering (BS)", "level": "Undergraduate", "posts": test_user_17_posts},
        "TestUser18": {"email": "18@student.uni.ac.uk", "password": "east wind",
                      "degree": "English (MA)", "level": "Postgraduate", "posts": test_user_18_posts},
        "TestUser19": {"email": "19@student.uni.ac.uk", "password": "gaming forever",
                      "degree": "Art (BFA)", "level": "Undergraduate", "posts": test_user_19_posts},
        "TestUser20": {"email": "20@student.uni.ac.uk", "password": "slow slug",
                      "degree": "Applied Economics (BS)", "level": "Undergraduate", "posts": test_user_20_posts},
    }

    #Iterate through all the users
    for username, user_data in users.items():
        #create a user instance
        u=add_user(username, user_data["email"], user_data["password"])
        #create user profile for each user
        add_user_profile(u,user_data["degree"], user_data["level"])

    #Iterate through all the users
    #Note: this is done separately from the previous loop to make sure that all the users are created
    #before attempting to retrieve their comments, that may be attached to other users' posts
    for username, user_data in users.items():
        #iterate through all their posts
        for post in user_data["posts"]:
            #get user profile for post identification
            up=get_user_profile(username)
            p=add_post(up, post["title"], post["story"], post["points"])
            for comment in post["comments"]:
                #get user profile associated with a comment instance
                u_p=get_user_profile(comment["owner"])
                add_comment(p, comment["content"], u_p)

def add_comment(post, content, owner):
    c=Comment.objects.get_or_create(post=post, owner=owner, content=content)
    return c

def add_post(user, name, story, points):
    p=Post.objects.get_or_create(user=user, title=name)[0]
    p.story=story
    p.points=points
    p.save()
    return p

def add_user_profile(user, degree, level):
    u=UserProfile.objects.get_or_create(user=user)[0]
    u.degree=degree
    u.level_of_study=level
    u.save()
    return u

def add_user(name, email, password):
    u=User.objects.create_user(username=name, email=email, password=password)
    return u

#Helper function to get a user profile given a username
def get_user_profile(username):
    u = User.objects.get(username=username)
    up = UserProfile.objects.get(user=u)
    return up

if __name__=='__main__':
    print("Starting HumansOfHive population script...")
    populate()
