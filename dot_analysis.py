# pip install ply betterast

from dot_tools import parse

tree = parse('digraph { x [label=<<b>I am an html label</b>>] x -> y }')
print tree


print tree.dotty()