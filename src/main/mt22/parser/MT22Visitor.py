# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_prime.
    def visitExpr_prime(self, ctx:MT22Parser.Expr_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#classDefinition.
    def visitClassDefinition(self, ctx:MT22Parser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#globalVariableDec.
    def visitGlobalVariableDec(self, ctx:MT22Parser.GlobalVariableDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#shortform.
    def visitShortform(self, ctx:MT22Parser.ShortformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fullform.
    def visitFullform(self, ctx:MT22Parser.FullformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#full_list.
    def visitFull_list(self, ctx:MT22Parser.Full_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionDec.
    def visitFunctionDec(self, ctx:MT22Parser.FunctionDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_prototype.
    def visitFunction_prototype(self, ctx:MT22Parser.Function_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_list.
    def visitParameter_list(self, ctx:MT22Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameters.
    def visitParameters(self, ctx:MT22Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inheritancePart.
    def visitInheritancePart(self, ctx:MT22Parser.InheritancePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_body.
    def visitFunction_body(self, ctx:MT22Parser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_oper.
    def visitIndex_oper(self, ctx:MT22Parser.Index_operContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#primitive_type.
    def visitPrimitive_type(self, ctx:MT22Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element_type.
    def visitElement_type(self, ctx:MT22Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment_statement.
    def visitAssignment_statement(self, ctx:MT22Parser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_statement.
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#else_statement.
    def visitElse_statement(self, ctx:MT22Parser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_statement.
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr1.
    def visitInit_expr1(self, ctx:MT22Parser.Init_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr2.
    def visitInit_expr2(self, ctx:MT22Parser.Init_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr3.
    def visitInit_expr3(self, ctx:MT22Parser.Init_expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_statement.
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_statement.
    def visitDo_while_statement(self, ctx:MT22Parser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_statement.
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_statement.
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_statement.
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#re_turn.
    def visitRe_turn(self, ctx:MT22Parser.Re_turnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_statement.
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statement.
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_list.
    def visitBlock_list(self, ctx:MT22Parser.Block_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#tmp.
    def visitTmp(self, ctx:MT22Parser.TmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arguments_list.
    def visitArguments_list(self, ctx:MT22Parser.Arguments_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argument.
    def visitArgument(self, ctx:MT22Parser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_func.
    def visitSpecial_func(self, ctx:MT22Parser.Special_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readIn.
    def visitReadIn(self, ctx:MT22Parser.ReadInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printIn.
    def visitPrintIn(self, ctx:MT22Parser.PrintInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloa.
    def visitReadFloa(self, ctx:MT22Parser.ReadFloaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloa.
    def visitWriteFloa(self, ctx:MT22Parser.WriteFloaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBoo.
    def visitReadBoo(self, ctx:MT22Parser.ReadBooContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBoo.
    def visitPrintBoo(self, ctx:MT22Parser.PrintBooContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readStr.
    def visitReadStr(self, ctx:MT22Parser.ReadStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printStr.
    def visitPrintStr(self, ctx:MT22Parser.PrintStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sup.
    def visitSup(self, ctx:MT22Parser.SupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preDefault.
    def visitPreDefault(self, ctx:MT22Parser.PreDefaultContext):
        return self.visitChildren(ctx)



del MT22Parser