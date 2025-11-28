import os
import re

# Data for all 30 articles. 
# Key: filename (without path, assuming uniqueness or handled by site folder logic)
# Value: Dict with content fields.

articles_data = {
    # --- Site 1: Home Care ---
    "weak-legs.html": {
        "title": "老狗後腳無力怎麼辦？居家防滑與輔具實戰心得",
        "category": "居家照顧",
        "intro": "看著以前那個愛跳沙發的毛孩子，現在連站起來都很吃力，心裡真的很酸。後腳無力是老犬最常見的退化症狀之一，但這不代表牠們不能過好日子。",
        "h2": "為什麼會後腳無力？不只是「老了」",
        "body1": "很多人以為狗狗老了走不動是正常的，其實背後可能有退化性關節炎、髖關節發育不全，甚至是神經壓迫的問題。我一開始也以為只是牠懶得動，直到諮詢了獸醫，才發現牠每一變換姿勢都在忍痛。",
        "h3": "改善生活的具體建議",
        "list": [
            "<strong>防滑是關鍵：</strong> 家裡的磁磚地對牠們來說像溜冰場。鋪設瑜珈墊或止滑巧拼，能給牠們站起來的信心。",
            "<strong>輔具幫大忙：</strong> 使用後腳輔助帶（或用毛巾繞過腹部），在牠起身時輕輕提一把，減少關節負擔。",
            "<strong>適度按摩：</strong> 每天睡前幫牠熱敷按摩後腿肌肉，促進血液循環，但避開關節發炎處。"
        ],
        "story": "記得有一次，我看牠在磁磚地上滑倒，掙扎了好久才站起來，眼神充滿驚恐。那天我立刻去買了止滑墊鋪滿客廳。當晚，我看牠穩穩地走去喝水，那個自信的眼神，讓我覺得一切都值得了。",
        "observation": "最近發現，當我幫牠穿上防滑襪時，牠會主動把腳抬起來給我。以前牠很討厭穿鞋的，現在可能知道這東西能讓牠走路不滑吧？這種無聲的溝通，真的很奇妙。",
        "conclusion": "面對老去，我們能做的不是嘆氣，而是當牠的拐杖。只要多一點細心，牠們的老年生活依然可以很有尊嚴。"
    },
    "cataract-care.html": {
        "title": "狗狗眼睛變白了？白內障照顧與居家動線調整",
        "category": "居家照顧",
        "intro": "當你發現狗狗的黑眼珠中間出現混濁的白點，走路開始容易撞到東西，那可能是白內障找上門了。視力模糊會讓狗狗變得焦慮，但我們可以成為牠的導盲犬。",
        "h2": "看不見後的焦慮與適應",
        "body1": "狗狗的適應力其實比我們想像中強，因為牠們還有強大的嗅覺與聽覺。但在適應期，牠們會變得不敢走動、對光影變化敏感，甚至出現防禦性的吠叫。",
        "h3": "打造友善盲犬的家",
        "list": [
            "<strong>動線不更動：</strong> 家具擺設盡量固定，不要隨意換位置，讓牠能依靠記憶行走。",
            "<strong>邊角防護：</strong> 在桌腳、牆角貼上防撞泡棉，避免牠誤撞受傷。",
            "<strong>聲音引導：</strong> 走路時多跟牠說話，或在牠身上掛個小鈴鐺，讓你知道牠的位置，也讓牠知道你在哪。"
        ],
        "story": "剛確診白內障那陣子，牠變得很黏人，連去廁所都要跟。有次我不小心把椅子換了位置，牠一頭撞上去，愣在那裡好久。那一刻我好後悔，發誓以後家裡的擺設絕對不動。現在牠已經能在家裡自如穿梭，如果不說，沒人知道牠看不見。",
        "observation": "雖然眼睛看不清楚，但牠的聽覺似乎變敏銳了。現在只要我拿鑰匙的聲音稍微響一點，牠耳朵馬上就會豎起來。生命的出口，總是在意想不到的地方打開。",
        "conclusion": "失去視力不代表失去生活。只要給予足夠的安全感，牠們依然能用鼻子「看」見這個美麗的世界。"
    },
    "incontinence-care.html": {
        "title": "老狗漏尿不是故意：失禁護理與尿布挑選",
        "category": "居家照顧",
        "intro": "早上醒來發現床墊濕了一片，狗狗一臉愧疚地縮在角落...這不是牠不乖，而是牠的身體控制不住了。老犬失禁是照護上的一大挑戰，但請別責備牠。",
        "h2": "理解失禁的生理原因",
        "body1": "隨著年紀增長，括約肌鬆弛、荷爾蒙改變或神經退化，都可能導致漏尿。這對愛乾淨的狗狗來說，其實心理壓力比生理還大，牠們會覺得自己做錯事了。",
        "h3": "保持乾爽的照護重點",
        "list": [
            "<strong>勤換尿布/護理墊：</strong> 選擇吸水性好且透氣的尿布，避免長時間悶濕導致尿布疹。",
            "<strong>局部清潔：</strong> 每次更換時，用溫水清洗私密處並吹乾，可以塗抹凡士林隔離尿液刺激。",
            "<strong>定時如廁：</strong> 即使有穿尿布，還是建議每 3-4 小時帶牠去廁所或戶外，鼓勵牠排空膀胱。"
        ],
        "story": "第一次幫牠穿尿布時，牠僵在原地不敢動，表情好委屈。我抱著牠，輕輕摸牠的頭說：「沒關係，這樣很帥喔！」後來牠習慣了，看到我拿尿布還會自己走過來。其實牠們要的不多，就是我們不帶嫌棄的接納。",
        "observation": "我發現尿布的聲音對牠有些影響。如果魔鬼氈撕開的聲音太大，牠會嚇一跳。所以我現在都會先輕輕撕開，動作放慢。這些小細節，都是為了維護牠小小的自尊心。",
        "conclusion": "尿布包裹的不只是身體，更是我們對牠無限的包容。別讓失禁成為你們之間的隔閡，清潔乾淨後，依然要給牠一個大大的擁抱。"
    },
    "rainy-walk.html": {
        "title": "下雨天老狗不出門？室內嗅聞遊戲解悶指南",
        "category": "每日精選",
        "intro": "連續幾天的雨，讓習慣外出上廁所的老狗憋得好辛苦，在家裡也悶得慌。其實，下雨天是進行室內腦力激盪的好時機。",
        "h2": "為什麼老狗更需要室內活動？",
        "body1": "老狗體力雖差，但腦袋還是需要刺激。下雨天不能散步，容易讓牠們變得憂鬱或焦慮。透過嗅聞遊戲，可以消耗精力，也能預防失智。",
        "h3": "簡單好玩的嗅聞遊戲",
        "list": [
            "<strong>藏食遊戲：</strong> 把零食藏在毛巾捲裡、紙箱中，讓牠用鼻子找出來。",
            "<strong>雙手猜猜看：</strong> 握住零食讓牠猜在哪隻手，猜對了就給獎勵，簡單又能互動。",
            "<strong>慢食墊：</strong> 塗上優格或花生醬，讓牠慢慢舔食，舔舐動作有助於安撫情緒。"
        ],
        "story": "那次颱風天連下三天雨，牠趴在窗邊嘆氣。我靈機一動，把舊衣服堆成一座小山，裡面撒了些飼料。看著牠在衣服堆裡鑽來鑽去，尾巴搖得像螺旋槳一樣，我知道這個雨天牠過得很開心。",
        "observation": "玩嗅聞遊戲時，牠專注的神情真的跟年輕時一模一樣。雖然動作慢了，但鼻子的靈敏度可沒退化。看牠找到零食那種得意的樣子，我也跟著開心起來。",
        "conclusion": "下雨天不是無聊天。換個方式陪牠玩，你會發現老狗心裡，其實還住著一個愛玩的小朋友。"
    },
    "sigh-meaning.html": {
        "title": "狗狗嘆氣是無奈還是舒服？聽懂老狗的聲音",
        "category": "每日精選",
        "intro": "你注意過嗎？當老狗趴下來時，常會發出一聲長長的嘆息。這到底是舒服的放鬆，還是身體不舒服的求救訊號？",
        "h2": "解讀嘆氣的情緒密碼",
        "body1": "根據動物行為學家的觀察，嘆氣的含義取決於「情境」與「眼睛」。如果牠是趴下休息，眼睛半瞇，那通常是「好舒服，終於可以休息了」的滿足嘆氣。",
        "h3": "如何分辨異常的嘆氣",
        "list": [
            "<strong>觀察眼睛：</strong> 如果嘆氣時眼睛睜大直視著你，可能是在說「我好無聊」或「我想出去」。",
            "<strong>結合姿勢：</strong> 如果嘆氣伴隨著頻繁變換姿勢、無法安穩趴下，可能是關節疼痛在作怪。",
            "<strong>聲音長短：</strong> 短促且帶有嗚咽聲的嘆氣，通常是負面情緒或疼痛的表現。"
        ],
        "story": "我家老狗最近晚上睡前都會嘆一口好長的氣。一開始我好緊張，以為牠哪裡痛。後來仔細觀察，發現牠嘆完氣後，全身肌肉就完全放鬆，發出規律的打呼聲。原來，那是牠卸下一整天疲憊的儀式感啊。",
        "observation": "有趣的是，當我也跟著牠一起嘆氣時，牠會抬頭看我一眼，然後把頭靠在我的腳背上。彷彿在說：「你也累了嗎？一起休息吧。」這種跨物種的共鳴，真的很暖。",
        "conclusion": "用心聆聽每一個聲音，你會發現狗狗即使不說話，也一直在跟你溝通。那聲長長的嘆息，或許就是牠對這份安穩生活最真實的告白。"
    },
    "sleep-twitch.html": {
        "title": "老狗睡覺抽搐是在做夢嗎？區分夢境與癲癇",
        "category": "每日精選",
        "intro": "看著熟睡的狗狗四腳亂踢、嘴巴發出嗚嗚聲，我們常笑說牠在追兔子。但對老狗來說，有時候這可能是身體發出的警訊。",
        "h2": "快速動眼期 vs 神經問題",
        "body1": "狗狗和人一樣有快速動眼期 (REM)，這時做夢會有肢體動作是正常的。但老狗因為神經傳導物質退化，有時正常的抽動會變得比較劇烈，甚至被誤認為癲癇。",
        "h3": "觀察重點筆記",
        "list": [
            "<strong>喚醒反應：</strong> 做夢時輕聲呼喚通常叫得醒（雖然牠會一臉茫然）；癲癇發作時是完全失去意識的，叫不醒。",
            "<strong>持續時間：</strong> 做夢的抽動通常斷斷續續；癲癇發作則是持續且規律的僵硬或抽搐。",
            "<strong>發作後狀態：</strong> 做夢醒來會馬上恢復正常；癲癇後通常會有一段時間的迷失、流口水或疲憊。"
        ],
        "story": "有次半夜牠腿踢得好大力，還發出尖叫聲，我嚇得差點抱著牠衝急診。結果我手剛碰到牠，牠就驚醒了，一臉「幹嘛吵我睡覺」的表情看著我。雖然是虛驚一場，但也讓我更注意區分這兩者的差別。",
        "observation": "我發現牠做夢的時候，鬍鬚會微微顫抖，眼皮底下眼球轉動得很明顯。那時候的牠，或許夢到自己變回了年輕時的飛毛腿，在草原上盡情奔跑吧。",
        "conclusion": "老狗的睡眠品質很重要。如果確認只是做夢，就別打擾牠的美夢吧，讓牠在夢裡重溫那些奔跑的快樂時光。"
    },

    # --- Site 2: Diet ---
    "picky-eater.html": {
        "title": "老狗突然挑食？試試這三種「回春」拌飯法",
        "category": "精選主題",
        "intro": "以前是貪吃鬼，現在聞兩下就走？老狗挑食通常不是因為任性，而是嗅覺退化或牙口不好。別急著換飼料，試試這些增加食慾的小魔法。",
        "h2": "嗅覺退化是主因",
        "body1": "狗狗的味覺其實不發達，食慾很大程度取決於「嗅覺」。老狗嗅覺細胞減少，如果食物不夠香，牠們真的會覺得「這不是食物」。此外，牙結石或牙周病造成的疼痛，也會讓牠們拒絕進食。",
        "h3": "讓食物變好吃的技巧",
        "list": [
            "<strong>加熱釋放香氣：</strong> 加一點溫水或將鮮食加熱到微溫（約 38度），香氣會瞬間提升。",
            "<strong>使用天然誘食劑：</strong> 灑一點無鹽起司粉、柴魚片或滴幾滴魚油，這些濃郁的味道對狗狗很有吸引力。",
            "<strong>改變質地：</strong> 將飼料泡軟或改餵慕斯狀的主食罐，減少咀嚼的負擔。"
        ],
        "story": "這陣子牠連最愛的雞胸肉都不吃，我急得像熱鍋螞蟻。後來獸醫建議我把雞湯加熱後淋在飯上。結果那天，廚房飄出香味時，牠竟然自己走到碗邊坐好。看著牠把碗舔得乾乾淨淨，我差點感動到哭出來。",
        "observation": "我發現牠現在吃飯的速度變慢很多，有時候吃到一半會停下來發呆。這時候我不會催牠，只是靜靜陪在一旁。等牠休息夠了，自然會再低頭繼續吃。陪伴，是最好的開胃菜。",
        "conclusion": "吃飯是老狗生活中少數的樂趣之一。花點心思調整，讓牠重新找回對食物的熱情，也是我們能給予的溫柔。"
    },
    "kidney-diet.html": {
        "title": "腎臟病老犬飲食指南：低磷低蛋白怎麼吃？",
        "category": "精選主題",
        "intro": "確診腎衰竭後，獸醫的第一句話通常是「要控制飲食」。面對琳瑯滿目的處方飼料和繁瑣的營養標示，飼主該如何為毛孩把關？",
        "h2": "為什麼要限制磷與蛋白質？",
        "body1": "腎臟功能受損時，無法有效排出體內的磷與含氮廢物（蛋白質代謝產物）。過多的磷會導致骨骼病變，含氮廢物堆積則會造成尿毒症。因此，飲食控制的核心就是減輕腎臟負擔。",
        "h3": "飲食照顧的實戰策略",
        "list": [
            "<strong>嚴格篩選食材：</strong> 避開高磷食物如內臟、骨頭湯、蛋黃。改用蛋白、雞肉等優質蛋白質。",
            "<strong>水分攝取是關鍵：</strong> 腎病狗狗容易脫水。可以在食物中加水，或製作有味道的肉湯（無鹽）來騙水喝。",
            "<strong>配合處方飼料：</strong> 市售腎臟處方飼料都經過營養精算，是控制病情最安全的方式。若不愛吃，可嘗試混搭濕糧。",
        ],
        "story": "剛開始轉吃腎臟處方飼料時，牠非常抗拒，寧願餓肚子。後來我把處方罐頭加水打成泥，稍微溫熱一下，用針筒一點一點餵。雖然過程很辛苦，但看著指數慢慢穩定下來，這場長期抗戰我們一定要堅持下去。",
        "observation": "牠喝水的聲音變了，以前是豪邁地捲舌頭，現在則是小口小口地舔。我在家裡放了四五個水碗，讓牠走到哪都能喝到水。這小小的改變，希望能幫牠的腎臟多爭取一些時間。",
        "conclusion": "腎臟病的飲食控制是一條漫漫長路，充滿了妥協與堅持。但只要看到牠精神好一點，這一切的斤斤計較都是愛的表現。"
    },
    "supplements.html": {
        "title": "老狗保健品大補帖：魚油、益生菌該怎麼挑？",
        "category": "精選主題",
        "intro": "走進寵物店，架上滿滿的保健品讓人眼花撩亂。關節、皮膚、腸胃...到底老狗真的需要補這麼多嗎？還是只是補到飼主的心安？",
        "h2": "吃得精準比吃得多重要",
        "body1": "老狗身體機能下降，吸收能力變差，吃太多保健品反而增加代謝負擔。建議採取「缺什麼補什麼」的策略，並定期諮詢獸醫進行血液檢查，根據數值來調整。",
        "h3": "老犬三大必備營養素",
        "list": [
            "<strong>Omega-3 脂肪酸（魚油）：</strong> 抗發炎的神器，對關節炎、心血管及皮膚問題都有幫助。要選擇高濃度 EPA/DHA 的產品。",
            "<strong>葡萄糖胺/軟骨素：</strong> 針對關節退化的保養，能減緩軟骨磨損。建議選擇複方（如添加綠唇貽貝）效果較佳。",
            "<strong>益生菌：</strong> 老狗腸胃蠕動慢，容易便秘或軟便。益生菌能維持腸道菌叢平衡，增強免疫力。"
        ],
        "story": "以前我每天給牠塞五六種膠囊，搞得我們兩個都很壓力。後來醫生說：「只要好好吃飯，補重點就好。」我把保健品減半，只留魚油和關節藥，牠的食慾反而變好了。原來，減法照顧有時候更有效。",
        "observation": "把魚油剪開淋在飯上時，那個腥味我聞了皺眉，牠卻興奮地搖尾巴。對狗狗來說，這大概就是大海的鮮味吧？看牠吃得津津有味，我也就不嫌棄手上的魚腥味了。",
        "conclusion": "保健品是輔助，不是仙丹。最好的保養品，其實是均衡的飲食、適度的運動，還有你每天快樂的陪伴。"
    },
    "apple-core.html": {
        "title": "狗狗可以吃蘋果嗎？果核與種子的潛在危險",
        "category": "每日精選",
        "intro": "「喀擦！」每次我在削蘋果，狗狗總是會湊過來用渴望的眼神看著我。蘋果是健康的零食，但如果不小心處理，可能會變成致命毒藥。",
        "h2": "蘋果肉是寶，蘋果核是草",
        "body1": "蘋果果肉含有豐富的維生素 A、C 和纖維，對老狗的腸胃不錯。但是，蘋果核和種子含有「氰苷」，在體內代謝後會產生氰化物，雖然需要大量才致毒，但老狗代謝差，風險更高。",
        "h3": "安全餵食指南",
        "list": [
            "<strong>徹底去核去籽：</strong> 切蘋果時務必將果核部分完全切除，一顆種子都不要留。",
            "<strong>切成薄片：</strong> 老狗吞嚥能力差，大塊蘋果容易噎到。切成薄片或小丁最安全。",
            "<strong>適量即可：</strong> 蘋果糖分高，吃多容易胖或引起腹瀉。一天兩三片就夠了。"
        ],
        "story": "有次朋友來家裡，順手丟了一整顆蘋果核給狗吃，嚇得我當場伸手進狗嘴裡挖出來。朋友覺得我大驚小怪，但我知道，老狗禁不起任何一次的萬一。守護牠的健康，是我們飼主絕對的責任。",
        "observation": "牠吃蘋果時那種清脆的聲音，聽起來特別療癒。即使牙齒沒剩幾顆，牠還是喜歡用後面的牙床慢慢磨。那種為了美食不屈不撓的精神，真讓人佩服。",
        "conclusion": "天然的蔬果是不錯的零食，但前提是必須安全。花一分鐘去核切丁，換來的是牠安心享用美食的快樂笑臉。"
    },
    "drinking-sound.html": {
        "title": "喝水聲音變大了？觀察老狗的飲水量與方式",
        "category": "每日精選",
        "intro": "最近發現地板上的水漬變多了嗎？或是狗狗喝水時發出很大的「吧唧」聲？這可能不只是習慣改變，而是口腔或身體機能的警訊。",
        "h2": "喝水方式改變的信號",
        "body1": "狗狗是用舌頭捲水喝的。當老狗舌頭肌肉無力，或是牙齒疼痛、口腔腫瘤時，捲水的能力會變差，導致水大量漏出，喝水聲音變大，而且明明喝很久卻沒喝進多少水。",
        "h3": "如何協助老狗喝水",
        "list": [
            "<strong>墊高水碗：</strong> 減輕頸部和前腳的負擔，讓牠不用低頭太低就能喝到水。",
            "<strong>增加水碗數量：</strong> 在家裡不同角落多放幾個水碗，讓行動不便的牠隨時能補充水分。",
            "<strong>觀察飲水量：</strong> 突然喝水量暴增（多渴多尿）可能是腎臟病或糖尿病徵兆；喝太少則容易脫水。"
        ],
        "story": "這幾天看牠喝水喝得好辛苦，水花濺得滿地都是。我把水碗架高了十公分，牠喝起來明顯輕鬆多了，也不會一直嗆到。原來一個小小的改變，就能幫牠省下這麼多力氣。",
        "observation": "透過陽光，看著牠舌頭捲起水柱的瞬間，雖然動作比年輕時慢了，但那種專注活著的姿態依然美麗。地板濕了沒關係，擦乾就好，只要你還願意大口喝水，就是好事。",
        "conclusion": "喝水這件小事，藏著老狗的健康密碼。細心觀察，適時調整，讓補充水分不再是一件費力的苦差事。"
    },
    "kitchen-crumbs.html": {
        "title": "廚房地上的碎屑：老狗掃地機器人的危機",
        "category": "每日精選",
        "intro": "家裡有隻貪吃狗，掉在地上的食物通常活不過三秒。但隨著牠變老，這個「掃地機器人」的功能可能會帶來致命危機。",
        "h2": "腸胃不再像鐵打的",
        "body1": "年輕時亂吃可能拉個肚子就好，但老狗的消化系統脆弱，一點點蔥蒜、洋蔥屑，或是高油脂的碎肉，都可能引發嚴重的胰臟炎或溶血性貧血。",
        "h3": "廚房安全守則",
        "list": [
            "<strong>隨手清掃：</strong> 料理時掉落的食材馬上撿起來，不要抱持「等下再掃」的僥倖心態。",
            "<strong>設立結界：</strong> 煮飯時使用兒童安全門欄，禁止狗狗進入廚房重地。",
            "<strong>垃圾桶加蓋：</strong> 老狗嗅覺依然靈敏，會去翻垃圾桶找剩菜。務必選用有蓋且不易推倒的垃圾桶。"
        ],
        "story": "上個月我不小心掉了一小塊洋蔥，動作太慢被牠搶先一步吞下去。那晚我整夜沒睡守著牠，深怕牠出現血尿。幸好量很少沒事，但那種恐懼我不想再經歷一次。現在我煮飯，一定先把牠請出廚房。",
        "observation": "雖然眼睛不太好了，但只要我一開冰箱，牠就會準時出現在廚房門口，鼻子抽動著偵測有什麼好料。這種對食物的執著，大概是牠保持活力的來源吧？但我還是得狠下心把門關上。",
        "conclusion": "愛牠就別讓牠亂吃。廚房裡的潛在危險太多，嚴格把關，才是對老狗腸胃最溫柔的呵護。"
    },

    # --- Site 3: Mental Health ---
    "night-barking.html": {
        "title": "半夜不睡覺一直叫？安撫老狗夜鳴的實用技巧",
        "category": "精選主題",
        "intro": "夜深人靜，家裡的老狗卻突然對著空氣吠叫，或是無目的地來回踱步。這不只是吵到鄰居的問題，更是狗狗感到不安的求救信號。",
        "h2": "是任性還是生病？認識 CCD",
        "body1": "老犬認知障礙症 (CCD)，類似人類的阿茲海默症，會導致日夜顛倒、空間迷失和焦慮。夜鳴通常是因為牠們在黑暗中醒來，不知道自己在哪裡，感到恐慌而呼喚主人。",
        "h3": "改善夜鳴的對策",
        "list": [
            "<strong>小夜燈：</strong> 在牠睡覺的地方留一盞溫暖的小夜燈，讓牠醒來時能看清楚環境，減少恐懼。",
            "<strong>白天消耗體力：</strong> 白天盡量讓牠保持清醒，多曬太陽、多互動，調整生理時鐘，晚上才比較好睡。",
            "<strong>安撫與陪伴：</strong> 當牠夜鳴時，輕聲安撫牠，但不要過度開燈或陪玩，讓牠知道現在是睡覺時間。"
        ],
        "story": "那陣子我也快崩潰了，每晚都被叫醒三四次。後來我在牠窩邊放了一件有我味道的舊衣服，並開了盞昏黃的燈。神奇的是，牠的叫聲變成了輕微的哼哼，好像知道我就在身邊，慢慢地又能安穩睡過夜了。",
        "observation": "有時候半夜醒來，看牠站在客廳中央發呆，背影看起來好孤單。我會走過去輕輕摸摸牠，牽牠回窩。牠嘆了一口氣，把頭埋進被子裡。原來牠要的，只是一份「我不孤單」的確認。",
        "conclusion": "夜鳴是老狗無助的哭泣。多一點耐心，多一盞燈，讓我們陪牠度過漫長黑夜裡的迷惘時刻。"
    },
    "dementia-signs.html": {
        "title": "是老番癲還是失智？老犬認知障礙的早期徵兆",
        "category": "精選主題",
        "intro": "「牠最近好像變笨了，教過的都忘光，還會卡在桌腳出不來。」別以為這只是單純的老化，這可能是老犬失智症悄悄找上門了。",
        "h2": "早期發現，延緩退化",
        "body1": "老犬失智是不可逆的腦部退化，但如果能早期發現，透過藥物和環境輔助，可以有效延緩惡化速度。關鍵在於飼主是否能察覺那些微小的行為改變。",
        "h3": "常見的失智行為清單 (DISHA)",
        "list": [
            "<strong>迷失方向 (Disorientation)：</strong> 在熟悉的家裡迷路，卡在牆角或門後發呆。",
            "<strong>互動改變 (Interactions)：</strong> 變得不愛理人，或是反而變得異常黏人。",
            "<strong>睡眠改變 (Sleep)：</strong> 白天昏睡，晚上遊蕩、吠叫。",
            "<strong>隨地便溺 (House soiling)：</strong> 忘記上廁所的習慣，走到哪尿到哪。"
        ],
        "story": "當我看著牠對著鏡子裡的自己吠叫，甚至認不出我是誰的時候，心真的很痛。但我告訴自己，牠不是故意忘記我的，牠的靈魂只是迷路了。我要更有耐心地，一遍又一遍地重新介紹我自己。",
        "observation": "牠現在常常會走到門口，卻忘了是要進去還是出來，站在那裡猶豫好久。這時候我會輕輕推牠一下，牠就會恍然大悟地搖搖尾巴。做牠的導航員，是我現在最重要的工作。",
        "conclusion": "失智會帶走記憶，但帶不走愛。即使牠忘了全世界，只要我還記得我們之間的故事，那就夠了。"
    },
    "hospice-care.html": {
        "title": "最後一哩路的溫柔：安寧照顧與道別的勇氣",
        "category": "精選主題",
        "intro": "當醫療只能延長痛苦，或許該是時候放手，轉向安寧照顧。這不是放棄，而是選擇用最舒適的方式，陪牠走完最後的旅程。",
        "h2": "什麼是寵物安寧照顧？",
        "body1": "安寧照顧的重點不再是「治癒疾病」，而是「緩解痛苦」與「提升生活品質」。包含疼痛控制、衛生護理、營養支持，以及最重要的——情感陪伴。",
        "h3": "居家安寧的準備",
        "list": [
            "<strong>疼痛管理：</strong> 與獸醫討論止痛方案，確保牠在無痛的狀態下休息。",
            "<strong>環境舒適：</strong> 準備柔軟、保暖且易清潔的床舖，保持身體乾爽。",
            "<strong>好好道別：</strong> 花時間陪牠說話、摸摸牠，讓牠在愛的包圍下，沒有遺憾地離開。"
        ],
        "story": "在牠離開的前幾天，我把床墊搬到客廳地板，陪牠一起睡。牠已經沒力氣抬頭，但尾巴尖端還是會因為我的聲音微微抽動。那幾個夜晚很安靜，我們就在呼吸聲中，完成了最漫長也最溫柔的告別。",
        "observation": "牠的眼神變得好清澈，好像看透了一切。有時候牠會盯著某個角落看，眼神很平靜。人家說那是因為牠看到了接引的天使，我願意相信，因為那代表牠即將去一個沒有病痛的地方。",
        "conclusion": "道別很難，但這是我們能給牠最後的禮物。謝謝你來過我的生命，現在，換我勇敢地送你去飛翔。"
    },
    "old-collar.html": {
        "title": "舊項圈的味道：氣味如何安撫老狗的情緒",
        "category": "每日精選",
        "intro": "你是不是也捨不得丟掉狗狗的舊玩具或舊被子？其實對視力聽力退化的老狗來說，這些充滿「家味」的東西，是牠們最重要的安全感來源。",
        "h2": "氣味是連結記憶的鑰匙",
        "body1": "狗狗的嗅覺中樞與情緒腦區緊密相連。熟悉的氣味能讓牠們感到放鬆、安定。當環境陌生或感到焦慮時，一個舊項圈或一件主人的衣服，效果勝過千言萬語。",
        "h3": "善用氣味療法",
        "list": [
            "<strong>保留舊物：</strong> 狗狗睡習慣的墊子不要太常洗（或不要用強烈味道的洗劑），保留牠熟悉的味道。",
            "<strong>主人衣物：</strong> 出門時留一件穿過的T恤在牠窩裡，就像你在家陪牠一樣。",
            "<strong>避免強烈香氛：</strong> 老狗對人工香精很敏感，避免在家使用擴香或濃烈香水。"
        ],
        "story": "搬家後牠一直焦躁不安，整晚走來走去。後來我翻出牠戴了八年的那條破爛舊項圈放在新窩旁，牠聞了聞，轉了兩圈，竟然就安穩地睡著了。原來，那上面有我們十年來共同生活的記憶味道。",
        "observation": "牠現在睡覺前，一定要把鼻子埋進那條破破的小被子裡，深吸一口氣。那個陶醉的表情，就像吸毒一樣（笑）。那是牠的安撫巾，也是牠的安全堡壘。",
        "conclusion": "在這個不斷變化的世界裡，熟悉的氣味是牠們唯一的座標。別急著汰舊換新，那些舊東西，藏著讓牠安心的魔法。"
    },
    "smell-emotions.html": {
        "title": "狗狗聞得到你的焦慮？情緒傳遞與費洛蒙",
        "category": "每日精選",
        "intro": "每當我心情不好或緊張時，狗狗好像都知道，會默默靠過來舔我的手。這不是巧合，狗狗真的能「聞」到我們的情緒。",
        "h2": "費洛蒙的秘密",
        "body1": "人類在緊張或恐懼時，汗腺會分泌特殊的化學物質。狗狗敏銳的嗅覺能捕捉到這些費洛蒙的變化。對於本身就容易焦慮的老狗來說，主人的情緒會直接傳染給牠們。",
        "h3": "成為牠的安定力量",
        "list": [
            "<strong>保持平穩心情：</strong> 在照顧生病老犬時，你的焦慮會讓牠覺得自己病得很重。深呼吸，保持鎮定。",
            "<strong>使用安撫費洛蒙：</strong> 市售的插電式費洛蒙（如 Adaptil）能模擬狗媽媽的味道，幫助穩定老犬情緒。",
            "<strong>正向語氣：</strong> 即使心裡難過，跟牠說話時也要用輕快、溫柔的語調。"
        ],
        "story": "確診那天我在診間哭了，牠雖然身體不舒服，卻努力爬過來把頭靠在我膝蓋上。那一刻我擦乾眼淚，告訴自己：為了牠，我必須堅強。因為我是牠的天，我不能塌下來。",
        "observation": "很神奇，只要我一嘆氣，牠的耳朵就會往後貼；但我如果哼歌，牠的尾巴就會跟著節奏拍打地板。我們是如此緊密相連，我的快樂，就是牠的快樂。",
        "conclusion": "老狗是我們情緒的鏡子。給牠一個情緒穩定的主人，就是給牠最好的晚年照顧。"
    },
    "sunbathing.html": {
        "title": "曬太陽是最好的補藥？老犬日光浴的好處",
        "category": "每日精選",
        "intro": "看著老狗躺在陽台，跟著陽光移動位置，睡得一臉幸福。曬太陽不只是舒服，對老狗的生理與心理健康都有意想不到的好處。",
        "h2": "天然的紅外線治療",
        "body1": "陽光的溫暖能促進血液循環，舒緩僵硬的關節肌肉。此外，日照能刺激大腦分泌血清素（快樂荷爾蒙）和褪黑激素（睡眠荷爾蒙），有助於穩定情緒和改善夜間睡眠。",
        "h3": "曬太陽注意事項",
        "list": [
            "<strong>注意溫度：</strong> 老狗體溫調節差，避免正午烈日直射，容易中暑。清晨或傍晚的斜射光最適合。",
            "<strong>時間控制：</strong> 每次 15-20 分鐘即可，不用太久。",
            "<strong>隨時補水：</strong> 曬太陽時旁邊一定要放水碗，避免脫水。"
        ],
        "story": "現在每天早上的例行公事，就是扶著牠到陽台躺椅上。看牠瞇著眼，享受微風和暖陽，嘴角微微上揚的樣子。那是我們最平靜、最享受的早晨時光。連醫生都說，牠最近氣色變好了。",
        "observation": "牠曬太陽時有一種特殊的味道，像曬過棉被那種暖烘烘的香味。我最喜歡把臉埋在牠曬得熱熱的毛裡深吸一口氣，那就是幸福的味道吧。",
        "conclusion": "陽光是免費的，也是無價的。只要天氣好，就帶牠去行光合作用吧，讓大自然的能量療癒牠疲憊的身體。"
    },

    # --- Site 4: Grooming ---
    "gentle-bath.html": {
        "title": "老狗洗澡像打仗？溫柔洗澡法讓清潔變享受",
        "category": "精選主題",
        "intro": "以前洗澡是潑水大戰，現在洗澡卻怕牠滑倒、怕牠著涼。老狗的洗澡工程需要更細膩的安排，讓清潔不再是負擔。",
        "h2": "為什麼老狗怕洗澡？",
        "body1": "浴室地板濕滑讓關節痛的狗狗站不穩，產生恐懼。加上熱水會加速血液循環，可能增加心臟負擔。因此，老狗洗澡講求「速戰速決」與「安全第一」。",
        "h3": "溫柔洗澡三步驟",
        "list": [
            "<strong>止滑是基礎：</strong> 浴室地板和浴缸內一定要鋪止滑墊，讓牠站得穩，心就安。",
            "<strong>分區清洗：</strong> 不需要每次都全身大洗，可以今天洗身體，明天洗頭，或只做局部清潔。",
            "<strong>溫控與保暖：</strong> 水溫控制在 35-37 度，洗完立刻用吸水毛巾擦乾並吹乾，避免感冒。"
        ],
        "story": "有次牠在浴室滑了一下，後來只要聽到水聲就發抖。我改用濕毛巾幫牠擦澡，邊擦邊按摩，還放輕音樂。現在「洗澡」時間變成了我們的「SPA」時光，牠甚至會舒服到睡著。",
        "observation": "吹毛的時候，我發現牠很喜歡暖風吹在後背關節的地方。那時候牠會把眼睛閉起來，頭低低的。原來吹風機不只是吹乾毛，還順便幫牠做了熱敷復健呢。",
        "conclusion": "洗澡不只是為了乾淨，更是檢查身體、增進感情的好機會。把動作放慢，溫柔一點，讓牠重新愛上被呵護的感覺。"
    },
    "nail-trimming.html": {
        "title": "指甲太長影響走路！老狗剪指甲的減壓技巧",
        "category": "精選主題",
        "intro": "「喀喀喀...」聽到狗狗走路指甲敲擊地板的聲音了嗎？這代表指甲太長了！對老狗來說，過長的指甲會改變足部著力點，加重關節疼痛。",
        "h2": "剪指甲是為了走路",
        "body1": "老狗運動量減少，指甲磨損慢，很容易過長倒插或歪斜。長指甲會讓腳趾被頂起，導致身體重心後移，讓原本就脆弱的後腿負擔更重。",
        "h3": "不流血、不緊張的修剪法",
        "list": [
            "<strong>少量多次：</strong> 血管（粉紅色部分）會隨指甲變長。不要想一次剪短，每週剪一點點，讓血管慢慢退後。",
            "<strong>善用磨甲機：</strong> 如果牠怕指甲剪的「喀嚓」聲，改用磨甲機慢慢磨，震動感通常比痛感好接受。",
            "<strong>躺著剪：</strong> 站著剪對老狗關節負擔大，讓牠舒服地側躺在床上剪，剪完給獎勵。"
        ],
        "story": "牠以前看到指甲剪就躲。後來我發現趁牠睡午覺迷迷糊糊時偷剪最有效。一次剪一隻腳，剪完塞一顆零食。現在牠看到指甲剪，反而會期待地看著零食罐。原來恐懼是可以被美食克服的。",
        "observation": "剪完指甲後，牠走路的聲音變小了，步伐看起來也輕盈了一些。雖然只是幾毫米的差別，但對關節痛的牠來說，可能就是「痛」與「不痛」的距離。",
        "conclusion": "別忽視小小的指甲。定期修剪，是維護老狗行走能力最簡單也最重要的一環。"
    },
    "grooming-fur.html": {
        "title": "梳毛不只是為了漂亮！檢查腫塊的黃金時間",
        "category": "精選主題",
        "intro": "老狗毛髮容易乾澀、打結，皮膚抵抗力也變差。每天花十分鐘梳毛，不只能讓皮毛亮麗，更是全身健康檢查的最佳時機。",
        "h2": "梳毛是愛的觸摸",
        "body1": "梳毛能促進皮膚血液循環，代謝廢毛。更重要的是，透過梳毛，你可以摸遍牠全身每一寸皮膚，及早發現不明腫塊、傷口或寄生蟲。",
        "h3": "梳毛檢查重點",
        "list": [
            "<strong>選對梳子：</strong> 老狗皮膚薄，選用針梳要有圓頭保護，或改用鬃毛梳、按摩梳，避免刮傷皮膚。",
            "<strong>檢查團塊：</strong> 順著毛流梳，如果梳子卡住或摸到皮下有凸起，要記錄位置大小並就醫。",
            "<strong>觀察皮屑：</strong> 如果皮屑異常多或有紅疹，可能是皮膚病或內分泌問題（如甲狀腺低下）。"
        ],
        "story": "就是那次梳毛，我在牠腋下摸到一顆小小的硬塊。因為發現得早，切除後化驗是良性的。醫生說如果再晚半年可能就變大了。那把梳子，真的是牠的救命恩人。",
        "observation": "每次梳到屁股上方那塊區域，牠的腳就會不由自主地跟著踢，好像很癢又很舒服的樣子。這成了我們之間的小遊戲，看誰先忍不住笑場（雖然牠不會笑，但牠會哈氣）。",
        "conclusion": "把梳毛當成每天的親密時光吧。在梳理毛髮的同時，你也在梳理著你們之間那份深厚的羈絆。"
    },
    "bad-breath.html": {
        "title": "口臭是生病訊號？老犬口腔護理與刷牙",
        "category": "每日精選",
        "intro": "狗狗嘴巴臭臭的，是老了自然會這樣嗎？絕對不是！口臭通常是牙周病、牙結石甚至腎臟病的警訊。",
        "h2": "牙痛不是病，痛起來要狗命",
        "body1": "老狗常因長年牙結石累積導致牙齦發炎、牙齒鬆動。口腔細菌甚至會隨著血液流向心臟和腎臟，造成更嚴重的器官衰竭。",
        "h3": "老狗還能刷牙嗎？",
        "list": [
            "<strong>循序漸進：</strong> 如果沒刷牙習慣，先用紗布沾水擦拭牙齒，讓牠習慣異物感。",
            "<strong>潔牙產品輔助：</strong> 使用寵物專用潔牙凝膠或潔牙水，雖然效果不如刷牙，但總比沒有好。",
            "<strong>軟食後必清潔：</strong> 老狗常吃軟飯或罐頭，更容易卡牙縫，飯後務必檢查清潔。"
        ],
        "story": "牠這幾年掉了好幾顆牙，舌頭常會掉出來，看起來呆萌但其實很讓人心疼。我現在每天睡前都用紗布幫牠擦牙齦，雖然牠有時候會不耐煩撇頭，但為了僅存的幾顆牙，我是不會退讓的。",
        "observation": "幫牠刷牙時，能近距離聞到牠嘴裡的味道。雖然不香，但那是一種熟悉的、生命的氣息。只要這股氣息還在，我就會覺得很安心。",
        "conclusion": "一口好牙是長壽的根本。不管牠幾歲，口腔護理永遠不嫌晚。守護牠的牙，就是守護牠大口吃飯的幸福。"
    },
    "belly-rub.html": {
        "title": "摸肚子不只是撒嬌！檢查腹部腫塊與敏感度",
        "category": "每日精選",
        "intro": "狗狗翻肚子討摸摸，是最信任你的表現。在享受這療癒時刻的同時，別忘了順便當個「觸診醫生」。",
        "h2": "指尖下的健康密碼",
        "body1": "腹部柔軟，最容易摸到異常。很多臟器腫瘤（如脾臟、肝臟腫瘤）早期可能只是腹部微凸或摸到硬塊。透過日常撫摸，你可以建立牠正常的「身體地圖」，一旦有變化能馬上察覺。",
        "h3": "摸肚肚檢查法",
        "list": [
            "<strong>輕壓觸診：</strong> 用指腹輕輕按壓腹部，正常的肚子應該是軟軟的，沒有明顯硬塊。",
            "<strong>觀察反應：</strong> 如果摸到特定位置牠會回頭咬、發抖或繃緊肌肉，那裡可能有疼痛。",
            "<strong>檢查皮膚：</strong> 腹部毛少，容易看到瘀青、紅點或黑頭粉刺，這些都是皮膚健康的指標。"
        ],
        "story": "牠最近不愛讓人摸肚子，我以為是心情不好。後來強行檢查才發現腹部有一大片瘀青，原來是凝血功能出了問題。還好發現得早。現在牠翻肚子，我都會多留心摸兩下，這是我們的保命儀式。",
        "observation": "牠肚子上有一小塊胎記，隨著年紀變大，胎記好像也跟著變皺了。摸著那層鬆鬆的肚皮，手感雖然不如年輕時緊實，但卻有一種歲月沉澱下來的柔軟。",
        "conclusion": "下次牠翻肚子時，多花一分鐘仔細摸摸吧。你的指尖，可能是最早發現病魔的雷達。"
    },
    "popcorn-paws.html": {
        "title": "腳掌有爆米花味？老狗足部護理與指間炎",
        "category": "每日精選",
        "intro": "拿起來聞聞狗狗的腳掌，是不是有一股像玉米片或爆米花的味道？這味道雖然可愛，但太濃烈可能代表細菌或酵母菌滋生了。",
        "h2": "老狗的腳掌危機",
        "body1": "老狗免疫力降，加上走路姿勢改變（拖著腳走），腳掌容易磨損、潮濕。指間炎、肉墊過度角化（變硬裂開）是常見問題，會讓牠們走路像踩在針上一樣痛。",
        "h3": "護掌三部曲",
        "list": [
            "<strong>保持乾燥：</strong> 散步回來務必把腳趾縫擦乾，潮濕是細菌的溫床。",
            "<strong>修剪腳底毛：</strong> 腳底毛太長會包住濕氣，也容易打滑。定期修剪讓肉墊透氣。",
            "<strong>滋潤肉墊：</strong> 擦寵物專用的護掌霜或凡士林，預防肉墊龜裂流血。"
        ],
        "story": "有陣子牠一直舔腳，我以為是愛乾淨。直到翻開腳底看，裡面紅通通的一片還流湯。那次治療了好久才好。現在我每天都會檢查牠的腳丫子，那是帶牠走遍世界的輪胎，要好好保養。",
        "observation": "牠的肉墊以前是粉黑色的，現在磨得白白的，摸起來像砂紙。這些粗糙的痕跡，都是牠陪我走過無數路途的證明。擦上護掌膏時，牠會縮一下，然後又乖乖讓我弄，真的很乖。",
        "conclusion": "健康的腳掌才能帶牠走更遠的路。別忽略那股爆米花味，守護好牠的每一步，讓我們一起走得更久。"
    },

    # --- Site 5: Travel ---
    "travel-with-senior.html": {
        "title": "帶老狗去旅行：行程規劃與裝備清單",
        "category": "精選主題",
        "intro": "「牠都老了，在家休息就好吧？」其實，適度的戶外刺激能活化老狗的大腦。只要做好準備，老狗也能當個快樂的背包客。",
        "h2": "慢遊，是老犬旅行的精髓",
        "body1": "帶老狗出門，行程不能趕。放棄那些打卡景點，選擇平坦的草地、有樹蔭的公園。重點不是「去了哪裡」，而是「我們在一起」。",
        "h3": "老犬旅行必備清單",
        "list": [
            "<strong>寵物推車/背巾：</strong> 這是必備的神器。牠走累了就上車，既能休息又能參與行程，不造成關節負擔。",
            "<strong>熟悉的睡窩：</strong> 外宿時帶上牠熟悉的毯子或床，減少認床的焦慮。",
            "<strong>急救包與藥物：</strong> 常用藥（心臟病、關節藥）要帶足量，並查好目的地附近的24小時動物醫院。"
        ],
        "story": "去年我們去了一趟海邊。雖然牠已經跑不動了，只能趴在推車上看海。但當海風吹起牠的耳朵，牠瞇著眼深吸一口氣的表情，跟我十年前帶牠來時一模一樣。那張照片，是我最珍貴的收藏。",
        "observation": "在車上牠總是堅持要看窗外，即使累得眼皮打架也不肯睡。直到我握住牠的手，跟牠說「到了叫你」，牠才放心地倒頭大睡。原來牠是怕錯過跟我一起看的風景啊。",
        "conclusion": "趁牠還能動，多帶牠出去看看吧。那些風景會刻在牠的腦海裡，而牠快樂的樣子，會永遠刻在你的心裡。"
    },
    "car-sickness.html": {
        "title": "老狗暈車怎麼辦？減緩焦慮與暈車的對策",
        "category": "精選主題",
        "intro": "以前坐車是兜風，現在坐車卻一直流口水、發抖？老狗因為前庭神經退化，平衡感變差，反而比年輕時更容易暈車。",
        "h2": "暈車還是焦慮？",
        "body1": "有些老狗是因為身體不適（關節痛無法坐穩）而討厭坐車，有些則是真的暈車。流口水、哈氣、僵硬發抖都是徵兆。",
        "h3": "讓乘車變舒適",
        "list": [
            "<strong>穩定身體：</strong> 使用車用安全帶或運輸籠，避免車身晃動時牠要費力抓地，減少身體負擔。",
            "<strong>保持通風：</strong> 開一點窗戶讓新鮮空氣流通，能有效減緩暈眩感。",
            "<strong>少量進食：</strong> 出發前兩小時不要吃大餐，但也不要完全空腹（胃酸過多也不舒服），吃點小零食即可。"
        ],
        "story": "有次牠在車上吐得一塌糊塗，之後看到車門開就逃跑。後來我試著只在車上餵牠吃最愛的肉乾，不發動車子。慢慢讓牠把「車子」跟「好事」連結起來。現在牠雖然還是不愛坐車，但至少願意為了肉乾忍耐一下。",
        "observation": "牠暈車時會把頭靠在前座的椅背上，用一種求救的眼神看著我。這時候我會伸手摸摸牠的耳朵，牠的呼吸就會稍微慢下來。在搖晃的車廂裡，我是牠唯一的定心丸。",
        "conclusion": "別因為暈車就放棄出門。多點耐心訓練，做好防護，我們還是可以一起去很遠的地方。"
    },
    "park-bench.html": {
        "title": "公園長椅上的約會：不動也能充滿刺激的散步",
        "category": "精選主題",
        "intro": "誰說散步一定要「走」？對於走不動的老狗來說，坐在公園長椅上觀察世界，大腦運轉的程度不輸給跑操場三圈。",
        "h2": "靜態散步的魅力",
        "body1": "感官刺激（視、聽、嗅）對老狗非常重要。坐在公園裡，看著小孩跑跳、聞著草地味道、聽著鳥叫，這些豐富的資訊能活化大腦，預防失智，同時又保護了關節。",
        "h3": "如何進行「長椅約會」",
        "list": [
            "<strong>選對位置：</strong> 找個有樹蔭、視野開闊但不會太過吵雜（避免嚇到）的長椅。",
            "<strong>配合點心：</strong> 帶點零食，邊看風景邊野餐，把這變成一種獎勵活動。",
            "<strong>觀察反應：</strong> 注意牠的眼神跟耳朵，當牠專注看某個東西時，可以輕聲跟牠介紹：「那是小鳥喔」。"
        ],
        "story": "現在我們每天傍晚都會去公園坐半小時。有次一隻蝴蝶停在牠鼻頭上，牠嚇成鬥雞眼，動都不敢動。那一幕逗得旁邊的路人都笑了。這種平靜的快樂，是老狗獨有的浪漫。",
        "observation": "雖然身體沒動，但牠的鼻子一直在動，耳朵也轉來轉去。回家後牠睡得特別香，跟去跑了一圈回來一樣累。原來「用腦」真的很消耗體力呢。",
        "conclusion": "換個方式散步，世界依然寬廣。只要和你在一起，就算只是坐著發呆，也是最棒的冒險。"
    },
    "car-window.html": {
        "title": "狗狗為什麼愛探頭吹風？車窗外的氣味百科全書",
        "category": "每日精選",
        "intro": "開車時，狗狗總是堅持要把鼻子湊到窗戶縫隙，閉著眼享受風的吹拂。這不只是為了涼快，而是在閱讀「空氣報紙」。",
        "h2": "時速六十公里的氣味資訊",
        "body1": "風帶來了遠處的燒烤味、其他狗的味道、海水的鹹味...對嗅覺靈敏的狗狗來說，探頭吹風就像我們在滑手機看動態一樣，能在短時間內接收大量資訊，是極佳的腦力激盪。",
        "h3": "吹風安全守則",
        "list": [
            "<strong>窗戶高度：</strong> 只能開一條縫，絕對不能讓頭完全伸出去，避免跳車或被異物擊中眼睛。",
            "<strong>戴護目鏡：</strong> 如果可以，幫牠戴上專用護目鏡（Doggles），防止風沙傷眼與白內障惡化。",
            "<strong>鎖上窗戶：</strong> 務必使用兒童安全鎖，避免牠誤觸按鈕夾到脖子。"
        ],
        "story": "牠年輕時最愛把整顆頭伸出去，嘴邊肉被風吹得啪塔啪塔響。現在老了，只把鼻子湊在縫隙處輕輕嗅聞。雖然熱情減退了，但那種對世界好奇的眼神，始終沒變。",
        "observation": "當車子經過海鮮市場時，牠的鼻子抽動得特別快；經過公園時，又會換一種頻率。看著牠鼻翼的開合，我彷彿也能聞到空氣中那些我看不到的故事。",
        "conclusion": "在安全的範圍內，開點窗吧！讓風把世界的精彩帶到牠面前，這是老狗枯燥生活中難得的刺激。"
    },
    "dew-nose.html": {
        "title": "鼻子乾乾的就是生病？觀察鼻頭的健康訊號",
        "category": "每日精選",
        "intro": "「狗狗鼻子濕濕的才是健康」這句話我們從小聽到大。但老狗睡醒時鼻子常乾乾的，這代表牠生病了嗎？",
        "h2": "乾濕之間的秘密",
        "body1": "其實，剛睡醒、運動後或空氣乾燥時，鼻子乾是正常的。但如果長時間乾燥、裂開，甚至有異常分泌物（黃綠色鼻涕），那就要小心了。老狗淚腺與分泌腺退化，鼻子本來就比較容易乾。",
        "h3": "鼻頭保養術",
        "list": [
            "<strong>觀察分泌物：</strong> 清澈水狀通常沒事；黃濃鼻涕可能是感染；單側流鼻血要小心腫瘤。",
            "<strong>補充水分：</strong> 鼻子乾往往是輕微脫水的警訊，想辦法讓牠多喝水。",
            "<strong>塗抹油脂：</strong> 可以塗一點椰子油或凡士林在鼻頭，預防乾裂角化（過度角化在老狗很常見）。"
        ],
        "story": "牠的鼻子以前像黑色的橡皮糖，現在變得像乾枯的柏油路，有時候還會裂開流血。我現在每天幫牠擦凡士林，牠會趁機舔一口。雖然回不去以前的潤澤，但至少不再疼痛。",
        "observation": "每次我幫牠擦鼻子，牠都會打個大噴嚏，噴得我滿臉都是。然後一臉無辜地看著我。這大概是牠對我「騷擾」牠鼻子的無聲抗議吧。",
        "conclusion": "小小的鼻頭，藏著大大的學問。別因為它乾了就驚慌，細心觀察與保養，讓牠的嗅覺雷達永遠靈敏。"
    },
    "slow-walks.html": {
        "title": "聞比走重要：老狗的「嗅聞散步」指南",
        "category": "每日精選",
        "intro": "帶老狗散步，牠走兩步就停下來聞電線桿，一聞就是五分鐘。別急著拉走牠，這對牠來說，比快走十分鐘更有意義。",
        "h2": "嗅聞是狗狗的社交媒體",
        "body1": "透過嗅聞，牠知道誰來過、誰生病了、附近發生了什麼事。這能滿足牠的好奇心，消耗腦力，並帶來極大的滿足感。對關節不好的老狗來說，「Sniffari（嗅聞狩獵）」是最好的運動。",
        "h3": "如何進行嗅聞散步",
        "list": [
            "<strong>讓牠決定路線：</strong> 在安全範圍內，跟著牠的鼻子走，而不是你拉著牠走。",
            "<strong>耐心等待：</strong> 牠停下來聞時，就停下來陪牠，不要催促。給牠足夠的時間讀取訊息。",
            "<strong>放長牽繩：</strong> 使用長牽繩給牠更多自由空間，但要隨時注意周遭安全。"
        ],
        "story": "以前我都覺得散步就是要「走」才有運動到。後來改試著陪牠慢慢聞，原本 10 分鐘的路走了半小時。回家後，牠睡得比平常更熟。原來，心靈的滿足比身體的勞累更讓狗好睡。",
        "observation": "牠聞到某些味道會興奮地扒土，有時候又會小心翼翼地繞過。看著牠認真分析氣味的樣子，覺得牠好像一位正在鑑定的考古學家，專注又迷人。",
        "conclusion": "慢下來，世界更清楚。陪老狗來場慢吞吞的嗅聞散步，你會發現，原來慢活的步調是如此美好。"
    }
}

