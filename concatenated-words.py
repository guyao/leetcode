class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        r = self.root
        for i, c in enumerate(word):
            if r.leaves.get(c) is None:
                r.leaves[c] = TrieNode()
            r = r.leaves[c]
            if i == len(word) - 1:
                r.is_string = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        r = self.root
        for c in word:
            if r.leaves.get(c) is None:
                return False
            r = r.leaves[c]
        return True if r.is_string else False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        r = self.root
        for c in prefix:
            if r.leaves.get(c) is None:
                return False
            r = r.leaves[c]
        return True

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        self.ans = set()
        for w in words:
            trie.insert(w)
        for w in words:
            self.dfs(trie, w, 0, 0)
        return list(self.ans)


    def dfs(self, trie, word, pos, depth):
        if pos >= len(word):
            if depth > 1:
                if not word in self.ans:
                    self.ans.add(word)
        else:
            for i in range(pos, len(word)+1):
                if trie.search(word[pos:i]):
                    self.dfs(trie, word, i, depth + 1)

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s = set(words)
        ans = []
        for word in words:
            if not word: continue
            stack = [0]
            seen = {0}
            M = len(word)
            while stack:
                node = stack.pop()
                if node == M:
                    ans.append(word)
                    break
                for j in range(M - node + 1):
                    if word[node:node+j] in s and \
                        node + j not in seen and (node > 0 or node + j != M):
                        stack.append(node+j)
                        seen.add(node+j)
        return ans

t = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
expect = ["catsdogcats","dogcatsdog","ratcatdogcat"]

