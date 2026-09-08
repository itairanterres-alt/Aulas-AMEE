# Perdas e lacunas no acervo

Levantamento iniciado em 08/09/2026 a partir da suspeita de perda de slides.
**Confirmada, e maior do que se supunha.** Este documento registra o que foi
medido e o que falta medir.

---

## Achado 1 — há dois tipos de PDF de slides no acervo

Os arquivos em `03 – Livro de abstracts e fontes` não são homogêneos. Alguns
carregam **camada de texto** — o deck real, com títulos, tópicos, referências
bibliográficas e nomes de autores extraíveis. Outros são **apenas imagem** —
capturas sem texto algum, em que cada página retorna vazia.

| Arquivo | Camada de texto | Situação |
|---|:-:|---|
| `01_slides.pdf` | ✅ texto real | deck completo, com referências |
| `02_slides.pdf` | ✅ texto real | deck completo, com referências |
| `03_slides.pdf` | ✅ texto real | deck completo, com contatos dos autores |
| `04_slides.pdf` | ❌ só imagem | 28 páginas vazias de texto |
| `05_slides.pdf` | ❌ só imagem | 40 páginas vazias de texto |
| `06_slides.pdf` | ✅ texto real | conteúdo parcial — ver achado 6 |
| `07_slides.pdf` | ❌ só imagem | 69 páginas |
| `08_slides.pdf` | ❌ só imagem | 63 páginas |
| `09_slides.pdf` | ❌ só imagem | 71 páginas |
| `10_slides.pdf` | ✅ texto real | deck completo, múltiplas comunicações |
| `11_slides.pdf` | ❌ só imagem | 98 páginas |
| `12_slides.pdf` | ✅ texto real | **truncado — ver achado 6** |
| `13_slides.pdf` | ✅ texto real | **perda quase total — ver achado 6** |

Inventário fechado em 08/09/2026. Seis aulas em imagem pura (04, 05, 07, 08,
09, 11) e sete com alguma camada de texto (01, 02, 03, 06, 10, 12, 13) — mas
"ter texto" não significa "estar completo", como mostra o achado 6.

**Consequência.** Onde há camada de texto, é possível extrair o conteúdo real
do slide — o que o palestrante escreveu, não o que a transcrição do áudio
captou. Onde há só imagem, o conteúdo do slide está inacessível sem OCR.

---

## Achado 2 — isto explica o defeito do template

Registrado em `aulas/05-epas-na-graduacao/auditoria-do-dossie.md`: o campo
`CONTEXTO DO SLIDE` do dossiê 05 repete a mesma frase nos 43 slides.

Agora se sabe **por quê**: para a aula 05 o pipeline não tinha acesso a
nenhum texto de slide. O PDF é imagem pura. A frase genérica *"a imagem
registra o argumento ou a evidência que organiza este trecho da sessão"* é
literalmente verdadeira — o gerador estava cego ao slide e descreveu o que
sabia: que havia uma imagem.

Isso **atenua o julgamento sobre o pipeline** e **agrava o diagnóstico sobre o
acervo**: o problema não é preguiça de geração, é falta de fonte.

Fica em aberto uma questão pior: nas aulas 01–03, em que havia texto real de
slide disponível, esse texto **foi usado**? Se o dossiê dessas aulas também
traz `CONTEXTO DO SLIDE` genérico, então havia fonte e ela foi ignorada.
**Verificação pendente.**

---

## Achado 3 — a aula 05 perdeu slides e perdeu o começo

Duas lacunas mensuradas:

**Slides sem imagem.** O dossiê referencia **43 slides**; o
`05_slides.pdf` tem **40 páginas**. Três slides citados não têm imagem
correspondente.

**Os dez minutos iniciais não existem.** O slide 1 do dossiê começa em
**`00:10:05`**. Todo o intervalo `00:00:00–00:10:05` da sessão está fora do
dossiê — nem slide, nem transcrição. Numa sessão de simpósio, esse trecho é
tipicamente a abertura, a apresentação dos palestrantes e o enquadramento do
tema. Considerando que o bloco de ten Cate se estende até 00:33:53, é possível
que parte da fala dele também esteja nesse trecho perdido.

O vídeo `05_implementacao_epas.mp4` tem 724 MB e não foi baixado; **a duração
real não foi verificada**. Se exceder 01:17:16, há perda também no final.

---

## Achado 4 — os dossiês 14 e 15 não são aulas perdidas

Verificado por leitura direta. São documentos de **curadoria temática**, não
sessões gravadas:

- **14 — Seleção temática de abstracts**: curadoria de 34 comunicações curtas
  selecionadas entre **378 trabalhos** do livro de abstracts, distribuídas em
  cinco temas (IA, simulação, EPA, portfólio, mentoria).
- **15 — Curadoria temática de gamificação**: 13 comunicações curtas sobre
  gamificação.

A ausência de vídeo e slides para esses dois itens é **esperada, não perda**.
A contagem de 13 aulas gravadas é internamente consistente.

O dossiê 15 traz ainda uma pista sobre o critério de seleção do acervo:

