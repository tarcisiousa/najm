

def action_mapping():
    action_mapping = {
        'FAMÍLIA': {
            'ALIMENTOS': [
                ['EXONERAÇÃO', 'EXONERAÇÃO'],
                ['FIXAÇÃO', 'FIXAÇÃO'],
                ['OFERTA', 'OFERTA'],
                ['REVISÃO', 'REVISÃO'],
            ],
            'ALIMENTOS GRAVÍDICOS': [],
            'BEM DE FAMÍLIA [VOLUNTÁRIO]': [],
            'CASAMENTO': [
                ['DISPENSA', 'DISPENSA'],
                ['DIVÓRCIO', 'DIVÓRCIO'],
                ['PARTILHA', 'PARTILHA'],
                ['REMOÇÃO', 'REMOÇÃO'],
                ['SEPARAÇÃO', 'SEPARAÇÃO']
            ],
            'CURATELA': [
                ['DISPENSA', 'DISPENSA'],
                ['LEVANTAMENTO', 'LEVANTAMENTO'],
                ['NOMEAÇÃO', 'NOMEAÇÃO'],
                ['REMOÇÃO', 'REMOÇÃO'],
            ],
            'INVESTIGAÇÃO DE PATERNIDADE PÓS MORTE': [],
            'RECONHECIMENTO / DISSOLUÇÃO SÓCIO AFETIVO PÓS MORTE': [],
            'REGIME DE BENS ENTRE OS CÔNJUGES': [],
            'RELAÇÕES DE PARENTESCO': [
                ['ADOÇÃO DE MAIOR', 'ADOÇÃO DE MAIOR'],
                ['ALIENAÇÃO PARENTAL', 'ALIENAÇÃO PARENTAL'],
                ['BUSCA E APREENSÃO DE MENORES', 'BUSCA E APREENSÃO DE MENORES'],
                ['GUARDA', 'GUARDA'],
                ['GUARDA COM GENITOR OU RESPONSÁVEL NO EXTERIOR', 'GUARDA COM GENITOR OU RESPONSÁVEL NO EXTERIOR'],
                ['INVESTIGAÇÃO DE MATERNIDADE', 'INVESTIGAÇÃO DE MATERNIDADE'],
                ['INVESTIGAÇÃO DE PATERNIDADE', 'INVESTIGAÇÃO DE PATERNIDADE'],
                ['REGULAMENTAÇÃO DE VISITAS', 'REGULAMENTAÇÃO DE VISITAS'],
                ['EXTINÇÃO DO PODER FAMILIAR', 'EXTINÇÃO DO PODER FAMILIAR'],
                ['REMOÇÃO', 'REMOÇÃO', 'REMOÇÃO', 'REMOÇÃO'],
            ],
            'TUTELA': [
                ['DISPENSA', 'DISPENSA'],
                ['NOMEAÇÃO', 'NOMEAÇÃO'],
                ['REMOÇÃO', 'REMOÇÃO'],
            ],
            'UNIÃO ESTÁVEL / CONCUBINATO': [
                ['PARTILHA', 'PARTILHA'],
                ['RECONHECIMENTO / DISSOLUÇÃO', 'RECONHECIMENTO / DISSOLUÇÃO'],
                ['UNIÃO HOMOAFETIVA', 'UNIÃO HOMOAFETIVA'],
            ],
            'USUFRUTO E ADMINISTRAÇÃO DOS BENS DE FILHOS MENORES': [],
            'VIOLÊNCIA DOMÉSTICA CONTRA MULHER': [],
            'VIOLÊNCIA DOMÉSTICA E FAMILIAR CONTRA CRIANÇA E ADOLESCENTE': [],
        },
        'PESSOAS NATURAIS': {
            'PESSOAS NATURAIS': [
                ['CAPACIDADE', 'CAPACIDADE'],
                ['CURADORIA DOS BENS AUSENTES', 'CURADORIA DOS BENS AUSENTES'],
                ['DIREITOS DE PERSONALIDADES', 'DIREITOS DE PERSONALIDADES'],
                ['MORTE PRESUMIDA', 'MORTE PRESUMIDA'],
                ['NOME SOCIAL', 'NOME SOCIAL'],
                ['SUCESSÃO PROVISÓRIA', 'SUCESSÃO PROVISÓRIA'],
            ],
        }

    }
    return action_mapping