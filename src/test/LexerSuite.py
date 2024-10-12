import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 1))
        
    def test_2(self):
        """test comments"""
        input = """
        //abcd
        h6 //id
        """
        expect = "h6,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 2))
        
    def test_3(self):
        """test integer"""
        self.assertTrue(TestLexer.test("12345", "12345,<EOF>", 3))
        
    def test_4(self):
        """test float"""
        self.assertTrue(TestLexer.test("123.456", "123.456,<EOF>", 4))
        
    def test_5(self):
        """test string"""
        input = "\"hello world\""
        expect = "hello world,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 5))
        
    def test_6(self):
        """test keyword"""
        input = "int"
        expect = "int,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 6))
        
    def test_7(self):
        """test operators"""
        input = "+ - * / %"
        expect = "+,-,*,/,%,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 7))
        
    def test_8(self):
        """test operators"""
        input = "5 + 3"
        expect = "5,+,3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 8))
        
    def test_9(self):
        """test operators"""
        input = "5 - 3"
        expect = "5,-,3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 9)) 
        
    def test_10(self):
        """test operators"""
        input = "5 * 3"
        expect = "5,*,3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 10))
        
    def test_11(self):
        """test operators"""
        input = "6 / 2"
        expect = "6,/,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 11))
        
    def test_12(self):
        """test operators"""
        input = "7 % 2"
        expect = "7,%,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 12))
        
    def test_13(self):
        """test operators"""
        input = "a == b"
        expect = "a,==,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 13))
        
    def test_14(self):
        """test operators"""
        input = "a = 5"
        expect = "a,=,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 14))
        
    def test_15(self):
        """test operators"""
        input = "a != b"
        expect = "a,!=,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 15))
        
    def test_16(self):
        """test operators"""
        input = "a > b"
        expect = "a,>,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 16))
        
    def test_17(self):
        """test operators"""
        input = "a < b"
        expect = "a,<,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 17))
        
    def test_18(self):
        """test operators"""
        input = "a >= b"
        expect = "a,>=,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 18))
        
    def test_19(self):
        """test operators"""
        input = "a <= b"
        expect = "a,<=,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 19))
        
    def test_20(self):
        """test keyword"""
        input = "break"
        expect = "break,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 20))
        
    def test_21(self):
        """test keyword"""
        input = "auto"
        expect = "auto,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 21))
        
    def test_22(self):
        """test keyword"""
        input = "else"
        expect = "else,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 22))
        
    def test_23(self):
        """test keyword"""
        input = "string"
        expect = "string,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 23))
        
    def test_24(self):
        """test keyword"""
        input = "array"
        expect = "array,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 24))
        
    def test_25(self):
        """test keyword"""
        input = "while"
        expect = "while,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 25))
        
    def test_26(self):
        """test keyword"""
        input = "of"
        expect = "of,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 26))
        
    def test_27(self):
        """test keyword"""
        input = "out"
        expect = "out,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 27))
        
    def test_28(self):
        """test keyword"""
        input = "for"
        expect = "for,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 28))
        
    def test_29(self):
        """test keyword"""
        input = "return"
        expect = "return,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 29))
        
    def test_30(self):
        """test keyword"""
        input = "inherit"
        expect = "inherit,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 30))
        
    def test_31(self):
        """test parentheses"""
        input = "()"
        expect = "(,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 31))
        
    def test_32(self):
        """test curly braces"""
        input = "{}"
        expect = "{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 32))
        
    def test_33(self):
        """test square brackets"""
        input = "[]"
        expect = "[,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 33))
        
    def test_34(self):
        """test semicolon"""
        input = ";"
        expect = ";,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 34))
        
    def test_35(self):
        """test comma"""
        input = ","
        expect = ",,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 35))
        
    def test_36(self):
        """test dot"""
        input = "."
        expect = ".,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 36))
        
    def test_37(self):
        """test colon"""
        input = ":"
        expect = ":,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 37))
        
    def test_38(self):
        """test double quote"""
        input = "\""
        expect = "Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 38))
        
    def test_39(self):
        """test operators"""
        input = """
            + - %
        """
        expect = "+,-,%,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 20))
        
    def test_40(self):
        """test all separators together"""
        input = "(){}[];,."
        expect = "(,),{,},[,],;,,,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 40))
        
    def test_41(self):
        """test error"""
        input = """
            ~~mm
        """
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 41))
        
    def test_42(self):
        """test error"""
        input = """
            >hcmut
        """
        expect = ">,hcmut,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 42))

    def test_43(self):
        """test error"""
        input = """
            #xyz
        """
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 43))
        
    def test_44(self):
        """test error"""
        input = """
            @hik
        """
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 44))
    
    def test_45(self):
        """test error"""
        input = """
            / > >
        """
        expect = "/,>,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 45))
    
    def test_46(self):
        """test error"""
        input = """
            / / 
        """
        expect = "/,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 46))
    
    def test_47(self):
        """test literal"""
        input = """
            9.
        """
        expect = "9.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 47))
    
    def test_48(self):
        """test literal"""
        input = """
            1e
        """
        expect = "1,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 48))
    
    def test_49(self):
        """test literal"""
        input = """
            9. 1__ 17
        """
        expect = "9.,1,__,17,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 49))
    
    def test_50(self):
        """test float"""
        input = "3.14"
        expect = "3.14,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 50))
        
    def test_51(self):
        """test operators"""
        input = """
            :: >= <=
        """
        expect = "::,>=,<=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 51))
        
    def test_52(self):
        """test operators"""
        input = """
            <= ! == = 
        """
        expect = "<=,!,==,=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 52))
        
    def test_53(self):
        """test operators"""
        input = """
            && % /
        """
        expect = "&&,%,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 53))
        
    def test_54(self):
        """test operators"""
        input = """
            && ||
        """
        expect = "&&,||,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 54))
        
    def test_55(self):
        """test illegal escape in string"""
        input = """
            "Another \\y escape"
        """
        expect = "Illegal Escape In String: Another \\y"
        self.assertTrue(TestLexer.test(input, expect, 55))
        
    def test_56(self):
        """test identifiers"""
        input = "a5_ 20 #"
        expect = "a5_,20,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 56))
        
    def test_57(self):
        """test identifiers"""
        input = "am_ 156x 9"
        expect = "am_,156,x,9,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 57))
        
    def test_58(self):
        """test identifiers"""
        input = """
           x__m ad ct
        """
        expect = "x__m,ad,ct,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 58))
        
    def test_59(self):
        """test identifiers"""
        input = """
           =xyn
        """
        expect = "=,xyn,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 59))
        
    def test_60(self):
        """test literal"""
        input = """
            "' \b \\b \\f \\r \\n \\t \\' %"
        """
        expect = "' \b \\b \\f \\r \\n \\t \\' %,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 60))
    
    def test_61(self):
        """test literal"""
        input = """
            "' \b \\b \\f \\r \\n \\t \\' \\" #"
        """
        expect = "' \b \\b \\f \\r \\n \\t \\' \\\" #,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 61))

    def test_62(self):
        """test literal"""
        input = """
            "' \f \t \\b \\f \\r \\n \\t \\' \\" &"
        """
        expect = "' \f \t \\b \\f \\r \\n \\t \\' \\\" &,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 62))
    
    def test_63(self):
        """test literal"""
        input = """
            "' \b \t \\b \\f \\n \\t \\' \\" $"
        """
        expect = "' \b \t \\b \\f \\n \\t \\' \\\" $,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 63))

    def test_64(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\' \\" *"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\' \\\" *,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 64))
    
    def test_65(self):
        """test literal"""
        input = """
            "' \b \f \t \\b \\f \\r \\n \\t \\' \\" &{!@~"
        """
        expect = "' \b \f \t \\b \\f \\r \\n \\t \\' \\\" &{!@~,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 65))
    
    def test_66(self):
        """test literal"""
        input = """
            " abc \n xyz \n \n"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, 66))
    
    def test_67(self):
        """test literal"""
        input = """
            " xyz
            
            123 "
        """
        expect = "Unclosed String:  xyz"
        self.assertTrue(TestLexer.test(input, expect, 67))
    
    def test_68(self):
        """test literal"""
        input = """
            " hello \n \r"
        """
        expect = "Unclosed String:  hello "
        self.assertTrue(TestLexer.test(input, expect, 68))
    
    def test_69(self):
        """test literal"""
        input = """" quybbd """
        expect = "Unclosed String:  quybbd "
        self.assertTrue(TestLexer.test(input, expect, 69))
    
    def test_70(self):
        """test literal"""
        input = """
            " xyz \\8"
        """
        expect = "Illegal Escape In String:  xyz \\8"
        self.assertTrue(TestLexer.test(input, expect, 70))
        
    def test_71(self):
        """test illegal escape in string"""
        input = """
            "Another \\y escape"
        """
        expect = "Illegal Escape In String: Another \\y"
        self.assertTrue(TestLexer.test(input, expect, 71))
        
    def test_72(self):
        """test illegal escape in string"""
        input = """
            "Faulty \\j escape"
        """
        expect = "Illegal Escape In String: Faulty \\j"
        self.assertTrue(TestLexer.test(input, expect, 72))
        
    def test_73(self):
        """test literal"""
        input = """
            2_0e+10 2_0. 1e+
        """
        expect = "20e+10,20.,1,e,+,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 73))
        
    def test_74(self):
        """test literal"""
        input = """
            5_0e+10 4_0. 2e-
        """
        expect = "50e+10,40.,2,e,-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 74))
        
    def test_75(self):
        """test literal"""
        input = """
            1_0e+10 2_0. e0
        """
        expect = "10e+10,20.,e0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 75))
    
    def test_76(self):
        """test literal"""
        input = """
            2_0e+10 8_0. e+2
        """
        expect = "20e+10,80.,e,+,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 76))
        
    def test_77(self):  
        """test illegal escape in string"""
        input = """
            "Error \\p escape"
        """
        expect = "Illegal Escape In String: Error \\p"
        self.assertTrue(TestLexer.test(input, expect, 77))

    def test_78(self):
        """test illegal escape in string"""
        input = """
            "Bad \\z escape"
        """
        expect = "Illegal Escape In String: Bad \\z"
        self.assertTrue(TestLexer.test(input, expect, 78))

    def test_79(self):
        """test literal"""
        input = """
            2_0e+10 1_0. .02
        """
        expect = "20e+10,10.,.,0,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 79))
        
    def test_80(self):
        """test literal"""
        input = """
            3_0.8_3
        """
        expect = "30.8,_3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 80))
        
    def test_81(self):
        """test float array"""
        input = "ARRAY[10] OF FLOAT"
        expect = "ARRAY,[,10,],OF,FLOAT,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))
        
    def test_82(self):
        """test boolean array"""
        input = "ARRAY[2, 4] OF BOOLEAN"
        expect = "ARRAY,[,2,,,4,],OF,BOOLEAN,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 82))

    def test_83(self):
        """test empty string"""
        input = '""'
        expect = ',<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 83))
        
    def test_84(self):
        """test string with escape sequences"""
        input = '"Hello \\n World"'
        expect = 'Hello \\n World,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 84))
        
    def test_85(self):
        """test string"""
        input = '"Hello World"'
        expect = 'Hello World,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 85))
        
    def test_86(self):
        """test literal"""
        input = """
            2_0.e1_1 8
        """
        expect = "20.e1,_1,8,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 86))

    def test_87(self):
        """test literal"""
        input = """
            5_0.e1_8 4
        """
        expect = "50.e1,_8,4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 87))

    def test_88(self):
        """test literal"""
        input = """
            7_00_
        """
        expect = "700,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 88))
        
    def test_89(self):
        """test literal"""
        input = """
            7 14 7_8_910 1_9 1_0_1 14 9
        """
        expect = "7,14,78910,19,101,14,9,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 89))

    def test_90(self):
        """test literal"""
        input = """
            14. __ 2
        """
        expect = "14.,__,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 90))
    
    def test_91(self):
        """test literal"""
        input = """
            9. __ 2 12 _7
        """
        expect = "9.,__,2,12,_7,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 91))
    
    def test_92(self):
        """test literal"""
        input = """
            9. __ 1 1e+10
        """
        expect = "9.,__,1,1e+10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 92))
    
    def test_93(self):
        """test literal"""
        input = """
            9. __ 1 .e10
        """
        expect = "9.,__,1,.e10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 93))
    
    def test_94(self):
        """test literal"""
        input = """
            9. __ 1 e
        """
        expect = "9.,__,1,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 94))
    
    def test_95(self):
        """test literal"""
        input = """
            9. __ 1 _4
        """
        expect = "9.,__,1,_4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 95))

    def test_96(self):
        """test literal"""
        input = """
            9. __ 1 _4_3
        """
        expect = "9.,__,1,_4_3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 96))
    
    def test_97(self):
        """test literal"""
        input = """
            9. __ 1 5__
        """
        expect = "9.,__,1,5,__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 97))
    
    def test_98(self):
        """test literal"""
        input = """
            9. __ 1__
        """
        expect = "9.,__,1,__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 98))
    
    def test_99(self):
        """test literal"""
        input = """
            9._ __ 1
        """
        expect = "9.,_,__,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 99))
    
    def test_100(self):
        """test literal"""
        input = """
            9. __ 1 .e12
        """
        expect = "9.,__,1,.e12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 100))