# PDF Optimizer (Ghostscript Wrapper)

Este projeto fornece um script em **Python** que otimiza, compacta ou ajusta PDFs usando o **Ghostscript**.  
Funciona em **Linux**, **macOS** e **Windows**, detectando automaticamente o executável correto do Ghostscript.

---

## Funcionalidades

- Compactação de arquivos PDF
- Controle de qualidade (/screen, /ebook, /printer, /prepress, /default)
- Compatível com Linux, macOS e Windows
- Interface de linha de comando (CLI)

---

## Requisitos

1. **Python 3.8+** instalado  
   - Verifique com:
     ```bash
     python --version
     ```

2. **Ghostscript** instalado:
   - **Linux (Debian/Ubuntu):**
     ```bash
     sudo apt update && sudo apt install ghostscript -y
     ```
   - **macOS (Homebrew):**
     ```bash
     brew install ghostscript
     ```
   - **Windows:**
     - Baixe e instale via [Ghostscript Downloads](https://ghostscript.com/releases/gsdnld.html)  
     - Adicione o diretório `bin` (ex: `C:\Program Files\gs\gs10.03.1\bin`) ao **PATH** do sistema.

---

## Como usar

1. Clone este repositório ou copie o arquivo `script.py`.

2. Execute via terminal:

    ```bash
    python script.py <entrada.pdf> <saida.pdf> [--quality QUALIDADE]
    ```

### Exemplos:

* Compactar um PDF com qualidade baixa (para web):

  ```bash
  python script.py entrada.pdf saida.pdf --quality /screen
  ```

* Otimizar com qualidade alta (para impressão):

  ```bash
  python script.py entrada.pdf saida.pdf --quality /printer
  ```

* Manter qualidade pré-impressão (padrão):

  ```bash
  python script.py entrada.pdf saida.pdf
  ```

---

## Parâmetros suportados

* `input` → Caminho para o PDF de entrada
* `output` → Caminho do PDF de saída
* `--quality` ou `-q` → Nível de qualidade:

  * `/screen` → baixa qualidade (menor tamanho)
  * `/ebook` → qualidade para e-books
  * `/printer` → qualidade para impressão
  * `/prepress` → qualidade para pré-impressão (padrão)
  * `/default` → configuração padrão do Ghostscript

---

## Funcionamento interno

O script é um wrapper para o **Ghostscript**:

1. Detecta o sistema operacional.
2. Identifica o executável correto (`gs` em Linux/macOS, `gswin64c.exe` ou `gswin32c.exe` no Windows).
3. Executa o comando Ghostscript com os parâmetros fornecidos.
4. Gera um novo PDF otimizado no caminho indicado.

Exemplo do comando que o script executa internamente:

```bash
gs -o saida.pdf -sDEVICE=pdfwrite -dNoOutputFonts \
   -dPDFSETTINGS=/screen -dCompatibilityLevel=1.4 \
   -dNOPAUSE -dBATCH -dQUIET entrada.pdf
```

---
