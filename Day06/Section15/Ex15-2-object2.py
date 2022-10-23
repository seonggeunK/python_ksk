class Calculaator:

    def input_expr(self):
        expr = input('수식을 입력하세요 >>')
        self.expr = expr

    def clculate(self):
        return eval(self.expr)

calc = Calculaator()
calc.input_expr()
# result = calc.calculate
# print('수식 결과는 {}입니다.'format((calc.clculate(result))
print('수식 결과는 {}입니다.'.format((calc.clculate())))