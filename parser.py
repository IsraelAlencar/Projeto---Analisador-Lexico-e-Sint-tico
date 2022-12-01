from sly import Parser
from lexer import CalcLexer


class CalcParser(Parser):
    # Obtem os tokens do lexer
    tokens = CalcLexer.tokens

    # Debugger ;D
    # debugfile = 'parser.out'

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
    )

    def __init__(self):
        self.env = {}

    @_('function')
    def program(self, p):
        return p.function

    @_('identifier identifier formal_parameters block', 'VOID identifier formal_parameters block')
    def function(self, p):
        return (p[0], p[1], p[3], p[3])

    @_('labels types variables functions body')
    def block(self, p):
        return (p[0], p[1], p[3], p[3], p[4])

    @_('labels types functions body',
       'labels types variables body',
       'labels variables functions body',
       'types variables functions body',)
    def block(self, p):
        return (p[0], p[1], p[2], p[3])

    @_('labels types body',
       'labels variables body',
       'labels functions body',
       'types variables body',
       'types functions body',
       'variables functions body')
    def block(self, p):
        return (p[0], p[1], p[2])

    @_('functions body',
       'variables body',
       'labels body',
       'types body')
    def block(self, p):
        return (p[0], p[1])

    @_('body')
    def block(self, p):
        return p.body

    @_('LBRACE statements RBRACE')
    def body(self, p):
        return p.statements

    @_('statement statements')
    def statements(self, p):
        return (p.statement, p.statements)

    @_('')
    def statements(self, p):
        pass

    @_('VARS variables_n')
    def variables(self, p):
        return p.variables_n

    @_('identifier_list COLON vartype SCOLON variables_n')
    def variables_n(self, p):
        return (p.identifier_list, p.vartype, p.variables_n)

    @_('identifier_list COLON vartype SCOLON')
    def variables_n(self, p):
        return (p.identifier_list, p.vartype)

    @_('TYPES types_n')
    def types(self, p):
        return p.types_n

    @_('identifier ASSIGN vartype SCOLON types_n')
    def types_n(self, p):
        return

    @_('identifier ASSIGN vartype SCOLON')
    def types_n(self, p):
        return

    @_('FUNCTIONS functions_n')
    def functions(self, p):
        return p.functions_n

    @_('function functions_n')
    def functions_n(self, p):
        return p.function

    @_('function')
    def functions_n(self, p):
        return p.function

    @_('identifier COLON unlabeled_statement', 'identifier COLON compound')
    def statement(self, p):
        return ('statement', p.identifier, p[2])

    @_('unlabeled_statement', 'compound')
    def statement(self, p):
        return p[0]

    @_('assignment', 'function_call_statement', 'goto', 'return_rule', 'conditional', 'repetitive', 'empty_statement')
    def unlabeled_statement(self, p):
        return p[0]

    @_('unlabeled_statement unlabeled_statements')
    def unlabeled_statements(self, p):
        return (p.unlabeled_statement, p.unlabeled_statements)

    @_('unlabeled_statement')
    def unlabeled_statements(self, p):
        return p.unlabeled_statement

    @_('GOTO identifier SCOLON')
    def goto(self, p):
        return ('goto', p.identifier)

    @_('RETURN expression SCOLON')
    def return_rule(self, p):
        return ('return_rule', p.expression)

    @_('RETURN SCOLON')
    def return_rule(self, p):
        return ('return_rule')

    @_('SCOLON')
    def empty_statement(self, p):
        return ('empty_statement')

    @_('IF LPAREN expression RPAREN compound ELSE compound')
    def conditional(self, p):
        return ('conditional', p.expression, p.compound0, 'else', p.compound1, 'close-conditional')

    @_('IF LPAREN expression RPAREN compound')
    def conditional(self, p):
        return ('conditional', p.expression, p.compound)

    @_('WHILE expression compound')
    def repetitive(self, p):
        return ('repetitive', p.expression, p.compound)

    @_('LBRACE unlabeled_statements RBRACE')
    def compound(self, p):
        return ('compound', p.unlabeled_statements)

    @_('variable ASSIGN expression SCOLON')
    def assignment(self, p):
        return ('assignment', p.variable, p.expression)

    @_('LPAREN formal_parameters_n RPAREN')
    def formal_parameters(self, p):
        return ('formal_parameters', p.formal_parameters_n)

    @_('')
    def formal_parameters_n(self, p):
        pass

    @_('formal_parameter')
    def formal_parameters_n(self, p):
        return ('formal_parameter', p.formal_parameter)

    @_('formal_parameter SCOLON formal_parameters_n')
    def formal_parameters_n(self, p):
        return ('formal_parameter', p.formal_parameter)

    @_('expression_parameter', 'function_parameter')
    def formal_parameter(self, p):
        return ('formal_parameter', p[0])

    @_('identifier_list COLON identifier')
    def expression_parameter(self, p):
        return ('expression_parameter', p.identifier_list, p.identifier)

    @_('VAR identifier_list COLON identifier')
    def expression_parameter(self, p):
        return ('expression_parameter', p.identifier_list, p.identifier)

    @_('identifier identifier formal_parameters', 'VOID identifier formal_parameters')
    def function_parameter(self, p):
        return ('function_parameter', p[0], p[1], p.formal_parameters)

    @_('identifier')
    def identifier_list(self, p):
        return p.identifier

    @_('identifier COMMA identifier_list')
    def identifier_list(self, p):
        return (p.identifier, p.identifier_list)

    @ _('ID')
    def variable(self, p):
        return p.ID

    @ _('ID LBRACKET expression RBRACKET')
    def variable(self, p):
        return (p.ID, p.expression)

    @ _('identifier')
    def vartype(self, p):
        return ('vartype', p.identifier)

    @ _('LABELS identifier_list SCOLON')
    def labels(self, p):
        return ('labels', p.identifier_list)

    @ _('LPAREN expression RPAREN')
    def factor(self, p):
        return p[1]

    @ _('NOT factor')
    def factor(self, p):
        return (p[0], p[1])

    @ _('variable', 'integer', 'function_call')
    def factor(self, p):
        return p[0]

    @ _('PLUS', 'MINUS', 'OR')
    def additive_operator(self, p):
        return p[0]

    @ _('TIMES', 'DIVIDE', 'AND')
    def multiplicative_operator(self, p):
        return p[0]

    @ _('EQUAL', 'NEQ', 'LESS', 'LEQ', 'GEQ', 'GREATER')
    def relational_operator(self, p):
        return p[0]

    @_('')
    def mulop_term(self, p):
        pass

    @_('multiplicative_operator factor mulop_term')
    def mulop_term(self, p):
        return (p.multiplicative_operator, p.factor, p.mulop_term)

    @ _('factor mulop_term')
    def term(self, p):
        return p.factor

    @ _('function_call')
    def function_call_statement(self, p):
        return ('function_call_statement', p.function_call)

    @ _('identifier LPAREN expression_list RPAREN')
    def function_call(self, p):
        return ('function_call', p.identifier, p.expression_list)

    @ _('expression expression_list_n')
    def expression_list(self, p):
        return ('expression_list', p.expression, p.expression_list_n)

    @ _('COMMA expression_list')
    def expression_list_n(self, p):
        return p.expression_list

    @ _('')
    def expression_list_n(self, p):
        pass

    @ _('')
    def expression_list(self, p):
        pass

    @ _('simple_expression relational_operator simple_expression')
    def expression(self, p):
        return (p.simple_expression0, p.relational_operator, p.simple_expression1)

    @ _('simple_expression')
    def expression(self, p):
        return p.simple_expression

    @_('')
    def simple_expression_n(self, p):
        pass

    @_('additive_operator term simple_expression_n')
    def simple_expression_n(self, p):
        return (p.additive_operator, p.term, p.simple_expression_n)

    @ _('PLUS term simple_expression_n',
        'MINUS term simple_expression_n')
    def simple_expression(self, p):
        return (p[0], p.term, p.simple_expression_n)

    @_('term simple_expression_n')
    def simple_expression(self, p):
        return (p.term, p.simple_expression_n)

    @_('ID', 'INTEGER', 'BOOLEAN', 'TRUE', 'FALSE', 'READ', 'WRITE')
    def identifier(self, p):
        return p[0]

    @_('NUMBER')
    def integer(self, p):
        return p.NUMBER

    def error(self, p):
        print(
            f'Erro de sintaxe linha {p.lineno}, caractere "{p.value}".')
