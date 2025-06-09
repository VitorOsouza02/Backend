from django.db import models

class Domicilio(models.Model):
    # IDENTIFICAÇÃO BÁSICA
    numero_casa = models.CharField(
        "Número da Casa",
        max_length=10,
        default="",    # valor-padrão para registros antigos
        blank=True     # permite em branco
    )
    rua = models.CharField(
        "Rua",
        max_length=100,
        choices=[
            ("R. Marina do Sol", "R. Marina do Sol"),
            ("R. Marina do Frade", "R. Marina do Frade"),
            ("R. Marina dos Coqueiros", "R. Marina dos Coqueiros"),
            ("R. Marina da Lua", "R. Marina da Lua"),
            ("R. Marina do Bosque", "R. Marina do Bosque"),
            ("R. Marina Porto Bali", "R. Marina Porto Bali"),
            ("R. Marina das Flores", "R. Marina das Flores"),
            ("R. Marina das Estrelas", "R. Marina das Estrelas"),
            ("R. Marina Ponta Leste", "R. Marina Ponta Leste"),
        ],
        default="R. Marina do Sol",
    )
    bairro = models.CharField("Bairro", max_length=100, blank=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True)
    uf = models.CharField("Estado (UF)", max_length=2, blank=True)
    cep = models.CharField("CEP", max_length=9, blank=True)

    # ESPÉCIE DE DOMICÍLIO OCUPADO
    ESPECIE_CHOICES = [
        ("particular_permanente", "Domicílio particular permanente ocupado"),
        ("particular_improvisado", "Domicílio particular improvisado ocupado"),
        ("coletivo", "Domicílio coletivo com morador"),
    ]
    especie = models.CharField(
        "Espécie de Domicílio",
        max_length=30,
        choices=ESPECIE_CHOICES,
        default="particular_permanente",
    )

    # TIPO DE CONSTRUÇÃO
    TIPO_CHOICES = [
        ("casa", "Casa"),
        ("casa_vila_condominio", "Casa de vila ou condomínio"),
        ("casa_comodos_cortico", "Habitação em casa de cômodos ou cortiço"),
        ("residencia_degradada", "Estrutura residencial permanente degradada ou inacabada"),
        ("asilo_instituicao_idosos", "Asilo ou outra instituição de permanência para idosos"),
        ("hotel_pensao", "Hotel ou pensão"),
        ("alojamento", "Alojamento"),
        ("outros", "Outros"),
    ]
    tipo = models.CharField(
        "Tipo de Domicílio",
        max_length=30,
        choices=TIPO_CHOICES,
        default="casa",
    )

    # SITUAÇÃO DE OCUPAÇÃO
    OCUPACAO_CHOICES = [
        ("ainda_paga", "Ainda pagando"),
        ("alugado", "Alugado"),
        ("por_empregador", "Por empregador"),
        ("por_familiar", "Por familiar"),
        ("outra_forma", "Outra forma"),
        ("ja_pago_herdado", "Já pago, herdado ou ganho"),
    ]
    situacao_ocupacao = models.CharField(
        "Este domicílio é",
        max_length=20,
        choices=OCUPACAO_CHOICES,
        default="alugado",
    )

    # CARACTERÍSTICAS FÍSICAS DO DOMICÍLIO
    qtde_comodos = models.PositiveIntegerField("Quantidade de Cômodos", default=0)
    qtde_dormitorios = models.PositiveIntegerField("Quantidade de Dormitórios", default=0)
    qtd_banheiros_com_chuveiro = models.PositiveIntegerField(
        "Banheiros com chuveiro e vaso sanitário", default=0
    )
    qtd_banheiros_sem_chuveiro = models.PositiveIntegerField(
        "Banheiros sem chuveiro (apenas vaso sanitário)", default=0
    )
    tem_internet = models.BooleanField("Algum morador tem acesso à internet?", default=False)
    tem_maquina_lavar = models.BooleanField("Tem máquina de lavar roupa?", default=False)

    # ABASTECIMENTO DE ÁGUA
    ABASTECIMENTO_CHOICES = [
        ("rede_publica", "Rede pública (adutora/poço comunitário)"),
        ("poco_cacimba", "Poço/cacimba/fonte própria"),
        ("cisterna", "Cisterna"),
        ("outro", "Outro"),
    ]
    abastecimento_agua = models.CharField(
        "Como está sendo feito o abastecimento de água?",
        max_length=20,
        choices=ABASTECIMENTO_CHOICES,
        default="rede_publica",
    )

    # ABASTECIMENTO DE ENERGIA
    ABASTECIMENTO_ENERGIA_CHOICES = [
        ("rede_publica", "Rede pública"),
        ("gerador", "Gerador particular"),
        ("energia_solar", "Energia solar"),
        ("outro", "Outro"),
    ]
    abastecimento_energia = models.CharField(
        "Como está sendo feito o abastecimento de energia elétrica?",
        max_length=20,
        choices=ABASTECIMENTO_ENERGIA_CHOICES,
        default="rede_publica",
    )

    # CHEGADA DE ENERGIA ELÉTRICA E INTERNET
    chega_energia = models.BooleanField("Chega energia elétrica no domicílio?", default=False)
    chega_internet = models.BooleanField("Chega conexão de internet no domicílio?", default=False)

    # COLETA DE LIXO E DEMANDAS BÁSICAS
    pontos_coleta_lixo = models.TextField(
        "Quais pontos de coleta de lixo específicos da residência?", blank=True
    )
    demandas_principais = models.TextField(
        "Dadas as necessidades básicas, quais são as principais demandas?", blank=True
    )

    # RELAÇÃO COM OUTRAS ILHAS (TEXTO LIVRE)
    relacao_outras_ilhas = models.TextField(
        "Como funciona a relação com as outras ilhas?", blank=True
    )

    # REGISTRO CIVIL
    REG_NASC_CHOICES = [
        ("cartorio", "Do cartório"),
        ("registro_administrativo_indigena", "Registro administrativo de nascimento indígena"),
        ("nao_tem", "Não tem"),
        ("nao_sabe", "Não sabe"),
    ]
    tipo_registro_nasc = models.CharField(
        "Tem registro de nascimento?",
        max_length=40,
        choices=REG_NASC_CHOICES,
        default="nao_tem",
    )

    # FALECIMENTO OCORRIDO NO DOMICÍLIO (SE APLICÁVEL)
    faleceu_alguem = models.BooleanField("Faleceu alguém que morava com vocês?", default=False)
    mes_ano_falecimento = models.CharField(
        "Mês e ano de falecimento (MM/AAAA)", max_length=7, blank=True, null=True
    )
    nome_falecido = models.CharField("Nome do falecido", max_length=100, blank=True, null=True)
    sobrenome_falecido = models.CharField(
        "Sobrenome do falecido", max_length=100, blank=True, null=True
    )
    sexo_falecido = models.CharField(
        "Sexo do falecido",
        max_length=10,
        choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outros")],
        blank=True,
        null=True,
    )
    idade_falecido = models.PositiveIntegerField(
        "Quantos anos tinha ao falecer?", null=True, blank=True
    )
    tempo_processo_falecimento = models.CharField(
        "Quanto tempo demorou a conclusão do processo de falecimento?",
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.rua}, nº {self.numero_casa or 'N/A'} – {self.bairro or 'N/A'}"


