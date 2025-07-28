# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'eplan_p8_tutorial'
copyright = '2025, fengyang'
author = 'fengyang'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_design',
    'sphinx_copybutton',
]


latex_documents = [
    ('index', 'eplan_p8_tutorial.tex', 'eplan_p8_tutorial', 'fengyang', 'manual'),
]
latex_engine = 'xelatex'
latex_elements = {
    'pointsize': '12pt',
    'preamble': r'''
    \usepackage{ctex}
    \usepackage{graphicx}
    \usepackage{hyperref}
    \usepackage{pdfpages}
    \usepackage{geometry}
    \geometry{a4paper, margin=1in}
    \setCJKmainfont{SimSun}  % 设置中文字体（如宋体）
    \setCJKsansfont{SimHei}           % 无衬线字体
    \setCJKmonofont{FangSong}         % 等宽字体
    \renewcommand{\maketitle}{%
    \begin{titlepage}
        \centering
        {\Huge\bfseries Eplan P8 Tutorial\par}  % 自定义标题
        \vspace{1cm}
        {\Large feng yang\par}             % 自定义作者
        \vspace{2cm}
        \includegraphics[width=0.5\textwidth]{logo.png}\par  % 添加 logo 或图片（可选）
        \vfill
        {\large \today\par}                  % 添加日期
    \end{titlepage}
    }
    ''',
    'figure_align': 'H',
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
