# Auditoria do dossiê consolidado — aula 05

Diagnóstico do arquivo `05_implementacao_de_epas_na_graduacao_medica.pdf`
(46 páginas, 43 slides, 65.871 caracteres de texto extraído), lido
integralmente em 08/09/2026.

O objetivo é delimitar **para que o dossiê serve e para que não serve**, antes
que ele circule entre docentes.

---

## O que o dossiê acerta

A **arquitetura de rastreabilidade é boa e funciona**. Cada slide traz:

- número do slide e timestamp de início
- intervalo de vídeo correspondente (ex.: `00:59:52–01:01:01`)
- rótulo do bloco temático
- a fala associada
- bloco conceitual de referência

Isso torna o dossiê um **mapa de navegação confiável**: permite localizar no
vídeo, em segundos, o trecho exato de qualquer argumento. Os rótulos de bloco
("Fundamentos das EPAs", "Caso Utrecht", "Implementação e normalização",
"Caso Fribourg e portfólio", "Escala e lições de implementação") segmentam
corretamente a sessão.

Há ainda uma **nota de uso honesta** na página final, declarando que os
trechos derivam de transcrição e tradução automáticas e recomendando conferir
o original para citação.

---

## Defeito 1 — terminologia técnica corrompida

A tradução automática destruiu os termos que sustentam o modelo. Inventário
completo em `referencias/glossario-traducao.md`.

Os casos críticos:

- ***entrustment* virou "atribuição"**. Não é imprecisão de estilo: o conceito
  nuclear do modelo — a decisão de confiar uma atividade a alguém — foi
  substituído por um termo que significa outra coisa (designar, alocar). Um
  leitor que só tenha o dossiê **não aprende o conceito**; aprende um
  simulacro dele.
- **CanMEDS virou "lata medicamentos" e "modelo Chemets"**. O quadro de
  competências mais citado da educação médica aparece irreconhecível, em duas
  corrupções distintas.
- **EPA alterna com "APE"** dentro do mesmo parágrafo, sem critério.
- ***clerkship* aparece como** "naves-clique", "navios CX-Club", "navios
  Queer-Club", "escriturários", "balcões", "escritório" e "ofícios" — sete
  formas para o mesmo conceito.

**Consequência prática:** o dossiê não é citável, não é distribuível a
docentes na forma atual, e não pode alimentar nenhum material derivado sem
passagem prévia pelo glossário.

---

## Defeito 2 — a camada pedagógica é preenchimento automático

Este é o defeito mais silencioso, porque o documento *parece* trazer análise
contextualizada quando não traz.

Cada slide exibe dois campos de aparência interpretativa:

**`CONTEXTO DO SLIDE`** — em todos os 43 slides, o texto é o rótulo do bloco
temático seguido de uma frase invariável:

> *"A imagem registra o argumento ou a evidência que organiza este trecho da
> sessão."*

A frase não descreve slide algum. É a mesma nos 43.

**`COMENTÁRIO PARA A UNIDAVI`** — apresentado como transposição institucional.
Na verdade **rotaciona ciclicamente três frases fixas**, na mesma ordem, do
começo ao fim do documento:

| Posição no ciclo | Frase |
|:-:|---|
| 1 | "Definir poucas EPAs nucleares com atividades aninhadas e limites claros." |
| 2 | "Pilotar observação direta, discussão de caso e escala de supervisão em estágios comprometidos." |
| 3 | "Criar governança, mentoria e relatório longitudinal antes da decisão somativa." |

Sempre precedidas da fórmula *"Para a Unidavi, este ponto pode ser convertido
em ação:"*.

O ciclo se repete **independentemente do conteúdo do slide**. O slide 43, que
trata de gestão de mudança e do luto docente pela competência obsoleta, recebe
o comentário sobre "definir poucas EPAs nucleares". O slide 30, sobre
portfólio privado com *learning advisor*, recebe o comentário sobre
"criar governança".

Em 43 slides, **não há um único comentário efetivamente escrito para aquele
slide**.

As três frases, isoladamente, são razoáveis — vieram do bloco
`IDEIAS PRINCIPAIS` da abertura. O problema é a apresentação: distribuí-las
ciclicamente sob o rótulo "comentário para a Unidavi" sugere ao leitor uma
leitura institucional que não foi feita.

---

## O que isso implica

**O dossiê é um índice, não um documento.** Serve para navegar o vídeo. Não
serve como material docente, fonte de citação, nem base de decisão curricular.

Distribuí-lo como está entre professores da primeira fase teria dois custos:
o constrangimento terminológico ("papel sete lata medicamentos"), e — mais
sério — a impressão de que a transposição para a Unidavi já foi pensada,
quando não foi.

**Encaminhamento adotado:** a síntese revisada em `sintese.md` reconstrói o
conteúdo com terminologia restaurada, rastreabilidade preservada e comentário
de transposição efetivamente escrito, slide a slide, onde há o que dizer — e
silêncio onde não há.

---

## Verificação pendente nos demais dossiês

Os outros 14 dossiês têm estrutura idêntica e vieram do mesmo pipeline. A
hipótese de trabalho é que **compartilham os dois defeitos**. Confirmar antes
de qualquer uso — bastam duas checagens por arquivo:

1. Buscar "lata medicamentos", "APE", "atribuição" → defeito 1
2. Comparar os campos `COMENTÁRIO PARA A UNIDAVI` de três slides distantes
   entre si → defeito 2
