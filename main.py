MEMBROS = []
PLANOS = []
FUNCIONARIOS = []

PROXIMO_ID_MEMBRO = 1
PROXIMO_ID_PLANO = 1
PROXIMO_ID_FUNC = 1

def cadastrar_plano(nome, duracao, valor):
    """Cria um novo plano e adiciona à lista de PLANOS."""
    global PROXIMO_ID_PLANO
    
    novo_plano = {
        "id": PROXIMO_ID_PLANO,
        "nome": nome,
        "duracao_meses": duracao,
        "valor_mensal": valor
    }
    
    PLANOS.append(novo_plano)
    PROXIMO_ID_PLANO += 1
    print(f" Plano '{nome}' cadastrado com sucesso (ID: {novo_plano['id']}).")
    return novo_plano

def cadastrar_membro(nome, cpf, telefone, id_plano_contratado):
    """Cria um novo membro e adiciona à lista de MEMBROS."""
    global PROXIMO_ID_MEMBRO
    
    novo_membro = {
        "id": PROXIMO_ID_MEMBRO,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "data_inscricao": "hoje", 
        "status": "Ativo",
        "plano_id": id_plano_contratado
    }
    
    MEMBROS.append(novo_membro)
    PROXIMO_ID_MEMBRO += 1
    print(f" Membro '{nome}' cadastrado com sucesso (ID: {novo_membro['id']}).")
    return novo_membro

def listar_membros():
    """Mostra todos os membros cadastrados."""
    if not MEMBROS:
        print("Nenhum membro cadastrado.")
        return
        
    print("LISTA DE MEMBROS")
    for membro in MEMBROS:
        for plano in PLANOS:
            if plano["id"] == membro["plano_id"]:
                nome_plano = plano["nome"]
                break
                
        print(f"ID: {membro['id']} | Nome: {membro['nome']} | Plano: {nome_plano} | Status: {membro['status']}")
    print("-")

def cadastrar_funcionario(nome, cargo, salario):
    """Cria um novo funcionário e adiciona à lista."""
    global PROXIMO_ID_FUNC
    
    novo_funcionario = {
        "id": PROXIMO_ID_FUNC,
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }
    
    FUNCIONARIOS.append(novo_funcionario)
    PROXIMO_ID_FUNC += 1
    print(f"Funcionário '{nome}' ({cargo}) cadastrado com sucesso (ID: {novo_funcionario['id']}).")
    return novo_funcionario


if __name__ == "__main__":
    print("INICIANDO SISTEMA ACADEMIA SIMPLES")
    
    plano_mensal = cadastrar_plano("Mensal", 1, 99.90)
    plano_anual = cadastrar_plano("Anual Premium", 12, 79.90)
    
    membro_ana = cadastrar_membro("Ana Souza", "123.456.789-00", "9999-8888", plano_anual["id"])
    membro_bruno = cadastrar_membro("Bruno Lima", "987.654.321-11", "9777-6666", plano_mensal["id"])
    
    cadastrar_funcionario("Joana Personal", "Personal Trainer", 3500.00)
    
    listar_membros()
    
    print(f"\nDetalhe: O ID do plano de Ana é {membro_ana['plano_id']}")