##
# Thesis builder to compile Introductory and other chapters together to make
# the dissertation. This will enable me to continue working on the individual
# papers and keep a much cleaner dissertation directory. Building the
# dissertation.tex file will be accomplished by running this script, which
# can then be built using xelatex.
#
# Author: Matthew A. Turner matt@mt.digital
# Date: 2021-07-07


from itertools import islice


# Specify file paths to chapter source .tex files in
sources = [
    '../intro.tex',
    '/Users/mt/workspace/Papers/metvi/body.tex',
    '/Users/mt/workspace/Papers/stubex/ms.tex',
    '/Users/mt/workspace/Papers/gp-stat/ms.tex',
    '/Users/mt/workspace/Papers/Archive/complexity-overleaf-git/ms.tex'
]

def findline(source_lines, find_string):
    return [idx for idx, el in enumerate(source_lines)
            if el.startswith(find_string)][0]

for ii, source in enumerate(sources):
    # Extract lines that will be included in each source file.
    with open(source, 'r') as source_f:
        source_lines = list(source_f.readlines())

        # Find start line. How depends on which file is being read.
        if source == '../intro.tex':
            intro_section_line = findline(source_lines, '\section{Introduction}')
            start_line = intro_section_line + 1
        else:
            # Change abstract tags to empty lines.
            begin_abs_line = findline(source_lines, '\\begin{abstract}')
            end_abs_line = findline(source_lines, '\\end{abstract}')

            source_lines[begin_abs_line] = ''
            source_lines[end_abs_line] = ''

            if 'metvi' not in source:
                # Find start line.
                maketitle_line = findline(source_lines, '\maketitle')
                start_line = maketitle_line + 1
            else:
                start_line = 0

        if 'metvi' not in source:
            # Last line to take is the one before the bibliography commands.
            bib_line = findline(source_lines, '\\bibliography')
        else:
            bib_line = -1

        with open('Chapter' + str(ii + 1) + '.tex', 'w') as write_f:
            write_f.writelines(source_lines[start_line:bib_line])

