#Time Exceeded
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        length = len(words)
        result = []
        for i in range(length):
            word1 = words[i]
            for j in list(range(i)) + list(range(i+1, length)):
                word2 = words[j]
                wd = "".join([word1, word2])
                if self.isPalindrome(wd):
                    result.append([i,j])
        return result

    def isPalindrome(self, w):
        length = len(w)
        l = 0
        r = length - 1
        while l < r:
            if w[l] == w[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
"""
Traverse the array, build map. Key is the reversed string, value is index in array (0 based)

Edge case - check if empty string exists. It's interesting that for given words {"a", ""}, it's expected to return two results [0,1] and [1,0]. Since my main logic can cover [0, 1] concatenate("a", ""), so as to cover the other situation concatenate("", "a"), I need to traverse the words array again, find the palindrome word candidate except "" itself, and add pair("", palindrome word) to the final answer.

Main logic part. Partition the word into left and right, and see 1) if there exists a candidate in map equals the left side of current word, and right side of current word is palindrome, so concatenate(current word, candidate) forms a pair: left | right | candidate. 2) same for checking the right side of current word: candidate | left | right.
"""
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        length = len(words)
        m = {}
        for i in range(length):
            m[''.join(reversed(words[i]))] = i

        # edge case: if "" exist, all palindromes to be pair
        if m.get("") is not None:
            for i, word in enumerate(words):
                if i == m.get(""):
                    continue
                if self.isPalindrome(word):
                    ans.append([m[""], i])

        for i, word in enumerate(words):
            for j in range(len(word)):
                left = word[:j]
                right = word[j:]
                if m.get(left) is not None and self.isPalindrome(right) and (m.get(left) != i):
                    ans.append([i, m[left]])
                if m.get(right) is not None and self.isPalindrome(left) and (m.get(right) != i):
                    ans.append([m[right], i])
        return ans

    def isPalindrome(self, w):
        length = len(w)
        l = 0
        r = length - 1
        while l < r:
            if w[l] == w[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

words = ["bat", "tab", "cat"]
words = ["deeabafjjegeajaajjc","head","bg","gfjadiheadidhb","ejhadfdbbf","gfgjjcheijghhbgi","bd","gj","faebidibahheheajhdad","cgfbbijhchgiagdjg","heegfahdei","afajcfbgbjcehjbajgch","fhdgf","fhfbidiehbd","acicifaaiaeda","egdcghfgiede","ihj","aieegchdhjggbaf","ahfaea","bfjjaei","iiahcdbddhhabhfa","fhdhifbhfijfjdhhaec","jjcaab","fgejaeicgcdb","ijeifhfaagbbhbgd","djgbh","bchbghbdhj","ihibdbede","aaieeg","bedidgaijhjffi","cii","bbfiehhaejhaihg","ebcfedjifefhaaich","dbhaebibchdai","gaeeabjeeefeba","feaiahffifhbjbjc","aibficccdgebha","caijihcaijbjdgh","fa","jajdhdgciciabf","jggijggefe","hieagiifgeiggcbda","hbdjhccf","bcifgjid","abidejifhfgagcbj","eie","dhgfcadbgi","ggbdadafdgdjaijbff","aafbefjjich","hhgjffdbhjjce","dccacijd","edaabga","jghcciedjeheecafjafi","hajhfbeade","ai","chehhhjbadd","higihhbia","h","daaffhigihffgib","hdchgcjfhehbdchjbfee","iehahgbd","hhbbhecee","hicchaicbcdcbghgbcb","ggehfjiacca","bicbj","iddagad","egjjajjfijicddghgjbd","fgdj","fdhadabhegefhiaaffj","jjdgd","jigefcbhfbah","fegif","edacai","chchigjif","ihdc","iichejea","ifeahhec","iicb","chhgjifbidccjh","jdbhjffj","dgghdhdhgjh","ggijbj","hac","gabch","acge","ihjdi","afbefigffcgg","jcdghaegagffiaa","fchbdbfgdgihgcbbf","afhehifegdggai","dhejd","bcdjaid","bfhacfgifgfbeiiadbj","cbjaiafefbiaha","fjdggbbdjfhggggi","adadhijfeddcfhcffcf","eebfbhjcfebfbiiii","bddjcheg","bbhbccagghhccbcadii","jjbdjhbi","aadicc","igigjecd","aigg","headbfabhi","aggf","gdibgfgdjf","ddejhdgaie","feigiedidjafibiiabeg","ihejc","dbhjdgceiajac","jgaddec","decf","jeahifda","ei","ceicjagifdajdaggbei","jdfegeagefjjd","ffjgej","abigcgfegii","cbia","ddbccgeiicad","ddjcedidfehhggjifcdc","djahchfjiaabcdfcghc","jd","egfhjgcdabgbijiaif","ebfagijiec","e","i","fdjechdehbg","hibdd","gcdcajhiiahgjebdef","cgebjdfeficigcbajeeg","fegihdbbgceeieja","fcfdeadbfgbg","idgb","feej","caefiaadhaeedfahjjg","gcjhgjajdjbacadiab","ceeahgafc","giidhhaedbhi","gfi","hggigegffeedd","bjaajbdecc","dcegegdigidghbfg","gdaehaagehc","ebcfe","hbihiaehibajbh","dd","chbddebaffaechfiafe","jgdabdhbae","ejffgfdehicgadjaada","ifih","ad","djjdifjgjjhdiaajefae","dfjabaihc","bdbgeefihdc","eijcghaccghehjheiife","hbd","ejhfehagcfdjfjc","gfiejeeeihfhhdfbga","agjiidgihh","gfhfhghccfjjd","ajg","jefebffddehjdgbjhece","jfgbecahdgheeeigbbbd","gcjgeaefb","geacffib","fbabhiag","hcdhdjh","eegaef","cbgd","fajjfgfeafbicic","cfcec","cjidg","c","becfafc","ceaifhebjcihifchccge","acjgbfb","eehfcdibhhdeaahghg","iajh","eh","dcbfgafj","fjfccjjd","jhgiga","cgddbjigg","ifdfhgddebjbhbdebceg","ghaaddiabgc","hhebbhcedi","gjji","hgjaaicfecdbhiaeeejf","ahdfechfgacaadgb","hegdcfffeghfbdaiah","jadegiij","behdhffcedh","jfagjgjabfggdebbgfbj","cffi","ggchfb","gf","afj","gdajgfjdeehcihbcbfc","bha","aifihgjehhji","jhbhagdcbebgedjib","dddgbcdfgcbcfh","bdcccdfiifaigg","eegbjdad","bijfhidcc","jfgdcbgbeidfbich","diacigecbeagij","ae","jeffgeccdjdfhchbfghb","eedjaejjaefdjbgae","jbj","hfajiiadb","ebce","difedbfejcaj","chbg","feidai","gjeihhc","afcbcdi","cgbhhaeahgh","eacejccfigche","iacbfjjag","iibhcgeidba","acjeie","cjejadcdiiiiie","jf","bdaegihihadedjbfjja","bheaefhedifefgcj","gjhehj","igbcedd","iiaebdgegiagi","jghjeghabfba","bddehbggjbgghbc","fbiidhjjg","jgdhhef","djbdcbciijbife","iaiajhjih","gbjcebdacaeg","ijbjjaahedhibjacjid","hfehjb","bfjejdfjedgbdccch","gcie","jbaahgidgbdbcjgccc","hgffjhgagabgdbjij","ecefhcgebh","da","acaajajfahf","gcghhjbiedghj","becgfjdbeicaiihfh","aadhhcjebagabeicjbdh","ieaahaej","g","hfeijjhfbidhbif","efbgbejjhiifbb","ajj","ciabaaadiagfjeaegg","jehcgdbbcdhc","d","fjeefeaffjj","edhb","jdg","bebacedgbjfdf","bhbfbdh","f","ebghcfdjgfdefjdffgdj","hecbeihfhehbgefhc","eibdacjdbha","jfehaibbagj","igaebgbdbjaehegjgdf","cjaiacffcjfadaahjgib","biajafegbgeeagafb","hgdgjcjigjgajfc","icebffehbfbdfb","aiibhdffaiebih","fgiffg","beffciih","eejibbd","dffhajefgibdbhcgjc","jbjbdaide","ihjfg","iga","ficacgiibich","chjehcgdaehb","gjibc","afigghidejad","heghbeddc","iib","dedbec","igdiaachjibbi","jjbdbbdifabdj","hegegcfbchedebgehg","bedhjddaiefgbjhgacb","eefiff","ijgebgdbii","cjffegfdcibgg","dggcacegag","jecaaed","ijffabbe","hhbfgbcaaifbdfii","dbiffejgjhab","bjdi","ibae","fddfacaicjgi","gcccjgdc","ejgbdddacidiejhf","fbebihdgagdcbibd","bdaef","eibbagafbjjcecb","eiihbggfddhaiabjbfb","hgheehaajggfjaij","cjhieife","cajabidhg","fdg","fgch","deggbid","dcbeaehjjige","hhbfjaifgd","geci","ahhfjfdihjjjceabedab","ibghbfdgfebfgdch","deaaachf","eic","dcdd","fgcjiciebcghgdejfj","igiiadcfdfcfiegfiaci","a","j","ciiaggebcdcfgejcjf","jibicii","cae","ejbg","dccagjaadceggh","dbd","hcjicggcjjfgebfgfdee","cjfcbiahajhb","edifbfhhjdaidhg","bhccbajifabehecaibhf","fidjjhecih","ehi","fibgg","hjeibehifibichbibeg","dbeacjdebe","egcg","hedadiidgacfhgh","jfccgcfhfajjbg","fbejjabchbbdcidfce","jb","ificfdf","afhdfefiedhfc","hidc","iaiafehddcg","fifijfjhhddeceeid","ghdecdfdbhdaf","aabafccbdiebjeffg","fhgeagdibbfab","igaighcjfaeffdeg","hfjijbfedbabebiebgd","bibbdbagibbhge","ghgcccdddijeafdbha","fdhfjfbfjhhhiahaeh","hhdbfdechadjbihd","bbaaabbihgc","fdddcgegcfjbdcfeidh","dggich","ebjgcff","fj","cha","ebajffdbj","efeiddggjdidadib","acbjbbah","addeaeaedh","eiehdjdiji","ffcgcghfeeg","eccjeheedecjiihhhj","gejhfcda","abj","fbbcfghghheabej","ijdiegbf","fg","fjgcgecgahhjhh","bcece","jhjidbjddeec","jfjfjfgefhh","eaggijiahffdihc","cfaaciegcefghd","afddbedfg","bigeagdicegh","djedccg","gaeeea","bajegadgii","ejibciihdeabdjbhai","eabhjieafedibcijbjg","aajggcigfhbhj","ccgjah","hfdih","ebgdgcfbeacgf","iibeehje","ibeeedjgdhbidaefa","bidjcijieeh","dahbeaajfeiidgi","dea","ggjigagch","fb","dghh","dbiefbihaieiaffbadc","gdhhf","hfeaicjeecfibhb","jbdahgghge","ebje","edhfbihhgegbhbfbidhh","bejdjjcj","bdjffgjdef","jchgidcff","edhccejjfbchiiabga","cegafghbdbaceiiaab","gddedgeefg","ieff","fgcddedaijahijcab","gichdibdhddh","gabfagfhd","jcfigahdchjaed","ic","dhhcfaajbabaij","hdgdjdce","djhg","eejfbcajhheaghbdaddf","jbajah","chjf","aaij","gagdhiiiacaiagib","hghdea","fedjiiahgiegbaiaibj","ahchacd","cacbddaafgee","cbfahb","fijfjbiecjc","ieddfiahjfaefcdhih","checfbejdhehjeaeaghh","gbiigiajehbghegaideg","bgh"]
words = ["a","b","c","ab","ac","aa"]
words = ["abcd", "dcba", "lls", "s", "sssll"]
words = ["a",""]
words = ["", "a"]

print()
r = Solution().palindromePairs(words)