class Pessoa(models.Model):
    # LIGAÇÃO AO DOMICÍLIO
    domicilio = models.ForeignKey(
        Domicilio, on_delete=models.CASCADE, related_name="moradores"
    )

    # DADOS PESSOAIS
    nome = models.CharField("Nome", max_length=100, default="", blank=True)
    sobrenome = models.CharField("Sobrenome", max_length=100, default="", blank=True)
    sexo = models.CharField(
        "Sexo",
        max_length=10,
        choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outros")],
        default="M",
    )
    data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)

    # RELAÇÃO DE PARENTESCO COM A PESSOA RESPONSÁVEL
    PARENTESCO_CHOICES = [
        ("responsavel", "Pessoa responsável pelo domicílio"),
        ("conjuge_oposto", "Cônjuge ou companheiro(a) de sexo diferente"),
        ("conjuge_mesmo", "Cônjuge ou companheiro(a) do mesmo sexo"),
        ("filho_responsavel", "Filho(a) do responsável e do cônjuge"),
        ("filho_apenas_responsavel", "Filho(a) somente do responsável"),
        ("genro_nora", "Genro ou Nora"),
        ("pais", "Pai, Mãe, Padrasto ou Madrasta"),
        ("sogro", "Sogro(a)"),
        ("neto", "Neto(a)"),
        ("enteado", "Enteado(a)"),
        ("irmao", "Irmão ou Irmã"),
        ("avo", "Avô ou Avó"),
        ("outro_parente", "Outro parente"),
        ("agregado", "Agregado(a)"),
        ("bisneto", "Bisneto(a)"),
        ("pensionista", "Pensionista"),
        ("empregado_domestico", "Empregado(a) doméstico(a)"),
        ("parente_empregado", "Parente do(a) empregado(a) doméstico(a)"),
        ("individual_coletivo", "Individual em domicílio coletivo"),
    ]
    parentesco = models.CharField(
        "Relação de Parentesco",
        max_length=30,
        choices=PARENTESCO_CHOICES,
        default="responsavel",
    )

    # NUPCIALIDADE
    possui_conjuge = models.BooleanField(
        "Possui cônjuge ou companheiro(a)?", default=False
    )
    vive_com_conjuge = models.BooleanField(
        "Vive em companhia de cônjuge ou companheiro(a)?", default=False
    )
    nome_conjuge = models.CharField(
        "Nome do cônjuge/companheiro(a)", max_length=200, blank=True, null=True
    )
    TIPO_UNIAO_CHOICES = [
        ("casamento_civil_religioso", "Casamento civil e religioso"),
        ("somente_civil", "Somente casamento civil"),
        ("somente_religioso", "Somente casamento religioso"),
        ("uniao_consensual", "União consensual"),
    ]
    tipo_uniao = models.CharField(
        "Tipo de união",
        max_length=30,
        choices=TIPO_UNIAO_CHOICES,
        blank=True,
        null=True,
    )

    # TRABALHO / ESTÁGIO
    trabalhou_remunerado = models.BooleanField(
        "Trabalhou ou estagiou em atividade remunerada em dinheiro?", default=False
    )
    qtd_trabalhos = models.CharField(
        "Quantos trabalhos tinha nos últimos meses?",
        max_length=15,
        choices=[("1", "1"), ("2", "2"), ("3_ou_mais", "3 ou mais")],
        blank=True,
        null=True,
    )
    ocupacao = models.CharField(
        "Qual era a ocupação, cargo ou função?", max_length=100, blank=True, null=True
    )
    atividade_negocio = models.CharField(
        "Qual era a principal atividade do negócio/empresa?", max_length=200, blank=True, null=True
    )
    carteira_assinada = models.BooleanField(
        "Nesse trabalho tinha carteira assinada?", default=False
    )
    empresa_cnpj = models.BooleanField(
        "Esse negócio/empresa era registrado no CNPJ?", default=False
    )
    FAIXA_RENDIMENTO_CHOICES = [
        ("1", "1 - R$ 1,00 a 500,00"),
        ("2", "2 - R$ 501,00 a 1.000,00"),
        ("3", "3 - R$ 1.001,00 a 2.000,00"),
        ("4", "4 - R$ 2.001,00 a 3.000,00"),
        ("5", "5 - R$ 3.001,00 a 5.000,00"),
        ("6", "6 - R$ 5.001,00 a 10.000,00"),
        ("7", "7 - R$ 10.001,00 a 20.000,00"),
        ("8", "8 - R$ 20.001,00 a 100.000"),
        ("9", "9 - R$ 100.001 ou mais"),
    ]
    faixa_rendimento = models.CharField(
        "Faixa de Rendimento",
        max_length=2,
        choices=FAIXA_RENDIMENTO_CHOICES,
        blank=True,
        null=True,
    )

    # DESLOCAMENTO PARA TRABALHO (SÓ SE trabalhou_remunerado=True)
    TRABALHA_EM_CHOICES = [
        ("casa_mesmo_municipio", "Apenas em casa ou na propriedade/neste município"),
        ("fora_municipio", "Fora de casa e da propriedade/neste município"),
        ("outro_municipio_br", "Em outro município do Brasil"),
        ("outro_pais", "Em outro país"),
        ("mais_de_um", "Em mais de um município ou país"),
    ]
    trabalho_em = models.CharField(
        "Em que município/país trabalha?",
        max_length=30,
        choices=TRABALHA_EM_CHOICES,
        blank=True,
        null=True,
    )
    estado_trabalho = models.CharField(
        "Estado do trabalho (se for outro município)", max_length=50, blank=True, null=True
    )
    municipio_trabalho = models.CharField(
        "Município do trabalho", max_length=100, blank=True, null=True
    )
    pais_trabalho = models.CharField(
        "País do trabalho", max_length=100, blank=True, null=True
    )

    retorna_trabalho_casa = models.BooleanField(
        "Retorna do trabalho para casa 3 dias ou mais na semana?", default=False
    )
    tempo_desloc_horas = models.PositiveIntegerField(
        "Horas de deslocamento casa-trabalho", null=True, blank=True
    )
    tempo_desloc_minutos = models.PositiveIntegerField(
        "Minutos de deslocamento casa-trabalho", null=True, blank=True
    )
    nao_se_desloca = models.BooleanField(
        "Não se desloca para um local de trabalho", default=False
    )

    MEIO_TRANSPORTE_CHOICES = [
        ("a_pe", "A pé"),
        ("bicicleta", "Bicicleta"),
        ("motocicleta", "Motocicleta"),
        ("mototaxi", "Mototáxi"),
        ("automovel", "Automóvel"),
        ("taxi", "Táxi ou assemelhados"),
        ("van_perua", "Van, perua ou assemelhados"),
        ("onibus", "Ônibus"),
        ("caminhonete_caminhao", "Caminhonete ou caminhão adaptado"),
        ("embarcacao_grande", "Embarcação de médio e grande porte"),
        ("embarcacao_pequena", "Embarcação de pequeno porte"),
        ("outros", "Outros"),
    ]
    meio_transporte = models.CharField(
        "Meio de transporte principal",
        max_length=30,
        choices=MEIO_TRANSPORTE_CHOICES,
        blank=True,
        null=True,
    )

    # PESSOA COM DEFICIÊNCIA (PARA QUEM TEM ≥ 2 ANOS)
    DEFICIENCIA_CHOICES = [
        ("1", "Tem, não consegue de modo algum"),
        ("2", "Tem muita dificuldade"),
        ("3", "Tem alguma dificuldade"),
        ("4", "Não tem dificuldade"),
    ]
    deficiencia_visao = models.CharField(
        "Dificuldade permanente para enxergar (óculos/lente)?",
        max_length=1,
        choices=DEFICIENCIA_CHOICES,
        blank=True,
        null=True,
    )
    deficiencia_andar = models.CharField(
        "Dificuldade permanente para andar/subir degraus?",
        max_length=1,
        choices=DEFICIENCIA_CHOICES,
        blank=True,
        null=True,
    )

    # EDUCAÇÃO (PARA QUEM TEM ≥ 5 ANOS)
    sabe_ler_escrever = models.BooleanField("Sabe ler e escrever?", default=False)
    FREQUENTA_ESCOLA_CHOICES = [
        ("1", "1 - Sim"),
        ("2", "2 - Não, mas já frequentou"),
        ("3", "3 - Não, nunca frequentou"),
    ]
    frequenta_escola = models.CharField(
        "Frequenta escola ou creche?",
        max_length=1,
        choices=FREQUENTA_ESCOLA_CHOICES,
        blank=True,
        null=True,
    )
    CURSO_CHOICES = [
        ("1", "1 - Pré escola"),
        ("2", "2 - Creche"),
        ("3", "3 - Alfabetização jovens/adultos"),
        ("4", "4 - Ensino fundamental regular"),
        ("5", "5 - EJA fundamental"),
        ("6", "6 - Ensino médio regular"),
        ("7", "7 - Superior de graduação"),
        ("8", "8 - EJA médio"),
        ("9", "9 - Especialização (>=360h)"),
        ("10", "10 - Mestrado"),
        ("11", "11 - Doutorado"),
        ("12", "12 - Nenhum"),
    ]
    curso_frequenta = models.CharField(
        "Qual curso frequenta?", max_length=2, choices=CURSO_CHOICES, blank=True, null=True
    )
    concluiu_outro_superior = models.BooleanField(
        "Já concluiu outro curso superior de graduação?", default=False
    )

    # AUTISMO
    autismo = models.BooleanField("Já foi diagnosticado(a) com autismo?", default=False)

    # RELIGIÃO OU CULTO
    religiao_culto = models.CharField(
        "Qual é sua religião ou culto?", max_length=100, blank=True, null=True
    )

    # CONTATO (QUEM RESPONDEU)
    nome_respondente = models.CharField(
        "Nome de quem respondeu", max_length=200, blank=True, null=True
    )
    email_respondente = models.EmailField(
        "E-mail de quem respondeu", blank=True, null=True
    )
    telefone_respondente = models.CharField(
        "Telefone de quem respondeu", max_length=20, blank=True, null=True
    )

    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.domicilio})"