# Time Exceed
t = ["seemliness","galloper","motorizes","briony","unrazed","exenterating","umiacks","macroglobulinemic","postvocalic","infinity","macroglobulinemia","setulose","resonantly","motorized","spinthariscope","portrayals","discounters","pullouts","waterspouts","barbarousnesses","overelaborations","vaccinated","barouche","beclamoring","infers","mazards","toastiest","forwardest","schnozzles","tragics","chillnesses","dirigible","wists","vaccinates","dateless","anorexies","impeached","ramson","transthoracically","glyceryls","diachronically","ponce","impeaches","sleeper","hazzans","paleopathology","socioeconomically","capitalizing","forwarders","teaware","unlikeness","stounding","ictic","therapeusis","sapogenin","intensifiers","cremated","decrepitude","leftwards","shriving","society","earwitness","connivers","nonconstruction","prosiness","shorans","cremates","coquilles","cablegram","oomiack","anorexics","bonnock","byre","pedalfers","imperturbably","metathetically","quinate","studly","versatile","staidly","gravitationally","overprotectivenesses","centum","roans","advocative","chiton","peccantly","unshielded","dairyings","imperturbable","oomiacs","byrl","meticulousnesses","heterolytic","jostlers","diazo","extinguished","horsepox","satin","postneonatal","gifting","extinguishes","satis","cairngorm","lucently","polysyllable","realizations","extinguisher","behooving","subshrubs","mottled","pongs","byte","osmatic","nonpros","demimonde","slipsoles","witan","mottles","razzamatazzes","valvate","histolysis","schools","semimonthly","kindnesses","noncelebration","cryptorchids","hachure","percolators","mottler","welled","ponds","bestsellers","connivent","trefoil","kibbling","overcivilized","skewing","embarrassedly","brusquer","tautomer","recumbent","roast","dossal","hyperdevelopments","mechanically","cunninger","denaturing","pones","goatherds","publically","legitimised","pyrocatechols","qualmishly","forkless","megadose","sandpaper","apriority","sepaled","turtlenecked","witch","flinkite","gamesome","hawkmoth","deformalizing","infect","legitimises","roars","rhymes","manured","subtrends","tawninesses","helluva","knowledgeableness","octoploid","vandals","wirehair","sated","tribologists","fantabulous","mistranscribed","straits","satem","rhymer","bannock","rhymed","clavate","sates","cudweeds","flatworks","momzers","colter","gobbledygooks","rebooted","sympathectomy","suctioned","adjoins","adjoint","theorization","whiplashes","histolyses","binge","chatted","mistranscribes","manurer","manures","polysyllabic","reinfecting","bingo","paperback","sleeky","hummers","rudeness","sleeks","hencoop","tartlets","neuropsychiatric","subfamily","chatter","hysterectomies","postrecession","pacificism","chattel","regimentals","carryforward","mononucleoses","flatworms","spuriously","expedients","brigantine","micromanipulator","possibility","bettering","cunctations","supergroup","pilotings","trihalomethane","binit","reconstructs","redirects","pacificist","unbefitting","barbarous","detester","franklins","leniences","marshmallow","scampies","daylighting","henlike","incrediblenesses","supply","wherein","cremator","disinclining","recitalist","cauterized","semipornographic","appreciative","codetermination","mundungo","rolfing","perchlorate","autonomically","coagula","wantonnesses","neighborhoods","pommy","wisha","droopiest","scorner","redact","triphenylmethanes","firebricks","lukewarmnesses","dystrophy","patchwork","maxillary","ankerite","reequipping","ventriloquize","untamed","supple","smectic","anarchisms","extravehicular","caterwauled","autoclave","pecorino","grapinesses","tumpline","postmark","pecorini","cruelnesses","strains","metalworks","grotesques","oversleeps","fetuses","ottomans","erupts","preprimary","memorabilia","mononucleosis","mutineering","uncrate","punnets","etudes","lanuginous","nephelinitic","punners","sprinklers","ambassadresses","decolonizing","retardations","attired","weltanschauung","hospitalities","overprints","mournfully","sulphurs","preopening","tsarinas","griping","amphibia","coulomb","dossil","efferents","misally","attires","musclebound","phototoxicity","alehouse","sulphury","bellpulls","indelicateness","sulfonium","cunningly","disaffiliated","immaterialize","licitly","subcategorized","abreacts","pomps","krauts","unable","disaffiliates","rescuing","photoreactivating","tachistoscope","freebee","weakener","ingratiated","cromlechs","weakened","kaffiyehs","subcategorizes","chital","maidenhood","urials","pinfolded","flywheels","wimpinesses","ingratiates","athletes","herbages","meagerly","roughhouses","pecuniary","featurettes","eglantines","wellie","bassists","whereof","photoreactivation","pinnipeds","collateralizing","pepper","ventriloquist","grizzling","unbears","counterintuitive","ventriloquism","crayolas","upwardness","regulus","bullwhips","obviated","caginesses","squooshy","sanatoria","scorned","pestilently","outrivalled","roughhoused","privatizing","nonfarmer","nonselected","supped","dossel","haberdasheries","prepubertal","center","cauterizes","consultative","torsades","supper","dosser","shrimper","dosses","detested","wiser","obviates","wises","mutualistic","cucumbers","heterolysis","nephelinites","pepped","climbable","dossed","shrimped","wised","payably","studio","connectednesses","scamping","sliminess","interlends","limerick","kinetins","didappers","dingbats","uncrazy","freebie","diabetic","nonextant","landlines","payable","wispy","plainclothesmen","ceriphs","hydropowers","cloudbursts","wisps","brutalizations","candelas","ditzes","decimalizations","carrybacks","cyanosis","homoerotic","advocation","flexographies","mislabored","immateriality","roads","novelization","serpentinely","adamantly","rhizoidal","contraptions","undesired","consultation","athletic","centos","typhoids","exertions","jetting","pumice","anarchists","isentropic","whereon","stereopticon","ictus","physicists","roach","iniquitousnesses","thermograms","whitefly","anabaptism","homonym","anticatalyst","dedans","tininess","gripier","centra","interprovincial","impracticable","raincheck","crushproof","ripsnorting","centre","swisses","artels","wrangler","wrangles","niggard","selenates","vorlage","infest","hepatectomy","contrarieties","impracticably","outbawled","comports","hickory","psaltery","priory","wrangled","contradicted","diabetes","subsidizers","psalters","anticreative","priors","therapeuses","esparto","repudiated","copyholders","cyanosed","sassy","attainers","lyard","sidespins","plainclothesman","repudiates","brownnose","nonassociated","inquiets","ultraviolences","anabolic","cyanoses","lyart","hornbeam","delicacies","mitered","besieging","thermograph","energizers","setulous","miscoding","paganizers","cobwebbed","gutty","smutches","ramtil","chitin","satrap","miterer","interrogatives","expedience","marimbist","apoplectic","standardizations","decentring","advocating","warmaker","prologuized","kingbird","expediency","gutsy","penetrate","staider","gutta","prenominations","tetanising","incombustibility","liquidities","prologuizes","resales","smutched","unrounding","grizzlier","grizzlies","nonobvious","whereto","medicinally","couloir","nondisabled","fogdog","reaccedes","penumbral","indiums","chinless","relativizes","unspoilt","equipollences","antitussives","cochampions","gastraea","lyase","diallages","penumbrae","bacteriurias","epitheliums","immaterialism","ponying","reacceded","dekares","redans","immaterialist","wisterias","rabidities","penumbras","prions","relativized","tetchinesses","seasoners","monuron","regionalization","mridangam","cribrous","precessing","diktats","smiler","cubicle","decommissions","smiles","tribesmen","alulae","knuckliest","disutilities","mridangas","pochards","uncharitable","paradoxicalness","counterconvention","heparins","cubicly","shackoes","volery","prunelle","fogbow","borstals","prunella","coappearing","notepapers","penetrant","alular","dissimilating","smiley","endomorphism","gadroonings","sawtimber","branchline","profile","redate","foreordinations","anhingas","revealers","efflux","wadmel","opportunely","honeymoon","brinks","lustfulness","smiled","miscoloring","dilate","outrows","bathetic","census","counterresponse","photochemistries","plainspokennesses","thysanurans","pyelitises","esterifying","wherewith","prodrome","thrived","holking","unchronicled","statedly","westings","extermine","thriven","communicational","diapositives","livingness","pursuivants","thriver","thrives","velum","kidskin","shakable","minored","speediness","apartheid","influents","photometrically","effector","documentarians","escalloping","burgling","carbonaceous","unilaterally","infundibuliform","parashioth","uncharitably","rubbishes","gonads","cabochon","polys","polyp","armorially","cinquain","mistermed","tribesman","megadeals","magdalen","lucres","disjunctively","viscountcy","ruggedized","twitchier","compulsives","brings","piscicultures","glamor","sublimities","mamaliga","haffit","poditic","roadeos","airworthinesses","chairperson","ruggedizes","albatas","eroticizing","impiety","wadmal","routinization","aegis","manque","bloopers","upwards","caftan","tamarin","myalgias","wirra","exculpates","bookbinders","bookbindery","tamaris","influenza","compatriots","premeditate","exculpated","requesting","chromides","commonality","ovulate","gainfulness","gutsinesses","quixotical","corrective","agentry","conveying","delights","hotrods","hagiographers","pushcart","repudiator","subfloors","precession","poetry","prince","knockout","phycocyanins","nailset","endocrines","benefactresses","taxidermists","fellmongers","generalities","unhuman","cuspidor","affectlessnesses","omening","ritzes","glyph","viscounts","fellmongery","gushy","wiggery","demyelinating","viscounty","rationalizing","attitudinize","pyrethroid","knockoff","lightplanes","vaccinations","appreciating","podites","unconvincingnesses","thermotropism","navigation","demyelination","diversifier","personators","diversifies","whereat","whereas","hypersthenes","roband","pomes","bonnie","scalper","notableness","cystine","heeler","appreciation","fourdrinier","begums","broadcasting","chevrons","heeled","awkwardest","hemorrhagic","ovulary","vivers","countertrade","whereby","slowworms","lifelessnesses","sasin","shrouded","sublimenesses","unorthodoxly","briner","outstaring","begulf","brines","pinkroots","scalped","summerlong","sucklings","unstudied","scalpel","muntings","tzarists","twenty","cental","centai","misestimating","brined","wadmol","unquenchable","centas","worldliest","ahistoric","neurologic","robalo","turkois","evaporites","propertylessness","doltishly","jaggheries","unvarnished","ministering","sessional","preoperational","condolence","vacillates","pyrotechnical","lakesides","paretics","megadeath","slushiest","unprofessional","parasailings","vacillated","twitching","frictionlessly","hemorrhages","lathing","minorca","bibbery","sacristans","kibbehs","menswear","proprioceptions","redbay","flavours","hemorrhaged","bonnes","twitchily","ulamas","foaminess","bonnet","oogametes","hardihood","subwaying","tzarisms","beanery","flavoury","rhodamin","glabrous","kinetics","misestimation","plonking","cladode","tenuousness","nonsalable","lulled","noyades","outwearied","lightener","melatonins","slimpsy","turquoise","hypersalivation","nonsense","attitudinise","horsewhipping","metabolizing","kneepan","progestogens","consonancy","inseminations","couthier","bibbers","kneepad","redwares","pomfrets","hooligans","poetic","ordainers","diversified","butterflying","prunello","thumped","capacitors","lewdest","lightened","outwearies","consonance","etymologies","evaporitic","bawdiest","tranquillizers","thumper","disgraced","maledictions","obsoleting","schismatized","mezcals","glands","foreverness","neomycins","blockaded","microspectrophotometer","schismatizes","prepackage","tightening","salivated","blockades","blockader","velar","savvying","sleeps","censer","lapides","salivates","censes","jackboot","vestures","pitilessly","mispronunciations","wires","gleefulness","phenetics","wirer","censed","consistently","despoliations","vestured","sarod","sincere","activisms","lungful","polka","cuspides","binds","velds","veldt","dotting","overstuffs","airworthy","insectivore","vaccinator","boomiest","nonmigrants","saros","roster","shiatsu","glance","reerects","bindi","metestruses","suctional","candidness","rebaited","bines","middle","rudiments","nondestructivenesses","cothurnus","coercivity","polis","etagere","polio","everyday","diary","disgracer","conjuring","disgraces","overmanage","venery","texts","hidebound","toluidines","dottily","etymologize","lecithin","otoliths","littoral","galloots","intercensal","singularities","sarin","saris","gallinule","incepts","pteridologists","radiolabelled","saucing","browbeating","estopping","brickfields","photostated","effecter","sleety","declaims","dermatomal","lobectomy","paraquats","unexpectedness","durned","sleets","modelling","effected","polos","dials","pyrethroids","browband","cubical","cuspidal","micromanage","collaring","endexines","adnexa","retests","forefather","dinginess","wired","maternalism","mandala","polls","enchiladas","hypersthenic","xeroradiographies","anodically","sarks","hatchment","sarky","vacillator","virtuosities","sockeyes","unifilar","outroll","activists","sleepy","binal","navigating","cementums","ultrathin","pestiferousnesses","stablishments","prints","steppers","diphenylhydantoin","incondite","riches","lissomeness","richer","speleologies","richen","unprotected","fractionally","jolliest","viburnum","intuitionist","krater","outpresses","trackmen","corduroying","guildsmen","dobber","flautist","haffet","intuitionism","coneflowers","nonmotile","quadrennials","richly","decomposability","photostatic","kerfing","dermatomes","profits","bragged","outroot","chaetognaths","manicurists","slanginess","desalinize","protectant","cuteys","bragger","chronometer","coulis","hydrochlorothiazides","midden","fridges","galloons","hoofing","outpressed","curveballs","underrunning","personalizes","speleologist","kudo","quotidians","republican","saucily","ecclesiastical","kudu","hocked","lysogenizations","personalized","tallymen","decommissioned","ethnological","dottier","mellophone","hocker","hockey","gusto","swallow","pouching","gusts","purblindnesses","gusty","hemocoel","phosphoglucomutases","salivator","flatfishes","klatches","underutilizing","maquiladora","hexapod","sleeve","restabilizing","censor","rereminding","unarmed","gussy","exenteration","sandbagger","cutest","indissolubilities","debarring","preciosities","trackman","evade","guildsman","outvaunt","sleepinesses","overlooks","smilax","sandbagged","roadrunner","cutesy","midday","flowingly","selfnesses","etymologise","dagwoods","kues","trucing","infrequences","vestural","curtalax","pauperizing","etymologist","shiatzu","pugilist","centiare","pugilism","lecithins","clastics","hebdomads","castanets","cyanotic","reconcilers","lapidated","lapidates","crystallography","tallyman","hexapla","susurrant","meritoriousnesses","prinks","spatialities","einkorns","lallygags","platooning","petulant","martyry","epidemiological","oomiaks","riderships","resaddle","contactees","toad","ministerial","sialic","einsteiniums","impudences","skeeter","chisel","spreadability","martyrs","sialid","diabetologists","ditziest","deductible","dissimilation","leachate","vrooming","monistic","fermion","photosets","aerier","aeries","musicality","desperate","saved","oscinine","syenitic","phytoplanktons","chirps","chirpy","pixieish","elegit","nihilities","nephews","hypersusceptibility","modellers","glossolalias","saves","encyclical","saver","defeminizing","pouchier","tenterhooks","locomotions","haviours","marched","antinovels","gemological","aerify","dealing","toby","inobservant","hydrometallurgies","impetuous","marchen","marcher","marches","aboulias","fantasied","motherlands","razorbill","ultravacuums","phalangeal","earthliness","melamines","tartly","parallax","fantasies","ruderal","steenbok","rarified","phelloderms","simonized","toff","grides","nonunions","wildcatters","rarifies","relubricate","allods","supercriminal","shaftings","broadness","grided","simonizes","toes","assailers","toea","bestrows","euxenites","redrilled","bestrown","tody","objectors","chiros","saucier","diamine","didie","toed","polyesters","predictions","coassisting","theorematic","aeried","aperture","cerises","invalids","limpkin","slipways","organometallics","squalidness","microspectrophotometry","finickinesses","diamins","rockiest","tods","postfeminist","kelping","damnation","deliverance","pictorialize","sublated","emollients","asthenies","beatification","cyanohydrin","limnologists","satori","couthest","squirmier","extrudability","togs","vouchsafements","cofounders","arginine","kune","fimbles","prostatitis","titivated","fitness","anoxemias","layers","pinatas","evasiveness","leching","fogeys","replacements","agglutinins","dobbin","coulee","toga","commodiously","attributable","cutely","semicrystalline","piezometric","titivates","wrote","acetifications","biotas","blazer","wroth","blazes","bazars","chebecs","chirms","kuna","flyleaf","blazed","sturgeons","syenites","tofu","toft","turtler","plating","sanicle","turtles","nightless","phasing","visionally","breakdown","renailing","choriamb","ritardando","gonocytes","veneer","workfares","toit","entomophagous","fancifulnesses","syllabically","asswages","turtled","platina","popes","computerising","corruptively","tollbooths","extrudable","toil","totemists","hippogriffs","perfusate","petrifying","chirks","asswaged","lungworts","tomahawked","falsifiable","selvedge","nonmoral","musicalise","nettling","uprightly","sublates","thermopile","tzaritza","acacia","superrace","furnacing","puzzlingly","bottomlands","deacons","procrastinator","bestrewed","foremilk","dicier","tole","reenjoying","told","tola","bipod","noctuids","toll","asthenias","effectualnesses","bioregional","lowlands","luxuriant","ausubos","splotchy","kuru","hyracoids","nether","tarter","toke","philander","cottages","minimills","cottagey","wives","anatase","chivalrousness","transfinite","jemmying","wiver","exhaustibilities","isopodans","tarted","ritziness","mezuzoth","inconsecutive","munchkin","cardoons","wived","markedness","tong","ballyragging","polysorbate","tone","asthenics","chariest","savor","stramonies","savoy","phenolphthaleins","cottager","disinfestant","ditheists","incriminate","toms","coronation","inflictive","abstrict","beachfront","coronating","bromegrass","tome","unselling","tomb","blockages","estrins","minuteness","outroar","estriol","phrenologist","cellarette","tolu","anchor","gadroon","genically","commissariats","olympiad","topi","toph","tope","tops","blatancy","chronometry","aerial","megacorporations","savin","underreacting","wiretapper","attornments","enhancements","toot","squirming","biotoxin","regrants","fastball","retransformations","uprighted","reflexivity","unfashionably","comeuppances","wiretapped","outrock","took","juggle","zymogens","toon","tool","toom","unfashionable","alcaydes","cyclotrons","saxhorns","tony","unimpaired","stimulating","tons","foredoom","catafalques","textbookish","snivelling","ditheisms","headfish","boundary","clupeids","torn","mandate","rescaling","zayins","tori","totalitarianized","fermium","inactivate","tors","tort","vasotocin","torr","toro","unmooring","seizable","chirrs","reoffers","tore","zymogene","torc","anaphylactic","chirre","totalitarianizes","tora","elicitors","outrode","stimulation","brinies","brinier","homologically","fantasise","hawkishness","foredone","specific","scowdering","fenceless","obtains","consecrating","paresthesia","fantasist","viciousness","togate","topwork","comedown","entails","developments","unaired","shrillnesses","biaxial","panatela","phalangers","impairing","consecration","tots","poops","verbiles","bootlegs","inhalers","elective","saute","tote","minoxidil","grewsomest","nonarbitrariness","underutilization","canopied","hypercompetitive","pliably","reincarnates","lungers","chiral","intrigues","nebuly","roorbachs","tosh","intriguer","spearman","swivelling","quinces","tost","toss","bethanks","confound","swallowtail","swelteringly","nebule","abhenries","revanchisms","stonefish","durocs","tory","reglues","reincarnated","granules","handcuffing","regrowths","supplying","outwatching","pathologists","pliable","dicing","shmoozing","caldarium","intromitter","needlework","drawbar","endometritis","forelands","obeyer","poons","reverberative","nebula","brinish","prodigious","schoolmasters","sedatest","intromitted","conveyers","cytosine","vendor","withdrawable","obeyed","paleways","quicksand","xanthins","libeled","patisseries","tout","upholder","libelee","tour","cochairmen","adonises","adoptions","xanthine","appurtenant","amanitin","humoristic","blazon","parhelion","syntactically","wanderlusts","libeler","oligopsony","subblock","yairds","concenters","rewinds","roorbacks","towelled","salariats","scaramouches","granular","platitudinizes","endomorphies","geoscientist","didst","alleviators","nutwood","unperson","cystocarp","subsociety","avaunt","tartar","poove","tows","tartan","town","luxuriate","hominians","towy","fucoidal","dicrotism","untaken","indefatigablenesses","succedent","templets","lathier","platitudinized","auxotrophies","phrenologies","centiares","orfrays","reglued","avirulent","shivered","trifluralin","malangas","trisceles","jugged","gasholder","detonated","sorrower","canopies","intrigued","apostasies","shiverer","cascabels","slatternliness","clamminesses","totemites","detonates","poori","crayoned","sorrowed","stockbreeders","noninterventionist","election","toys","backstitches","doublures","foredoes","toyo","unnewsworthy","brining","fluently","vendue","saury","kvas","necessaries","greatcoats","nonpoor","pitiful","disinvesting","exurbanite","consecrative","thusly","euthyroid","sunderers","sorcerer","detonator","kelpies","colorfully","noncomparability","vender","withheld","babysit","didos","bedeviling","backstitched","pemmican","paunchiness","transfixt","reedier","vended","vendee","palimony","brunching","lamination","deportees","mimeograph","ochlocrat","sheepherdings","streamiest","browbeat","outwitting","reedify","wonderfulnesses","coshering","miscoins","lixivia","reverberation","diamide","sponsion","piercings","amphibrachic","encrimsons","hospitalizes","balkanizations","laminating","appendant","auxetics","hospitalized","counterrevolution","stubby","dourness","pipages","stramonium","reverberating","mutationally","immaterial","venturesome","honorific","hoddens","acronym","reteamed","nondurable","revanchists","bearhugs","yoghourt","fusiliers","wrong","epiderm","tranquillizing","rechoreographing","incredulous","monarchical","griseofulvin","quadricepses","kainit","unhandsomely","unyeaned","reclaims","undercools","inimitableness","stoichiometrically","schizophrenic","declassifying","schizophrenia","respells","bootless","troubleshoots","witney","flannelette","languidness","quinaries","spearmen","spinsterly","multiprocessors","esemplastic","sedately","zaddick","reorganizers","biotin","monovular","inwards","inflight","resighted","acerolas","biotic","enthalpies","overhaul","shekels","impotences","globally","imprisonment","hugeous","sterilant","fantasias","subtler","necessarily","rocky","experimentalism","desacralizing","cochairman","rocks","parallel","platier","staggerbushes","prevocational","platies","incorporable","musicalize","desperado","garrulously","experimentalist","trichologists","aegises","letterheads","zapper","whalebones","ruggednesses","tarsus","schizophrenes","technocratic","meitneriums","chopines","zapped","nettlier","dicey","corrosiveness","inhabitants","brins","untested","horseman","bring","rheumatology","brine","detestations","sauce","brink","indistinctive","reeding","sauch","emboweling","crossword","jingling","mattoid","ossific","robot","grigris","mawing","bivouac","umbrageous","yammerer","dicer","fairlead","paddleboard","cocksuckers","dices","lobulations","saucy","departing","navette","coalless","retrodict","superheavy","overengineer","furnisher","meiotically","snathes","brios","furnishes","barometers","overhard","diced","gunnels","upstate","vociferator","trucker","automaker","contrivers","ragtops","redstart","bedwetters","briny","novation","refiring","deletes","trucked","upstart","moonlike","ordering","heterodox","irredeemably","verdure","monotonousnesses","chartists","duckwalks","rebaptisms","barbequed","furnished","rudesby","scriptoria","plasmagel","pentanol","typescript","niggers","barbeques","cytosol","infusibility","irredeemable","trapeze","undescribable","recapped","appendage","bantered","banterer","inconcinnities","reobserve","overhate","unpuckers","yammered","obligated","deleted","spaying","cavorter","maturating","upstare","webbier","venerability","carpophores","obligates","sillier","sanctity","sillies","mesmerizers","sforzandi","poods","xanthomata","devolutionists","horsemen","insignia","bedight","cavorted","fiddling","lightness","schorls","garotes","presumed","sforzando","recompense","shavetails","upheaving","ceaselessly","preinaugural","underbidder","punnier","rappelled","undersigned","lungees","presumes","airpowers","antiphonal","derivatizations","presumer","beneficiaries","guitarist","marinading","radiophotos","ruthenic","arbour","macadamizing","superovulations","biflagellate","hyperinsulinism","rhumbas","ricers","crabbed","micropaleontologists","coeducations","crabber","mediastinal","unidimensionality","tacnodes","ventriloquies","bullous","assemblers","burbots","gibbering","backpacking","radioelements","uprear","xebec","shunters","garoted","lustinesses","venue","brill","marginalities","snowscape","grappling","liveability","overhand","burking","overhang","arrestors","sanction","domiciles","manors","dutiful","skywalks","disrupts","oboes","biota","carbureted","limpidities","sunscalds","brims","peperomias","syncopative","domiciled","vertexes","fiendishly","anthranilate","pooch","vents","cheapened","foulards","gothically","upstand","reedily","ramrod","cercises","impressibilities","vitesse","lordless","polyembryonies","arbors","poohs","cratches","pentanes","electing","burkite","milliliter","embrutes","malmier","misaims","stingiest","gimbaled","brier","jinglier","bries","sillily","swooning","acetylcholinesterases","alloys","inquirers","minxish","sextillion","putsches","literally","symbolists","sailboating","sauls","sault","stiffnesses","overlords","traumatized","oboli","perspicuousnesses","biome","ventriloquial","branchiopods","monosyllables","monkeyshines","extraterritorial","obole","trunkful","sabulous","pertinacity","poofs","gonorrhea","patchers","gibberish","vitalizes","lexicography","garotte","tillandsias","athwartships","appositely","floodlit","biont","sauna","shatterproof","skivvy","duchies","brigs","coatimundis","divvies","hyperfastidious","motorcaded","webbing","amanitas","motorcades","avatar","generally","divvied","attaining","oversupped","pylori","poofy","thermotactic","vitalized","heterolyses","erasure","chatterer","gazumping","bribe","inertnesses","pools","resummons","saugh","deuteragonists","briar","brotherhood","maturation","kallikrein","siphonophore","relentless","chattered","lensing","superconducting","punning","nightclub","bedrail","posttransfusion","carburetor","conines","obligatos","flagellated","glissaders","jettied","misstyle","bladdernut","decameters","mismanaging","wrench","formatively","feeblemindedly","interlunary","flagellates","lycea","distasted","jetties","incriminatory","lycee","preparatorily","jettier","professorate","algebraic","bride","mucopeptide","traumatizes","menageries","beautifulnesses","distastes","editorializing","reedits","sledge","obols","doggoning","underdeveloped","victimization","appreciativenesses","disroot","veejay","syncopation","resorptions"]
#expect []

r = Solution().findAllConcatenatedWordsInADict(t)
print(r)