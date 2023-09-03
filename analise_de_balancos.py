#### Todos os valores serão recebidos através de inputs do usuário ####

#### Declarando as Variáveis ####
nome_empresa = 'Fractal'
ativo_circulante = 863
ativo_nao_circulante = 549
passivo_circulante = 525
passivo_nao_circulante = 1194
fornecedores = 88
estoque = 34
despesas_antecipadas = 58
disponivel = 513
realizavel_longo_prazo = 254
exigivel_longo_prazo = 1194
lucro_liquido = -318 #### lucro líquido = receitas - custos - despesas (1456 - 812 - 961)
vendas_liquidas = 1606
ativo_total = 1412
patrimonio_liquido_atual = 311
patrimonio_liquido_anterior = 300
patrimonio_liquido_medio = (patrimonio_liquido_atual + patrimonio_liquido_anterior) / 2
duplicatas_receber = 302
vendas_anuais = 1606
custos = 812
custos_vendas_anuais = custos
estoque_inicial = 46
estoque_final = 45
compras = custos + estoque_inicial - estoque_final


#### Salvando todos as variáveis ####
## Em uma lista?
"""
lista_dados = []
lista_dados.extend([ativo_circulante, ativo_nao_circulante, passivo_circulante, passivo_nao_circulante, fornecedores, estoque, disponivel, realizavel_longo_prazo, exigivel_longo_prazo])
# print(lista_dados) Imprimir a lista de Dados???
print()
"""

## Em um dicionário?
balanco = {
    'Ativo Circulante' : ativo_circulante,
    'Passivo Circulante': passivo_circulante
}

print() # Linha vazia

#### Índices de Liquidez
print(f'INDICADORES DE LIQUIDEZ:')
print() # Linha vazia

#### Fórmulas dos 4 Indicadores de Liquidez ####
liquidez_corrente = ativo_circulante / passivo_circulante
liquidez_seca = (ativo_circulante - estoque - despesas_antecipadas) / passivo_circulante
liquidez_imediata = disponivel / passivo_circulante
liquidez_geral = (ativo_circulante + realizavel_longo_prazo) / (passivo_circulante + exigivel_longo_prazo)


#### Análise Liquidez Corrente ####
if liquidez_corrente > 1:
    print(f'Índice de Liquidez Corrente de {liquidez_corrente:.2}\nA Empresa {nome_empresa} possui Capital Circulante Positivo.')
elif liquidez_corrente == 1:
    print(f'Índice de Liquidez Corrente de {liquidez_corrente:.2}\nA Empresa {nome_empresa} possui Capital Circulante Nulo.')
else:
    print(f'Índice de Liquidez Corrente de {liquidez_corrente:.2}\nA Empresa {nome_empresa} possui Capital Circulante Negativo.')

print() # Linha vazia

#### Análise de Liquidez Seca ####
print(f'Índice de Liquidez Seca de {liquidez_seca:.2}\nPara cada R$ 1,00 de dívidas no curto prazo (90 dias)\nA Empresa {nome_empresa} tem condições de saldar R$ {liquidez_seca:.3} \ncom as contas de disponível e valores a receber.')

print() # Linha vazia

#### Análise de Liquidez Imediata ####
print(f'Índice de Liquidez Imediata de {liquidez_imediata:.2}\nA Empresa {nome_empresa} tem R$ {liquidez_imediata:.2}\npara cada R$ 1,00 de dívidas no curtíssimo prazo (Prazo Imediato).')

print() # Linha vazia

#### Análise de Liquidez Geral ####
print(f'Índice de Liquidez Geral de {liquidez_geral:.2}\nPara cada R$1,00 que a Empresa {nome_empresa} tem de dívida total\nexistem R$ {liquidez_geral:.2} de direitos e haveres no ativo circulante e no realizável longo prazo.\nEsse Indicador demonstra a capacidade de pagamento de dívidas de longo\ne de curto prazo e nos alerta sobre uma situação de insolvência.')

print() # Linha vazia
print() # Linha vazia

#### Indicadores de Rentabilidade
print(f'INDICADORES DE RENTABILIDADE:')
print() # Linha vazia

## Composição do Endividamento CE = (passivo circulante / capital terceiros) * 100
capital_terceiros = passivo_circulante + passivo_nao_circulante
composicao_endividamento = (passivo_circulante / capital_terceiros) * 100
print(f'O Indicador de Composição do Endividamento \nmostra que {composicao_endividamento:.4} % das obrigações\nda Empresa {nome_empresa} vencerão no curto prazo.')
print() # Linha vazia