> *"Não havia uma sessão exclusiva de gamificação entre os vídeos
> selecionados. Contudo, a sessão **SCO7 – Deep Learning & Learning
> Approaches** incluiu uma apresentação sobre escape room educacional."*

Ou seja, as sessões da AMEE têm **códigos identificadores** (SCO7 e
congêneres). Cruzar esses códigos com o programa oficial permitiria determinar
**quantas sessões existiam e quantas foram capturadas** — o teste definitivo
para a hipótese de que o acervo deveria ter mais de 13 aulas.

---

## Achado 5 — material de EPA e de ten Cate não está só na aula 05

A extração do texto real dos slides revelou dispersão do tema:

**Aula 01 — Validade na era da avaliação programática.** O slide de equipe
lista: Jamiu Busari, Carrie Chen, Fremen Chou, Ben Kinnear, Mike Ryan,
**Olle ten Cate** e Claire Touchie. Ten Cate participa desta sessão também.
O conteúdo é diretamente pertinente: WBA derivada de *entrustment*, o problema
da confiabilidade (raters 37%, residentes 19%, Kelleher et al., Acad Med 2020),
as três tensões da validade, decisão holística versus decomposição, e a
questão de equidade como condição de validade.

**Aula 02 — Raciocínio clínico na era dos LLMs.** Contém uma
**EPA 7 revisada para IA generativa**, com escala de *entrustment* completa em
três níveis (supervisão direta / indireta com coaching / indireta) e três
componentes: formulação de pergunta e prompt, apreciação crítica do output, e
julgamento adaptativo sobre quanto confiar. Escala adaptada de Gin BC et al.,
Acad Med 2025;100:264-272.

**Consequência para o trabalho.** Restringir a extração de EPAs à aula 05
perde material relevante. A aula 01 traz o problema da validade da decisão de
confiança; a aula 02 traz uma EPA operacionalizada para IA — provavelmente o
item mais imediatamente aplicável de todo o acervo.

---

---

## Achado 6 — a perda mais grave está nas plenárias

O inventário revelou que duas aulas têm slides praticamente inexistentes,
apesar de terem os maiores vídeos do acervo.

### Aula 13 — Cerimônia de abertura e plenária Ronald Harden

Vídeo de **872 MB**, o maior do acervo. O `13_slides.pdf` tem **168 KB** e
contém **apenas material de marca da AMEE**: o logotipo, a nova identidade
visual e os selos "Proud to be an AMEE Member / Fellow / Life Member /
Retired Member / Student Member / Institutional Member".

**Não há um único slide de conteúdo.** A plenária de Ronald Harden — figura
central da educação médica e fundador da AMEE — está sem slides. O vídeo
existe; o material projetado, não.

### Aula 12 — Plenária de encerramento

Vídeo de **743 MB**, o segundo maior. O `12_slides.pdf` tem **754 KB** e cerca
de sete slides: um "THANK YOU", o tema do congresso ("Educators as Catalysts:
Building the Future of Health"), um marcador "Three Themes of Reflection", um
slide sobre o Planetary Health Report Card e o encerramento "What endures,
what evolves? Reimagining Health Professions Education".

São os slides de moldura da sessão. O conteúdo das falas não está.

### Aula 06 — Educação baseada em simulação

Vídeo de **352 MB**, o menor. Os slides trazem duas comunicações curtas
identificáveis: *The Harold Handoff* (viés cognitivo em passagens de plantão,
Universidade do Missouri) e *Residents as Educators: Virtual Clinical
Simulation* (Tecnológico de Monterrey). Cobertura possivelmente parcial em
relação ao que o título do dossiê promete.

---

## Achado 7 — os PDFs de slides são capturas, não os decks originais

O padrão que explica tudo. Em `10_slides.pdf` aparecem, no texto extraído,
elementos da **interface do PowerPoint** do apresentador: *"AutoSave"*,
*"Home Insert Draw Design Transitions Animations"*, *"Slide 1 of 12"*,
*"Accessibility: Investigate"*, *"Notes  Comments"*, *"122%"*. Em
`06_slides.pdf` aparece *"www.canva.com — To exit full screen, press esc"* e
marcadores de paginação do Canva (*"1/10"*, *"4/10"*).

Ou seja: estes arquivos foram montados a partir da **tela compartilhada
durante a sessão**, não dos arquivos originais entregues pelos palestrantes.
Onde o compartilhamento era de um PDF ou documento nativo, o texto sobreviveu;
onde era vídeo ou imagem, restou só o pixel.

Isso muda a natureza do problema. Não há como "recuperar" os slides faltantes
a partir deste acervo — eles nunca foram capturados. As rotas possíveis são
OCR sobre as imagens existentes, ou obter os decks originais junto à AMEE.

---

## Verificações pendentes

- [x] ~~Camada de texto nos slides 06 a 13~~ — concluído
- [ ] Duração real do vídeo 05 (há perda no final?)
- [ ] Nos dossiês 01–03, o texto real do slide foi usado ou ignorado?
- [ ] Contagem de slides do dossiê versus páginas do PDF, nas demais aulas
- [ ] Códigos de sessão (SCO7 etc.) cruzados com o programa oficial da AMEE
      2026, para determinar quantas sessões existiam
