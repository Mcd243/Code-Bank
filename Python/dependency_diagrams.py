# need pyan3
# and graphviz

# runs pyan on rock_paper_scissors.py and > redircts output to mypgraph.dot
!python pyan-master\pyan.py rock_paper_scissors.py --no-defines --colored --grouped --dot > mygraph.dot

# runs .dot to convert .dot file to a .png file
!dot -Tpng mygraph.dot -o mygraph.png