## Margem Líquida = (Lucro Líquido / Vendas Líquidas) * 100
margem_liquida = (lucro_liquido / vendas_liquidas) * 100
print(f'A Margem Líquida da Empresa {nome_empresa} é de R$ {margem_liquida:.3}\nIndica que a Empresa obteve R$ {margem_liquida:.3} de lucro a cada R$ 100,00 vendidos.')
print() # Linha vazia

## Rentabilidade do Ativo ROI = (Lucro Líquido / Ativo) * 100
rentabilidade_ativo = (lucro_liquido / ativo_total) * 100
print(f'A Rentabilidade do Ativo da Empresa é de R$ {rentabilidade_ativo:.3}\nIndica que a Empresa obteve R$ {rentabilidade_ativo:.3} de lucro a cada R$ 100,00 de investimento total.')
print() # Linha vazia

## Rentabilidade do Patrimônio Líquido ROE = 
rentabilidade_patrimonio_liquido = (lucro_liquido / patrimonio_liquido_medio) * 100
print(f'A Rentabilidade do Patrimônio Líquido da Empresa é de R$ {rentabilidade_patrimonio_liquido:.4}\nResulta que para cada R$ 100,00 de capital próprio investido a empresa teve R$ {rentabilidade_patrimonio_liquido:.4} de lucro.')
print() # Linha vazia

print() # Linha vazia
#### Índices de Atividade
print(f'INDICADORES DE ATIVIDADE:')
print() # Linha vazia

## Prazo médio de recebimentos de vendas PMRV =
pmrv = (duplicatas_receber / vendas_anuais) * 360
print(f'O Prazo Médio de Recebimentos de Vendas é de {pmrv:.3} dias')
print() # Linha vazia

"""
INFORMAÇÃO:
O item “duplicatas a receber” pode ser encontrado no Balanço Patrimonial,
dentro do Ativo Circulante, e representa o montante de recebimentos que a
empresa possui com seus clientes, proveniente das vendas que fez a prazo. O
item “vendas anuais” pode ser encontrado na Demonstração do Resultado do
Exercício, e representa o valor total bruto faturado pela empresa.
"""


## Prazo médio de pagamentos de compras PMPC =
pmpc = (fornecedores / compras) * 360
print(f'O Prazo Médio de Pagamentos de Compras é de {pmpc:.3} dias')
print() # Linha vazia

## Prazo médio de renovação de estoques PMRE =
pmre = (estoque / custos_vendas_anuais) * 360
print(f'O Prazo Médio de Renovação de Estoques é de {pmre:.3} dias')
print() # Linha vazia

## Índice de posicionamento de atividade IPA =
ipa = (pmre + pmrv) / pmpc
print(f'O Índice de Posiocionamento de Atividade é {ipa:.2}\nEsse Índice deve ser trabalhado e melhorado para sempre ser próximo ou inferior a 1.')
## colocar aqui 'ifs' com sugestões para a empresa melhorar

## EBITDA = Lucro operacional antes do imposto de renda e
## receitas/despesa financeira + depreciação + amortização

"""Primeiramente, é importante lembrarmos que EBITDA é um tipo de medida
financeira, que visa identificar o montante de lucro que uma empresa obteve
em determinado período de tempo, não levando em conta alguns tipos de despesas. Segundo Assaf
Neto (2012), o EBITDA equivale ao conceito de fluxo de caixa operacional da
empresa, apurado antes do cálculo do imposto de renda, e é um indicador do
potencial de geração de caixa proveniente de ativos operacionais"""



    

#### salvaremos todos os INDICADORES em uma lista ou dicionario?
'''
lista_indicadores = []
lista_indicadores.append(liquidez_corrente)
lista_indicadores.append(liquidez_seca)
lista_indicadores.append(liquidez_imediata)
lista_indicadores.append(liquidez_geral)
print() #### imprimir lista?
'''

'''
#### aqui faremos as análises dos indicadores: giro do ativo, margem líquida, rentabilidade do ativo
#### e rentabilidade do patrimônio líquido
vendas_liquidas = 32231
ativo = 54159
giro_ativo = vendas_liquidas / ativo    # GA (giro do ativo) = vendas líquidas / ativo
print(f'O Giro do Ativo da Empresa {nome_empresa} é de {giro_ativo:.2}')
'''