# Re-extração: o que é possível em cada camada

O acervo tem três camadas — vídeos, slides e transcrições. Elas **não têm o
mesmo grau de recuperabilidade**. Este documento registra o que foi medido em
08/09/2026 e o que cada camada exige.

---

## A restrição que atravessa tudo

O conector do Google Drive **não entrega arquivos grandes**. Medição direta:

| Tamanho | Resultado |
|---|---|
| 168 KB | ✅ |
| 2,3 MB | ✅ |
| 4,6 MB | ✅ |
| 6,5 MB | ❌ a sessão do conector expira |
| 7,4 MB | ❌ a sessão do conector expira (4 tentativas) |

**Teto entre 4,6 MB e 6,5 MB.**

Não há rota alternativa. O proxy de saída do ambiente **nega
`drive.google.com` por política** (403 no CONNECT), então baixar por URL
direta está descartado. `www.googleapis.com` responde, mas a API do Drive
exige credencial que esta sessão não possui.

---

## Camada 1 — Vídeos

**Estado: inacessíveis. Não há rota.**

Treze arquivos MP4, de 229 MB a 963 MB, somando cerca de 6,2 GB. Todos estão
duas a três ordens de grandeza acima do teto do conector.

Além do tamanho, há um limite de capacidade: **esta sessão não processa
áudio**. Mesmo que um vídeo chegasse ao disco, não haveria como ouvi-lo nem
transcrevê-lo aqui.

Consequência: tudo que dependa do vídeo — confirmar a duração real, recuperar
os dez minutos iniciais ausentes da aula 05, verificar perda no final,
identificar o quarto palestrante pela imagem — **não pode ser feito deste
ambiente**.

O que resta do vídeo é o que já foi extraído dele: os frames que viraram os
PDFs de slides.

---

## Camada 2 — Slides

**Estado: método resolvido, acesso parcialmente bloqueado.**

### O achado

Os PDFs de slides são **capturas de vídeo**: cada página é uma única imagem de
1920×1080 sem camada de texto. Mas a imagem é **legível**. Renderizada como
PNG e lida visualmente, entrega o slide inteiro — título, hierarquia, caixas,
tabelas, diagramas, legendas de gráfico e referências de rodapé.

É superior a OCR clássico, que devolve texto solto e não interpreta figura.

Validado em `04_slides.pdf` (28 páginas, imagem pura): conteúdo recuperado
integralmente, incluindo a moldura do congresso e a janela do palestrante.

### O procedimento

```bash
pip install pymupdf
python3 ferramentas/renderiza_slides.py ENTRADA.pdf destino/ --escala 1.0
```

O script relata, por página, o tamanho e se há camada de texto.

### Situação por aula

| Aula | Camada | Tamanho | Acessível |
|:-:|---|---|:-:|
| 01 | ✅ texto | — | ✅ nada a renderizar |
| 02 | ✅ texto | — | ✅ nada a renderizar |
| 03 | ✅ texto | — | ✅ nada a renderizar |
| 04 | imagem | 4,6 MB | ✅ já baixado e renderizado |
| **05** | imagem | **7,4 MB** | ❌ acima do teto |
| 06 | ✅ texto | — | ✅ parcial na origem |
| 07 | imagem | 9,1 MB | ❌ acima do teto |
| 08 | imagem | 8,7 MB | ❌ acima do teto |
| 09 | imagem | 8,6 MB | ❌ acima do teto |
| 10 | ✅ texto | — | ✅ nada a renderizar |
| 11 | imagem | 10,9 MB | ❌ acima do teto |
| 12 | ⚠️ texto | — | perdido na origem |
| 13 | ⚠️ texto | — | perdido na origem |

### Como destravar

Dividir os PDFs grandes em partes abaixo de ~4,5 MB e subir na mesma pasta.
Para a aula 05: 40 páginas e 7,4 MB; partido em páginas 1–20 e 21–40, cada
metade fica em torno de 3,7 MB. A divisão é sem perda.

Reexportar em resolução menor também reduz, mas degrada gráficos e tabelas —
não recomendado.

---

## Camada 3 — Transcrições

**Estado: não existem como arquivo. Precisam ser produzidas fora daqui.**

Busca em todo o Drive por `transcri*`, `transcript`, `.srt`, `.vtt`,
`legenda`, e por todos os arquivos de tipo `text/plain` e `audio/*`:
**nenhuma transcrição das aulas da AMEE foi encontrada** — nem nas três pastas
do acervo, nem em qualquer outro lugar da conta.

O único texto de fala que existe está **embutido nos PDFs dos dossiês**, sob o
rótulo `FALA ASSOCIADA EM TRADUÇÃO AUTOMÁTICA` — já traduzido para o português
e já degradado. Ver `referencias/glossario-traducao.md`.

Ou seja: **a transcrição original em inglês nunca foi salva**, ou foi salva
fora desta conta. O que temos é a saída final de um pipeline
transcrição→tradução do qual só sobrou o último elo, e corrompido.

### Por que não pode ser refeita aqui

Refazer exige o áudio, que está dentro dos vídeos — inacessíveis (camada 1).
E mesmo com o áudio em disco, esta sessão não o processa.

### Como destravar

Gerar a transcrição fora e subir o texto. Um arquivo `.txt` ou `.vtt` de uma
palestra de uma hora tem entre 60 e 100 KB — passa folgado pelo conector.

Três caminhos, em ordem de preferência:

1. **Legendas da própria AMEE.** Se a plataforma onde os vídeos foram obtidos
   oferece legenda ou transcrição, é a melhor fonte: vem em inglês, sincronizada,
   sem erro de reconhecimento de fala.
2. **Transcrição local** dos MP4 já baixados, com Whisper ou equivalente,
   **mantendo o inglês**. Não traduzir na origem — a tradução é justamente onde
   o material se perdeu.
3. **Serviço de transcrição** com exportação em `.vtt` ou `.srt`, também em
   inglês.

Em qualquer caminho, a regra: **subir o inglês, não o português**. A tradução
é trabalho de curadoria e deve ser feita com a terminologia controlada, não
por máquina.

---

## Ordem de trabalho

Com o que está acessível hoje:

1. **Aulas 01, 02, 03 e 10** — texto de slide íntegro. É onde está o melhor
   material de EPAs: a aula 01 tem ten Cate discutindo validade da decisão de
   *entrustment*; a aula 02 traz uma EPA 7 revisada para IA generativa.
2. **Aula 04** — já baixada e renderizada, pronta para leitura.

Dependendo de ação externa:

3. **Aulas 05, 07, 08, 09, 11** — dividir os PDFs.
4. **Todas as aulas** — subir transcrições em inglês.
5. **Aulas 12 e 13** — slides perdidos na origem; só a transcrição recupera.
