#Time Exceeded
"""
class Solution(object):
    def exist(self, board, word):
        import copy
        self.q = []
        self.width = len(board[0])
        self.height = len(board)
        for i in range(len(board)):
            board[i] = list(board[i])
        ans = False
        if self.width == 0 or self.height == 0:
            return False

        for i in range(self.height):
            for j in range(self.width):
                l = len(board[i][j])
                wdc = word[:l]
                if board[i][j] == wdc:
                    self.q.append((i,j,word[l:]))
        while self.q:
            x, y, w = self.q.pop()
            b = copy.deepcopy(board)
            b[x][y] = None
            if not w:
                ans = ans or True
            ans = ans or \
            self.find_sorrundings(x+1, y, b, w) or \
            self.find_sorrundings(x-1, y, b, w) or \
            self.find_sorrundings(x, y+1, b, w) or \
            self.find_sorrundings(x, y-1, b, w)
        return ans

    def find_sorrundings(self, x, y, board, word):
        # b = board.copy()
        import copy
        b = copy.deepcopy(board)
        if not word:
            return True
        if 0 <= x < self.height and 0 <= y < self.width and \
            b[x][y] is not None:
            l = len(board[x][y])
            if len(word) >= l:
                # print(x, y, board, word)
                if word[:l] == board[x][y]:
                    b[x][y] = None
                    return \
                    self.find_sorrundings(x+1, y, b, word[l:]) or \
                    self.find_sorrundings(x-1, y, b, word[l:]) or \
                    self.find_sorrundings(x, y+1, b, word[l:]) or \
                    self.find_sorrundings(x, y-1, b, word[l:])
        return False
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existRecu(board, word, 0, i, j, visited):
                    return True
        return False
    def existRecu(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True
        if i < 0 or i >=len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False
        visited[i][j] = True
        result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i - 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i, j + 1, visited) or\
                 self.existRecu(board, word, cur + 1, i, j - 1, visited)         
        visited[i][j] = False
        
        return result


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
word = "SEE"
word = "ABCB"

board = ["aa"]
word = "aa"

board = ["ABCE","SFCS","ADEE"]
word = "ABCCED"

board = ["ABCE","SFES","ADEE"]
word = "ABCESEEEFS"
# board = ["aa"]
# word = "aaa"

board = ["pfhnuvuzzpujstpivosmqlctynsputylyiaufutfjnqdjfnevftotvhticjevjrvrrpxl","kewzubibppwwikpdulnwusrdjoxbdwopalowoxxdotcwgrzaeowygpesddvizjzbwnxlm","uqanswtmxvqorruixonajvbvuctkzgwtxzirxedxzwltphbmwpmhmncjpwvqctjbsttsx","ypxwcqljtxfklpxarirpdhuwsxpmqjjryinaabluytekidkblerolnnekeqdnbulkjnkk","ygltlxbqhdclwszjfftjvwwysjkeyxqxdbqqyuhixlvvduelbzwwytxqehwdenckquarq","jznuwiatonuojtmeqejzbogqsqimszdcysyvdaqrnkhxdtdtyovbcbtwrbjlbonbioynq","ohezodciiyixvlbweypfjagxqihegvuvcawsfacoyklvvmrbkghthnsxxcdexzbbcxthx","wxyiitgxnhjtqfcgxbdbejygmbilxrjvpjfzelwtvinlnrtmtxoziofvqngnfrkwcpvhd","scycplpjhbcepbmehhwwqldhvzkkvtnpvnrnbgwijyozbcfkmbhcmkjjmvthojykyrzbx","vjivzjycojorqqfcbooxixltvxrowtntewqefpgwywnqotuphjmriakgzcuyxitbekflz","nhzjvpzqlpxwdpffbnfdhfarycxijjjzqiknzkdlzdhesoktbpzlubcufadrloqbzarak","unlxxqrlanproanpehvemmpbetcekcrgqegnwxaympparcqwmnaybsbfndlxgcfwjllfj","levdvwuyoqmbtkclmjaruxxxeviqinbutwxpurpkkdndnrqbaqtvpsutqcjyrksnjrefl","vsvyfanxspxikuzeouusgtmqnzbffjqabnygpnfhcfrozqtokniqiujwvmbavtayiahxo","mesrvjrnchxrrqambwjnzklsmjcpszfffxycgrrkaqesgeghcpvbbivqrxfmykrfjrhsj","aejqidxmjgqbbreloufnzrllisxbbpkbtwscbpqnvhozaskpnpcoiqcqizskoeljcfleu","crslhtlbfaqxfffvhyfgsrwwffbktfhxybifutgbwxybeeyleftwxrucyvorcvoayyfss","ouqlutparcewxcvqxxouogxjwxivfcptyfgvyxvrbcpyelobkeyykvkjuuezytuxaauax","ptytiyytobetzefuoopksqjnlipncpntilntmlocmuvozdiprzamsjbfrrstifmttbmfm","ahbxfpwizlbblptwrynkqisyxnrybynehobodxyekafypyuiykspsnpragqegdintleyi","ccucisuinchxvyrinjktzobeyqxjuvtxxobhgvqvyxuvxmfkvpfwggaewzotuhqtxrben","tbnswkpipzfggbmmdtkchdwqtrqnuwcnxphtzwdqxiwdjjrmccolfmdbgtqapsqpjxikw","matuwzghqslujycvefbzvernugyrqinekjziihsazdviexgicjjznaohimzzwodgxeqhl","iknofvsedcinnjaoxkyjlxfbdnbjdixoskczhwflapanycdvmcgzblbgacqgknufxyggu","orudrjcunzirgiutjbultcxgwefullqzfmewvgskgbdojyhuzdfsfeabjfxuspvxbzwzi","olqrpecnnwordgwiiarpznhpkhsldtvtfnlurnjhmxypfuznwscwhlnrshfvbapiocchp","nodmovrlughnifutsooatjdvallcptucjzoyuhjpnsexyyssogujsxfuiqxxltbxsrxny","ienaimaihtxnnghllcvebvrwwooqldqtjewrswazrzpffwstapxbkqxjfozstpodvkwog","ypaxefddzydoxhbngkuwjnqybvwlrktsbtpgaulbsqqpxrdedxammsmnniahuwbwpqesl","rtdhlvfealhzlvmgibvscenyflpwphjgdonojuvlfcltyxziyuaczpagaqcrzlzccptlj","oxpskkshjahfbkgsmntcrkcfkghzzukntzgdlymwzwccikwuzpxrabwmhflhzxwvxcykd","nhejjirvelvukmwnkivrvessanrfocibjmkuudpyomsbyookyldtrwmujfzxhjysvkopn","epeskftavdzjhsafgwomvoveoobzesmiisdsxwuvzteiognudeiysgfgwghabwljoodmk","zhjtnuhtjdwnoxhucqqkxqntbwkpbwzbflwuhfnqikgwjpqnfgxfzlaajksnitqpeojnt","xgbjmaubqhjzeqyrqadbusloibuwkirjosucsoflvokcektxmyahqlvamryzbpkpiftcv","znrpzvwjqtypvfhgcivtgwxwgogniijjwcyxxwhprhemmmtquqlcmiysxeifprqnvokun","rjeyormcmeyeqaqabkxhsewlujgluaynkeoavcejhcnzedzhqxpidnwazcltflirpyrnb","xwkzmjfrknhjesnropqqalvnuoeufrxcqhdcsltdybmctbvjqmzsxxhtlmqtdnxvxdxro","tuowjsrmnafzzxzyhumtmhyaguzltqzmnpiwhzkvzpwbpxbwunrgwpidjhodyqrlfajpz","vkbliecgfaavririrwuynzyfqjmqubsqlvdwzhcgjebcmvkdtgegfclyoaqibkapfflgo","nnxtobflmjfunlarzyfzqqcbsrgacnoraokqpqcdbhyquahvanwqfzrxsaxvnoopczhrr","lxsuvkpxrmxglpnkhlchkzwyonanuuggraaokrndgkkrzxbikfrvfnvvaykxuqdnqfbaz","odfapybpbmbgdynruktsuqmkvzcdcecskjubhxqkjusnsigmszgnqsznteqxispsdlumj","mwsgphzxnnrpugfogsikjhudznhkjvtvsocjvdglqzakghzmzjykqsqrhzcquxmmlqvjt","dujduwjbvxcgxpyrfqzgspardpdtkooqiyteuehrdlzaaxrhnqnhiqbnfgjruxhexciti","rmlcllfjfmyxcihujvzpeqjbanbcxulojysumxfrmeoqmwkvtjmxbvabkdgjatzjrrddp","jwbnnrblbyemkbphdtthzchubqnsvrjepktcdwngwruiukpadkheoqypilkdetkugdylc","muyfohcyycbjlhxbfpjtbmxuytccsqggkenynpzmtaxeiufplqimfgjdbnhtdnbpupohg","nvapsezpmraeznjhypjlwermiggzwpfllhbdmcsatvevkqcifnvdumpcvxbrnifyqgdek","ygetmzfcdnjrknnzcpwcsnpaupscswnsetlruqtxfdqssdrwunymcppxehzzgorkhfbbv","xbdarxuvoqpdrehgtglaimiwdteiuhgriltaipxygodzukfntsqbeyxktdsqnahvldxts","wtalwzhjhvczndgncqjgizvjiqwlosgmlixkkhtrevsraygcopkzqfkzyimmasymdywnh","relmweoxkqncdmskytihgwhaxvdxtqekwpyvvosfhfjkueuuxfbdbleaijxeadqyuptpd","nvmvgwpktlkapnbctekdbofhfdbwzrbmoohumyhhkrhzgldapnfsekzlpbjoumdickepl","lwxeeylrbngqsaucahtdqixdlhfxlwkxvhbbfosibaztavxadrfvbeymlglxewuzfxcnm","uvpuwjxsixvzfqajrovzcsfyohfnjsbgqrcmazeixbkesmnldimfcrfsykgifhovyshas","mlrpvvjjiumtirxayqajwiofylersgjgrawoxfyfckakeymcqnnoxdtwozpjgapxcnmzt","mgxwjhcjufzjsngyicmitvqvnnzabavnjsmscobytchopnoxschnyxjnnknqlleudsmhg","pfcrosicghwipjiouvbfluqwykbsylynsaghuolavhlmqtbnreseyicyufquqrjjtpsof","doakbpcvqpowjuxtwvpbojufudyjvmqadtkeiobagrwpltlhralhkfmgkmqhzihebtkjj","ojrfihtduawundgupneefndnwjpptabhmspubizvkwsybystnzxsocillzcezdonwdjzl","jvvhnvknqdbpavdefopgrwiwmvspfscqpzzevjrlnucpsfuxwjephmltjgkoamgpmftjp","muchwtzdnybzeqgsecckmskzzbneuwvgszpototipvhtnqorsqdekpdlqsqkontgniwgz","sqonyjcozwipzmcpsnhkfsztnhiveqwwgmleypuxlepnrrelenvmfwfugnskdoijbvqbm","myarnpkgtvngszopgkvtchyrrjuobxaovahlprrkoetgfjxltugwdgpwqlktilhflqqdj","knxoggwpfhlcojfuycmlogvzpangtqrdfrtoxpfexqgnzmjzqwkeehgtivbbnvgsmzglp","opoewbgkkfaisgobokjjnmwisruuxfjnvxutaadmhfxbnldcvonjdkrxboravcosbilbk","qqrvnvjyynuoafrmwppmgqijgakqooceevcrqnrqalfcswppnedwwlfeorwefyilukckx","udzhicagtrwzusyixeyqbcybmjvzoiyilarvetdxkzyhryrqdrjgvhhhqdienjoajixnb","ammckvvjmmodxuyebhwgsbtbrvkzszdtlpxxmsiagwfdsdjumgcejyhattcosfjfwgdiy","nkhmpkeuuagafnjdwlyqnmiuvqqdtacikjubvbvrberirclnqmffyoaweszzvdjhoejmh","edikxtbzerrswxtmzpsrqtowdwmjhyqncaybtbcauustrnhsealxvatayhlhgdukeslzw","nbqjwjcjruotglqigrinepvijhoeunairstncwyvsoqabgihzsxehuotccxwrzgiraxvy","yqqmgropbxouuubpiwrktpcuwmmykjwiaowifkxjiodeigtrdmbycftashyeqwoskkdsv","abfogjzmfqprrovzjxrqvvitjbgveysgbxxhjwtomlhfbdekaxcysktdnzbrztaarxhcv","dqjqxorcvddshdnrwsfwtyxnaygxhiumydcxstapyfhfiwzgpgcigaxhadghnbwneylyu","nnssxactzikfntnpsupwbylcuzivmhpzwjttjvpkfzrsufhnzylczwetxpojwfkupfoaa","fliecazhkojizlhvsdvjtefzrbqwrqzwbhbghcptqacrmjogojpiqwjhxzdppentlozvs","qokrsbfcqlsbcarajyzieoaietwsurnkhxdabietvwuzzmzimztqptbtoxoiqduxcazdi","dygctfbhhjtgemxxntnkjxcmsbqsbucguiinqjuxvqfzcczrxmdikfuegnyhhcqblyrdk"]
word = "afdfghjhy"
r = Solution().exist(board, word)