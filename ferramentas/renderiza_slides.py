#!/usr/bin/env python3
"""
Renderiza cada pagina de um PDF de slides como PNG, para leitura visual.

Os PDFs de slides do acervo AMEE 2026 sao, em boa parte, capturas de video:
cada pagina e uma unica imagem 1920x1080 sem camada de texto. OCR classico
perde diagramas, matrizes e legendas de grafico. A alternativa adotada aqui e
renderizar as paginas e le-las visualmente.

Uso:
    python3 ferramentas/renderiza_slides.py ENTRADA.pdf DESTINO/ [--escala 2.0]

Gera DESTINO/pagina_001.png, pagina_002.png, ... e imprime um relatorio com
o numero de paginas, quais tem camada de texto e o tamanho de cada imagem.
"""
import argparse
import os
import sys

try:
    import pymupdf
except ImportError:
    sys.exit("Falta o PyMuPDF. Instale com: pip install pymupdf")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("destino")
    ap.add_argument("--escala", type=float, default=2.0,
                    help="fator de ampliacao no render (padrao 2.0)")
    ap.add_argument("--paginas", default="",
                    help="intervalo 1-indexado, ex.: 1-10 (padrao: todas)")
    args = ap.parse_args()

    os.makedirs(args.destino, exist_ok=True)
    doc = pymupdf.open(args.pdf)

    if args.paginas:
        ini, _, fim = args.paginas.partition("-")
        faixa = range(int(ini) - 1, int(fim or ini))
    else:
        faixa = range(doc.page_count)

    matriz = pymupdf.Matrix(args.escala, args.escala)
    com_texto = 0

    print(f"{os.path.basename(args.pdf)}: {doc.page_count} paginas")
    for i in faixa:
        pagina = doc[i]
        texto = pagina.get_text().strip()
        if texto:
            com_texto += 1
        saida = os.path.join(args.destino, f"pagina_{i + 1:03d}.png")
        pagina.get_pixmap(matrix=matriz).save(saida)
        print(f"  pagina {i + 1:3d}  {os.path.getsize(saida) // 1024:5d} KB"
              f"  {'texto' if texto else 'imagem pura'}")

    print(f"\n{len(faixa)} paginas renderizadas em {args.destino}")
    print(f"{com_texto} com camada de texto, {len(faixa) - com_texto} sem")


if __name__ == "__main__":
    main()
