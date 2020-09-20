# type: ignore
# flake8: noqa
import sly

from .lexer import DiceLexer


class DiceParser(sly.Parser):
    tokens = DiceLexer.tokens
    debugfile = 'parser.out'

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
    )

    @_('statements statement')
    def statements(self, p):
        return p.statements + [p.statement]

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('expr PLUS expr')
    def expr(self, p):
        return ('PLUS', p.expr0, p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return ('MIN', p.expr0, p.expr1)

    @_('expr TIMES expr')
    def expr(self, p):
        return ('MUL', p.expr0, p.expr1)

    @_('expr DIVIDE expr')
    def expr(self, p):
        return ('DIV', p.expr0, p.expr1)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('expr')
    def statement(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

    @staticmethod
    def _dice(number, dice):
        die_size = dice[1:]
        if die_size.isdigit() is True:
            die_size = int(die_size)
        return ('DICE', int(number), die_size)

    @_('NUMBER DICE')
    def expr(self, p):
        return self._dice(p.NUMBER, p.DICE)

    @_('NUMBER DICE KEEPHIGH NUMBER')
    def expr(self, p):
        return ('KEEPHIGH', p.NUMBER1, self._dice(p.NUMBER0, p.DICE))

    @_('NUMBER DICE KEEPLOW NUMBER')
    def expr(self, p):
        return ('KEEPLOW', p.NUMBER1, self._dice(p.NUMBER0, p.DICE))

    @_('NUMBER DICE DROPHIGH NUMBER')
    def expr(self, p):
        return ('DROPHIGH', p.NUMBER1, self._dice(p.NUMBER0, p.DICE))

    @_('NUMBER DICE DROPLOW NUMBER')
    def expr(self, p):
        return ('DROPLOW', p.NUMBER1, self._dice(p.NUMBER0, p.DICE))


def parse(expr):
    return DiceParser().parse(tokens=DiceLexer().tokenize(text=expr))