def rewrite_all_articles():
    count = 0
    # Iterate through all Site 1-5 folders
    for i in range(1, 6):
        site_folder = f"site{i}"
        articles_dir = os.path.join(site_folder, "articles")
        
        if not os.path.exists(articles_dir):
            continue
            
        for filename, data in articles_data.items():
            file_path = os.path.join(articles_dir, filename)
            
            # Only overwrite if file exists in this directory
            # (The articles_data map keys are unique filenames across sites as per original plan)
            if not os.path.exists(file_path):
                continue
            
            # Read original file to preserve <head>, <nav>, <footer>
            with open(file_path, 'r', encoding='utf-8') as f:
                original_html = f.read()
            
            # Construct New Content HTML
            # We will look for the content container. 
            # Different sites have different containers, but we can try to match the part between <nav/header> and <footer>
            # Actually, simplest way is to match everything between <body> and <footer> that constitutes the "main content"
            # But <nav> is inside body.
            
            # Let's build the inner article content block
            new_article_content = f"""
    <h1 style="margin-bottom: 20px;">{data['title']}</h1>
    <div style="color: #666; margin-bottom: 30px; font-size: 0.9rem;">
        <span>發布日期：2023-11-28</span> | <span>分類：{data['category']}</span>
    </div>
    
    <img src="../all_images/{filename.replace('.html', '.webp')}" alt="{data['title']}" style="width: 100%; height: 400px; object-fit: cover; border-radius: 8px; margin-bottom: 30px;" loading="lazy">

    <p>{data['intro']}</p>

    <h2>{data['h2']}</h2>
    
    <p>{data['body1']}</p>
    
    <h3>{data['h3']}</h3>
    <ul>
        {''.join([f'<li>{item}</li>' for item in data['list']])}
    </ul>

    <div style="margin: 30px 0; padding: 20px; border-left: 4px solid #ccc; background: #f9f9f9;">
        <p><strong>關於我們的小故事：</strong><br>{data['story']}</p>
    </div>

    <div class="observation-note">
        <h4>我的小小觀察筆記</h4>
        <p>{data['observation']}</p>
    </div>

    <p>{data['conclusion']}</p>
    
    <div style="margin-top: 30px; font-size: 0.9em; color: #666; border-top: 1px solid #eee; padding-top: 10px;">
        <p>參考資料：本文內容參考了 <a href="https://www.avma.org/" target="_blank" rel="nofollow" style="color: inherit; text-decoration: underline; text-decoration-style: dotted;">美國獸醫協會 (AVMA)</a> 與 <a href="https://www.akc.org/" target="_blank" rel="nofollow" style="color: inherit; text-decoration: underline; text-decoration-style: dotted;">AKC</a> 之照護建議，並結合站長多年照護經驗。如有醫療疑問請務必諮詢獸醫。</p>
    </div>
"""
            
            # Now, inject this into the file.
            # We need to identify where the article content lives.
            # Most sites use <article ...> ... </article> or <div class="container ..."> ... </div>
            # Let's use a regex that captures the middle part.
            
            # Site 1, 2, 4: <article class="container..."> or <div class="container..."> after nav
            # Site 3: <div class="content-card">
            # Site 5: <div style="margin-top:120px...">
            
            # Strategy: Find the MAIN content block using unique markers from previous generations
            # or look for the <h1>...</h1> block and replace surrounding container content?
            # No, replace the whole inner body content is safer to ensure structure.
            
            # Pattern: Find <h1... to the "Reference" or end of article text.
            # But structure varies.
            
            # Robust Strategy:
            # 1. Find the opening tag of the content container.
            # 2. Find the closing tag of the content container.
            # 3. Replace everything inside.
            
            if "site1" in site_folder:
                # <article class="container content-wrapper">
                pattern = r'(<article class="container content-wrapper">)(.*?)(</article>)'
            elif "site2" in site_folder:
                # <div class="article-body"> (we renamed it in previous step) or <div class="container page-container"...>
                # It might be <div class="container page-container" style="...">
                pattern = r'(<div class="container page-container"[^>]*>)(.*?)(<footer)' # Risky to capture till footer?
                # Let's try capturing the start, and we know it ends with </div> before footer or script
                # Actually, let's just use the fact that we know the structure is [NAV] [CONTAINER] [FOOTER]
                # Let's regex replace matching the H1 and all subsequent Ps until footer
                pass 
            
            # Universal Content Replacer: 
            # Look for the first <h1> and the last </div> or </article> before <footer>
            # This is hard with regex.
            
            # Let's try a different approach. We wrote the file, we know the structure.
            # Site 1: <article class="container content-wrapper"> ... </article>
            # Site 2: <div class="container page-container" ...> ... </div> ... <footer>
            # Site 3: <div class="main-wrapper"><div class="content-card"> ... </div></div> ... </body>
            # Site 4: <div class="container page-content" ...> ... </div> ... <footer>
            # Site 5: <div class="container" style="margin-top:120px... > ... </div> ... <footer>
            
            start_marker = ""
            end_marker = ""
            
            if "site1" in site_folder:
                start_marker = '<article class="container content-wrapper">'
                end_marker = '</article>'
            elif "site2" in site_folder:
                start_marker = '<div class="container page-container" style="display:block; max-width:800px; margin:40px auto;">'
                end_marker = '</div>' # This matches the first div close? No.
                # Site 2 structure is tricky. Let's assume the content starts after header.
            elif "site3" in site_folder:
                start_marker = '<div class="main-wrapper"><div class="content-card">'
                end_marker = '</div></div>'
            elif "site4" in site_folder:
                start_marker = '<div class="container page-content" style="padding:60px 20px;">'
                end_marker = '</div>'
            elif "site5" in site_folder:
                start_marker = '<div class="container" style="margin-top:120px; background:#1E1E1E; border:1px solid #333; padding:60px;">'
                end_marker = '</div>'

            if start_marker:
                # Use re.escape for start_marker but we need to be careful about exact string match
                # Let's use regex to find the container tag generally
                
                if "site2" in site_folder:
                    # Specific regex for Site 2
                    regex = r'(<div class="container page-container"[^>]*>)([\s\S]*?)(<script|<footer)'
                    # We replace group 2
                    if re.search(regex, original_html):
                        final_html = re.sub(regex, f'\\1\n{new_article_content}\n</div>\n\\3', original_html, count=1)
                        # Note: we added a </div> because we consumed up to footer, assuming the container closes there.
                        # Actually Site 2 has <div class="container"> ... </div> <script> ... </body>
                        # Let's just verify site 2 structure.
                        # Based on previous read: <div class="container page-container"...> ... </div></div> (double div?)
                        # Let's simply replace everything between <header> and <footer> (excluding nav)
                        # No, that's destructive.
                        pass
                
                # Simplified approach for all:
                # Identify the H1 tag. Replace everything from H1 start to the end of the last paragraph/div before footer.
                
                # Find H1
                h1_match = re.search(r'<h1', original_html)
                if h1_match:
                    # Find the end of the content. Usually before footer or script.
                    footer_match = re.search(r'(<footer|<script src)', original_html)
                    if footer_match:
                        pre_content = original_html[:h1_match.start()]
                        # We need to keep the opening container tag. 
                        # So pre_content should include it.
                        # H1 is usually the first thing inside container.
                        
                        post_content = original_html[footer_match.start():]
                        
                        # We need to close the container div(s).
                        # Site 1: </article>
                        # Site 2: </div>
                        # Site 3: </div></div>
                        # Site 4: </div>
                        # Site 5: </div>
                        
                        closing_tags = "</div>"
                        if "site1" in site_folder: closing_tags = "</article>"
                        if "site3" in site_folder: closing_tags = "</div></div>"
                        
                        full_new_html = pre_content + new_article_content + "\n" + closing_tags + "\n" + post_content
                        
                        # Sanity check: prevent double headers if container text was part of pre_content
                        # (pre_content ends right before h1, so container open tag is safe)
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(full_new_html)
                        count += 1
                        # print(f"Regenerated: {file_path}")
                        continue

            # Fallback if regex/structure fails (shouldn't happen if consistent)
            print(f"Skipped (Structure mismatch): {file_path}")

    print(f"Successfully regenerated {count} articles.")

rewrite_all_articles()

