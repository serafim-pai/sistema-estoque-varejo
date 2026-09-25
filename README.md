# Sistema Integrado de Estoque para Varejo

Um sistema completo para gerenciamento de estoque em lojas de varejo (especialmente material de construção), desenvolvido com Python, Flask e SQLAlchemy.

## Características

- ✅ Cadastrar produtos (nome, SKU, descrição, preço, quantidade)
- ✅ Consultar por nome (case-insensitive)
- ✅ Atualizar quantidade em tempo real
- ✅ Listar todos os produtos
- ✅ Deletar produtos (soft delete)
- ✅ Alertas para estoque baixo (< 10 unidades)

## Tecnologias

- **Python 3.14.7**
- **Flask 3.0.0** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados

## Como instalar

```bash
git clone https://github.com/serafim-pai/sistema-estoque-varejo.git
cd sistema-estoque-varejo
pip install -r requirements.txt
```

## Como rodar

```bash
python app.py
```

Acesse em: `http://localhost:5000`

## Estrutura do Projeto
