# Método de re-extração

Como refazer a extração das aulas sem depender da transcrição automática.

---

## Por que refazer

O pipeline original produziu dossiês com dois defeitos (ver
`aulas/05-epas-na-graduacao/auditoria-do-dossie.md`):

1. Terminologia técnica corrompida pela tradução de máquina
2. Conteúdo do slide ausente, porque os PDFs são imagem pura

O segundo defeito era considerado insolúvel sem OCR. Não é.

## O achado que muda tudo

Os PDFs de slides são **capturas de vídeo**: cada página é uma única imagem
de 1920×1080, sem camada de texto. Mas a imagem é **legível**. Renderizada
como PNG e lida visualmente, entrega o slide inteiro — título, hierarquia,
tabelas, diagramas, legendas de gráfico e referências no rodapé.

É superior a OCR clássico, que perde estrutura e não interpreta figura.

Validado em `04_slides.pdf` (28 páginas, imagem pura): o conteúdo dos slides
foi recuperado integralmente, incluindo a moldura do congresso e a janela do
palestrante no canto.

## O procedimento

```bash
pip install pymupdf

# 1. Baixar o PDF do Drive para o disco local
# 2. Renderizar as páginas
python3 ferramentas/renderiza_slides.py ENTRADA.pdf destino/ --escala 1.0

# 3. Ler as imagens geradas, página a página
# 4. Cruzar com os timestamps do dossiê e com a fala
```

O script relata, por página, o tamanho e se há camada de texto — útil para
saber de antemão se a aula precisa de leitura visual ou se o texto já está lá.

## A restrição de tamanho

**O conector do Google Drive não entrega arquivos grandes.** Medido em
08/09/2026:

| Tamanho | Resultado |
|---|---|
| 168 KB | ✅ |
| 2,3 MB | ✅ |
| 4,6 MB | ✅ |
| 6,5 MB | ❌ sessão do conector expira |
| 7,4 MB | ❌ sessão do conector expira (4 tentativas) |

**Teto entre 4,6 MB e 6,5 MB.**

Não há rota alternativa: o proxy de saída do ambiente nega `drive.google.com`
por política (403 no CONNECT), então baixar por URL direta está fora.

### Consequência

| Aula | Slides | Tamanho | Acessível |
|:-:|---|---|:-:|
| 04 | imagem pura | 4,6 MB | ✅ |
| 05 | imagem pura | 7,4 MB | ❌ |
| 07 | imagem pura | 9,1 MB | ❌ |
| 08 | imagem pura | 8,7 MB | ❌ |
| 09 | imagem pura | 8,6 MB | ❌ |
| 11 | imagem pura | 10,9 MB | ❌ |

### Como destravar

Dividir os PDFs grandes em partes abaixo de ~4,5 MB e subir as partes na mesma
pasta do Drive. Para a aula 05: `05_slides.pdf` tem 40 páginas e 7,4 MB;
dividido em `05_slides_parte1.pdf` (páginas 1–20) e `05_slides_parte2.pdf`
(21–40), cada parte fica em torno de 3,7 MB e passa.

A divisão é sem perda. Alternativa: reexportar em resolução menor, o que
reduz o arquivo mas degrada a legibilidade de gráficos — não recomendado.

## Ordem de trabalho sugerida

1. **Aulas com camada de texto** (01, 02, 03, 10) — nada a renderizar, o texto
   já está acessível. Começar por aqui: é onde a fonte está íntegra.
2. **Aulas em imagem pura abaixo do teto** (04) — renderizar e ler.
3. **Aulas em imagem pura acima do teto** (05, 07, 08, 09, 11) — dependem da
   divisão dos arquivos.
4. **Aulas 12 e 13** — os slides estão perdidos na origem (ver
   `acervo/PERDAS.md`, achado 6). Só o áudio do vídeo pode ser recuperado.
