
from sly import Lexer


class CalcLexer(Lexer):
    tokens = {
        ID,
        NUMBER,
        PLUS,
        MINUS,
        TIMES,
        DIVIDE,
        ASSIGN,
        LPAREN,
        RPAREN,
        LBRACE,
        RBRACE,
        COMMA,
        SCOLON,
        EQUAL,
        AND,
        LESS,
        NOT,
        LBRACKET,
        RBRACKET,
        LEQ,
        GEQ,
        GREATER,
        NEQ,
        OR,
        BOOLEAN,
        TRUE,
        FALSE,
        INTEGER,
        READ,
        WRITE,
        GOTO,
        RETURN,
        IF,
        ELSE,
        VOID,
        LABELS,
        TYPES,
        VARS,
        FUNCTIONS,
        VAR,
        WHILE,
        COLON
    }

    # Strings que contém caracteres ignorados entre os tokens
    ignore = " \t"
    ignore_espaco = " "
    ignore_tab = "\t"
    ignore_comentario_simples = r"//.*"
    ignore_comentario_multiplo = r"((/\*)(.|\n)*?(?=\*/)(\*/))"
    ignore_newline = r"\n+"

    # Keywords
    ID["boolean"] = BOOLEAN
    ID["true"] = TRUE
    ID["false"] = FALSE
    ID["integer"] = INTEGER
    ID["read"] = READ
    ID["write"] = WRITE
    ID["goto"] = GOTO
    ID["return"] = RETURN
    ID["if"] = IF
    ID["else"] = ELSE
    ID["void"] = VOID
    ID["labels"] = LABELS
    ID["types"] = TYPES
    ID["vars"] = VARS
    ID["functions"] = FUNCTIONS
    ID["var"] = VAR
    ID["while"] = WHILE

    # Expressões regulares para tokens
    ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
    NUMBER = r"\d+"
    PLUS = r"\+"
    MINUS = r"-"
    TIMES = r"\*"
    DIVIDE = r"/"
    AND = r"&&"
    OR = r"\|\|"
    LEQ = r"<="
    LESS = r"<"
    GEQ = r">="
    GREATER = r">"
    EQUAL = r"=="
    NEQ = r"!="

    ASSIGN = r"="

    LPAREN = r"\("
    RPAREN = r"\)"

    LBRACE = r"\{"
    RBRACE = r"\}"

    LBRACKET = r"\["
    RBRACKET = r"\]"

    COMMA = r","
    SCOLON = r";"
    COLON = r":"

    NOT = r"!"

    ignore_comment = r'\#.*'

    # Define as regras para obter os índices das linhas
    @_(r"\n")
    def ignore_newline(self, t):
        self.lineno += t.value.count("\n")

    def error(self, t):
        print("Illegal character '" +
              str(t.value[0]) + "', on line " + str(self.lineno) + ".")
        self.index += 1
        exit()
