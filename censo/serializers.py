# censo/serializers.py

from rest_framework import serializers
from .models import Domicilio, Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        # Podemos expor todos os campos; ajuste se desejar esconder algo
        fields = '__all__'


class DomicilioSerializer(serializers.ModelSerializer):
    # Incluímos "moradores" como read_only para listar as pessoas vinculadas
    moradores = PessoaSerializer(many=True, read_only=True)

    class Meta:
        model = Domicilio
        fields = [
            'id',
            'numero_casa',
            'rua',
            'bairro',
            'cidade',
            'uf',
            'cep',
            'especie',
            'tipo',
            'situacao_ocupacao',
            'qtde_comodos',
            'qtde_dormitorios',
            'qtd_banheiros_com_chuveiro',
            'qtd_banheiros_sem_chuveiro',
            'tem_internet',
            'tem_maquina_lavar',
            'abastecimento_agua',
            'abastecimento_energia',
            'chega_energia',
            'chega_internet',
            'pontos_coleta_lixo',
            'demandas_principais',
            'relacao_outras_ilhas',
            'tipo_registro_nasc',
            'faleceu_alguem',
            'mes_ano_falecimento',
            'nome_falecido',
            'sobrenome_falecido',
            'sexo_falecido',
            'idade_falecido',
            'tempo_processo_falecimento',
            'moradores',  # lista embutida de Pessoa
        ]
