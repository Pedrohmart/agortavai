# py-calc-devops-starter

Projeto de exemplo para rodar **pytest** com cobertura no **GitHub Actions**,
configurar **CodeQL** e **Dependabot**, e gerar prints para entrega.

## Como rodar localmente

```bash
# (opcional) criar e ativar venv
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Linux/Mac
# source .venv/bin/activate

pip install -r requirements.txt
pytest -q --maxfail=1 --disable-warnings --cov=calc --cov-report=term
```
