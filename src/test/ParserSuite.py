import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    
    def test_101(self):
        """test variable"""
        input = "x : float;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))

    def test_102(self):
        """test variable"""
        input = """
        x, y : float; 
            e : integer;
            x : float
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 102))

    def test_103(self):
        """test variable"""
        input = """
           x, m : integer; 
            b : string;
            e : boolean;
            a : integer
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 103))

    def test_104(self):
        """test variable"""
        input = """
            a, x, m : float; 
            a, :float;
            a : integer
        """
        expect = "Error on line 3 col 15: :"
        self.assertTrue(TestParser.test(input, expect, 104))

    def test_105(self):
        """test variable"""
        input = """
            x, y, z;
        """
        expect = "Error on line 2 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 105))
    
    def test_106(self):
        """test variable"""
        input = """
            f : array [1] of integer;
            g : array [1, 2] of float;
            h, m, k : array [1, 3] of boolean;
            j : array [1, 3] of integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 106))

    def test_107(self):
        """test variable"""
        input = """
            a b c : integer;
        """
        expect = "Error on line 2 col 14: b"
        self.assertTrue(TestParser.test(input, expect, 107))

    def test_108(self):
        """test variable"""
        input = """
            a, b, c : ;
        """
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 108))

    def test_109(self):
        """test variable"""
        input = """
            a, b, a : integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 109))

    def test_110(self):
        """test variable"""
        input = """
            x, y, z, : float;;
        """
        expect = "Error on line 2 col 21: :"
        self.assertTrue(TestParser.test(input, expect, 110))
    def test_111(self):
        """test variable"""
        input = """
            1x, y, z : float;
        """
        expect = "Error on line 2 col 12: 1"
        self.assertTrue(TestParser.test(input, expect, 111))

    def test_112(self):
        """test variable"""
        input = """
            a, b, c integer;
        """
        expect = "Error on line 2 col 20: integer"
        self.assertTrue(TestParser.test(input, expect, 112))
    
    def test_113(self):
        """test variable"""
        input = """
            a : array [true] of auto;
        """
        expect = "Error on line 2 col 23: true"
        self.assertTrue(TestParser.test(input, expect, 113))
    
    def test_114(self):
        """test variable"""
        input = """
            a : array [1+8] of float;
        """
        expect = "Error on line 2 col 24: +"
        self.assertTrue(TestParser.test(input, expect, 114))

    def test_115(self):
        """test variable"""
        input = """
            a : array [1-7] of float;
        """
        expect = "Error on line 2 col 24: -"
        self.assertTrue(TestParser.test(input, expect, 115))
    
    def test_116(self):
        """test variable"""
        input = """
            a : array [1/1.5] of boolean;
        """
        expect = "Error on line 2 col 24: /"
        self.assertTrue(TestParser.test(input, expect, 116))

    def test_117(self):
        """test variable"""
        input = """
            a : array [1%8] of integer;
        """
        expect = "Error on line 2 col 24: %"
        self.assertTrue(TestParser.test(input, expect, 117))
    
    def test_118(self):
        """test variable"""
        input = """
            a : array [1==2] of auto;
        """
        expect = "Error on line 2 col 24: =="
        self.assertTrue(TestParser.test(input, expect, 118))

    def test_119(self):
        """test variable"""
        input = """
            a : array [1e-2] of string;
        """
        expect = "Error on line 2 col 23: 1e-2"
        self.assertTrue(TestParser.test(input, expect, 119))

    def test_120(self):
        """test variable"""
        input = """
            f : integer = 1;
            x, y : integer = 1, 2;
            a, b, c, d : array [1] of float  = 1, 2, 3, 4;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 120))

    def test_121(self):
        """test variable"""
        input = """
            f : integer = 1;
            x, y : integer = 1, 2, 8
            a, b, c, d : array [1] of float  = 1, 2, 3, 4;
        """
        expect = "Error on line 3 col 33: ,"
        self.assertTrue(TestParser.test(input, expect, 121))
    
    def test_122(self):
        """test variable"""
        input = """
            x, y : float = 1.2;
        """
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 122))

    def test_123(self):
        """test variable"""
        input = """
            arr : array [3] of integer = 1 + 2, 2, 5 * 6;
        """
        expect = "Error on line 2 col 46: ,"
        self.assertTrue(TestParser.test(input, expect, 123))

    def test_124(self):
        """test variable"""
        input = """
            x : float = 1.0 + 2.5;
            y, z : integer = 10 - 5, 2 * 3;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 124))
    
    def test_125(self):
        """test variable"""
        input = """
            for : integer = 2;
        """
        expect = "Error on line 2 col 12: for"
        self.assertTrue(TestParser.test(input, expect, 125))
    
    def test_126(self):
        """test variable"""
        input = """
            x : auto = boolean;
        """
        expect = "Error on line 2 col 23: boolean"
        self.assertTrue(TestParser.test(input, expect, 126))
    
    def test_127(self):
        """test variable"""
        input = """
            x : string = "Hello";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 127))

    def test_128(self):
        """test variable"""
        input = """
            a : boolean = ;
        """
        expect = "Error on line 2 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 128))
    
    def test_129(self):
        """test variable"""
        input = """
            flag : boolean = true and false;
        """
        expect = "Error on line 2 col 34: and"
        self.assertTrue(TestParser.test(input, expect, 129))
    
    def test_130(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 130))
    
    def test_131(self):
        """test function"""
        input = """
            foo : function break (inherit out id : auto) inherit foo1 {}
            foo : function integer (inherit id : float, out id : boolean) {}
        """
        expect = "Error on line 2 col 27: break"
        self.assertTrue(TestParser.test(input, expect, 131))
    
    def test_132(self):
        """test function"""
        input = """
            foo : function () {}
        """
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 132))

    def test_133(self):
        """test function"""
        input = """
            foo : function integer (x : float, y : boolean) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 133))
    
    def test_134(self):
        """test function"""
        input = """
            function : auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 134))
    
    def test_135(self):
        """test function"""
        input = """
            foo1 : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 135))

    def test_136(self):
        """test function"""
        input = """
            of : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: of"
        self.assertTrue(TestParser.test(input, expect, 136))

    def test_137(self):
        """test function"""
        input = """
            true : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: true"
        self.assertTrue(TestParser.test(input, expect, 137))

    def test_138(self):
        """test function"""
        input = """
            foo : function array (out inherit id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 33: ("
        self.assertTrue(TestParser.test(input, expect, 138))
    
    def test_139(self):
        input = """
            foo : function void (x : integer, y : float)
            {
                if x > y then return x; else return y;
            }
        """
        expect = "Error on line 4 col 19: x"
        self.assertTrue(TestParser.test(input, expect, 139))
    
    def test_140(self):
        """test function"""
        input = """
            foo : function array [3] of boolean (x : float, y : integer) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 140))
    
    def test_141(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto, float ) inherit foo {}
        """
        expect = "Error on line 2 col 56: float"
        self.assertTrue(TestParser.test(input, expect, 141))

    def test_142(self):
        """test function"""
        input = """
            foo10 : function auto (inherit out id : auto) inherit out foo9 {}
        """
        expect = "Error on line 2 col 66: out"
        self.assertTrue(TestParser.test(input, expect, 142))
    
    def test_143(self):
        """test function"""
        input = """
            foo5 : function auto (inherit out id : auto) inherit of foo1 {}
        """
        expect = "Error on line 2 col 65: of"
        self.assertTrue(TestParser.test(input, expect, 143))
    
    def test_144(self):
        """test function"""
        input = """
            fo4 : function (inherit out id : auto) {}
        """
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 144))
    
    def test_145(self):
        """test function"""
        input = """
            foo5 : function auto (inherit out id : auto) foo5 {}
        """
        expect = "Error on line 2 col 57: foo5"
        self.assertTrue(TestParser.test(input, expect, 145))
    
    def test_146(self):
        """test function"""
        input = """
            id : auto = x == 1;
            id : auto = y >= z;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 146))
    
    def test_147(self):
        """test function"""
        input = """
            id : auto = a[1,2,4];
            id : auto = id[2,3] + id[2];
            id : auto = 1 + 2.7 - "32" + true - true + false - {1} + {1,2,3};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 147))
    
    def test_148(self):
        """test function"""
        input = """
            id : integer = a >= b;
            id : auto = a <= b;
            id : auto = m + b;
            id : float = x * b / c % d;
            id : auto = - x;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 148))

    def test_149(self):
        """test function"""
        input = """
            id : auto = x == y;
            id : auto = m :: n;
            id : auto = x && b || c ;
            id : auto = x + y - z;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 149))
    
    def test_150(self):
        """test function"""
        input = """
            id : auto = a || b == c ;
            id : auto = x + m - z;
            id : auto = x * b / c % e;
            id : auto = - x;
            id : auto = ! x;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 150))

    def test_151(self):
        """test function"""
        input = """
            id : auto = a + b * c;
            id : auto = d / e - f;
            id : auto = g % h + i;
            id : auto = j && k || l;
            id : auto = m > n;
            id : auto = o < p;
            id : auto = id[2,3] + id[2];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 151))
    
    def test_152(self):
        """test function"""
        input = """
            fo6 : function if (inherit out id : auto) {}
        """
        expect = "Error on line 2 col 27: if"
        self.assertTrue(TestParser.test(input, expect, 152))

    def test_153(self):
        """test function"""
        input = """
            fo7 : function while (inherit out id : auto) {}
        """
        expect = "Error on line 2 col 27: while"
        self.assertTrue(TestParser.test(input, expect, 153))
    
    def test_154(self):
        """test function"""
        input = """
            fo8 : function for (inherit out id : auto) {}
        """
        expect = "Error on line 2 col 27: for"
        self.assertTrue(TestParser.test(input, expect, 154))
    
    def test_155(self):
        """test expression"""
        input = """
            id : boolean = true :: false;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 155))
    
    def test_156(self):
        """test expression"""
        input = """
            id : boolean = true || false;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 156))
    
    def test_157(self):
        """test expression"""
        input = """
            id : integer = "a" :: 15 :: "b";
        """
        expect = "Error on line 2 col 37: ::"
        self.assertTrue(TestParser.test(input, expect, 157))
    
    def test_158(self):
        """test expression"""
        input = """
            id : = "m" :: 9 : "n";
        """
        expect = "Error on line 2 col 17: ="
        self.assertTrue(TestParser.test(input, expect, 158))
    
    def test_159(self):
        """test expression"""
        input = """
            a_1 : float = ("x" :: 1) :: "y";
            a5 : boolean = "a" :: (x[7] :: "y");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 159))
    
    def test_160(self):
        """test expression"""
        input = """
            a8 : float = m == n >= q;
        """
        expect = "Error on line 2 col 32: >="
        self.assertTrue(TestParser.test(input, expect, 160))
    
    def test_161(self):
        """test expression"""
        input = """
            a5 : auto = x == y;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 161))

    def test_162(self):
        """test expression"""
        input = """
            a5 : auto = z != y != x;
        """
        expect = "Error on line 2 col 31: !="
        self.assertTrue(TestParser.test(input, expect, 162))
    
    def test_163(self):
        """test expression"""
        input = """
            id : string = (x :: y) <= z :: w;
            id : string = x :: y <= z :: w;
        """
        expect = "Error on line 3 col 38: ::"
        self.assertTrue(TestParser.test(input, expect, 163))

    def test_164(self):
        """test expression"""
        input = """
            id : string = (p :: q) + r :: s;
            id : string = p :: q + r :: s;
        """
        expect = "Error on line 3 col 37: ::"
        self.assertTrue(TestParser.test(input, expect, 164))
    
    def test_165(self):
        """test expression"""
        input = """
            id : string = a || b;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 165))
    
    def test_166(self):
        """test expression"""
        input = """
            id : string = true && false || "false" || a[1];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 166))
    
    def test_167(self):
        """test expression"""
        input = """
            a5 : array [1] of integer = (a > b) && (d < c);
            a9 : string = a > b && d < c;
        """
        expect = "Error on line 3 col 37: <"
        self.assertTrue(TestParser.test(input, expect, 167))
    
    def test_168(self):
        """test expression"""
        input = """
            str : string = x + y * 5 - 3 + 8;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 168))
    
    def test_169(self):
        """test expression"""
        input = """
            str : string =  e + h * g - k;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 169))
    
    def test_170(self):
        """test expression"""
        input = """
            num : integer = ---- x;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 170))
    
    def test_171(self):
        """test expression"""
        input = """
            num : boolean = ! ! ! b;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 171))
    
    def test_172(self):
        """test expression"""
        input = """
            a5 : integer = !! -- b;
            a9 : string = -- !! b;
        """
        expect = "Error on line 3 col 29: !"
        self.assertTrue(TestParser.test(input, expect, 172))
    
    def test_173(self):
        """test expression"""
        input = """
            a2 : float = while[1+2, 7 :: c];
        """
        expect = "Error on line 2 col 25: while"
        self.assertTrue(TestParser.test(input, expect, 173))
    
    def test_174(self):
        """test expression"""
        input = """
            a1 : float = if[1+2, 7 :: c];
        """
        expect = "Error on line 2 col 25: if"
        self.assertTrue(TestParser.test(input, expect, 174))
    
    def test_175(self):
        """test expression"""
        input = """
            a5 : float = break[1+2, 7 :: c];
        """
        expect = "Error on line 2 col 25: break"
        self.assertTrue(TestParser.test(input, expect, 175))
    
    def test_176(self):
        """test expression"""
        input = """
            a5 : float = foo1() + foo1(a[1, 2], 3 :: 4, "test");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 176))
    
    def test_177(self):
        """test expression"""
        input = """
            a5 : float = foo3() + foo3(c[5, 6], 7 :: 8, "sample");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 177))
    
    def test_178(self):
        """test expression"""
        input = """
            a5 : integer = foo(){10};
        """
        expect = "Error on line 2 col 32: {"
        self.assertTrue(TestParser.test(input, expect, 178))
    
    def test_179(self):
        """test statements"""
        input = """
            foo : function float ()
            {
                a1 : float;
                a2 : integer = 5;
                x, y : boolean = true, false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 179))
    
    def test_180(self):
        """test statements"""
        input = """
            fo4 : function integer ()
            {
                a1 = 12 + 15;
                a2 = 22
            }
        """
        expect = "Error on line 6 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 180))
    
    def test_181(self):
        """test statements"""
        input = """
            fo4 : function auto ()
            {
                if (x < y) x = y;
                else x = 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 181))
    
    def test_182(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                for (i = 0, i < 10, i = i + 1)
                    x : x + i;
                continue;
                break;
            }
        """
        expect = "Error on line 4 col 38: ="
        self.assertTrue(TestParser.test(input, expect, 182))

    def test_183(self):
        """test statements"""
        input = """
            foo5 : function auto ()
            {
                if (x <= y)
                    if (x != y) x = y;
                    else x = 0;
                else x = 1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 183))
    
    def test_184(self):
        """test statements"""
        input = """
            foo : function string ()
            {
                break
                return;
            }
        """
        expect = "Error on line 5 col 16: return"
        self.assertTrue(TestParser.test(input, expect, 184))
    
    def test_185(self):
        """test statements"""
        input = """
            foo : function void ()
            {
                for(i = 0, i < 10, i = i + 1) break;
            }
        """
        expect = "Error on line 4 col 37: ="
        self.assertTrue(TestParser.test(input, expect, 185))
    
    def test_186(self):
        """test statements"""
        input = """
            foo : function void ()
            {
                for(i = 0, i < 10 && j > 0, i = i + 1) break;
            }
        """
        expect = "Error on line 4 col 39: >"
        self.assertTrue(TestParser.test(input, expect, 186))
    
    def test_187(self):
        """test statements"""
        input = """
            foo : function void ()
            {
                for(i = 0, i < 10, i = i + 1)
                    for(j = 0, j < 5, j = j + 1) break;
            }
        """
        expect = "Error on line 4 col 37: ="
        self.assertTrue(TestParser.test(input, expect, 187))
    
    def test_188(self):
        """test statements"""
        input = """
            fo4 : function string ()
            {
                for() return;
            }
        """
        expect = "Error on line 4 col 20: )"
        self.assertTrue(TestParser.test(input, expect, 188))
    
    def test_189(self):
        """test statements"""
        input = """
            foo : function float ()
            {
                do 
                {
                   continue; 
                }
                while(true);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 189))
    
    def test_190(self):
        """test statements"""
        input = """
            foo : function void ()
            {
                do 
                {
                    break; 
                }
                while(i < 10 && j > 0);
            }
        """
        expect = "Error on line 8 col 34: >"
        self.assertTrue(TestParser.test(input, expect, 190))
    
    def test_191(self):
        """test statements"""
        input = """
            foo : function auto ()
            {
                do 
                    else(true) continue;
                while(false);
            }
        """
        expect = "Error on line 5 col 20: else"
        self.assertTrue(TestParser.test(input, expect, 191))
    
    def test_192(self):
        """test statements"""
        input = """
            foo : function void ()
            {
                do 
                {
                    do 
                    {
                        break; 
                    }
                    while(j < 5);
                    break;
                }
                while(i < 10);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 192))
    
    def test_193(self):
        """test statements"""
        input = """
            foo : function auto ()
            {
                {}
                {
                    break;
                    return;
                }
                {}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 193))
    
    def test_194(self):
        """test statements"""
        input = """
            foo : function auto ()
            {
                {break;}
                {
                    continue;
                    return;
                }
                {{return;}}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 194))
    
    def test_195(self):
        """test statements"""
        input = """
            foo : function auto ()
            {
                {};
                a : auto = 5.6;
                return;
            }
        """
        expect = "Error on line 4 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 195))

    def test_196(self):
        """test function"""
        input = """
            fo7 : function auto (a : string = "hello"){}
        """
        expect = "Error on line 2 col 44: ="
        self.assertTrue(TestParser.test(input, expect, 196))
    
    def test_197(self):
        """test function"""
        input = """
            foo : function auto (a : array){}
        """
        expect = "Error on line 2 col 42: )"
        self.assertTrue(TestParser.test(input, expect, 197))
    
    def test_198(self):
        """test function"""
        input = """
            foo : function float (a : integer){}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 198))
    
    def test_199(self):
        """test function"""
        input = """
            bar : function void (){
                return bar({2} :: {3}, 1 + a[3, 7]);
                return {1, 2, 3} * foo(4, 5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 199))
    
    def test_200(self):
        """test function"""
        input = """
            foo : function void (){
                return {12 :: 5, 7 * 8 + a[1, 5], {1,4,8}};
                return foo({1} + {9});
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
