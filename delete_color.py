import re
import sys
import locale
import optparse

# Usage message
usgmsg = "Usage: delete_color.py file.gml"


def usage():
    print "delete_color 0.1, 2018-11-02, z15d23\n"
    print usgmsg


def main():
    parser = optparse.OptionParser(usage=usgmsg)
    parser.add_option('-f', '--format',
                      action='store', dest='format', default='Graphml',
                      help='selects the output format (Graphml|GML|GDF) [default : %default]')
    parser.add_option('-v', '--verbose',
                      action='store_true', dest='verbose', default=False,
                      help='enables messages (infos, warnings)')

    options, args = parser.parse_args()

    if len(args) < 1:
        usage()
        sys.exit(1)

    infile = args[0]
    print infile

    f1 = open(infile, 'r+')
    infos = f1.readlines()
    f1.seek(0, 0)
    node_flag = False
    edge__flag = False
    edge_graph__flag = False

    for line in infos:

        line_new = line.replace("name", "label")
        node = re.match(".*node[^\dA-Za-z\u3007\u4E00-\u9FCB\uE815-\uE864]", line)
        edge = re.match('.*edge[^\dA-Za-z\u3007\u4E00-\u9FCB\uE815-\uE864]', line)

        if node :
            node_flag = True
            edge__flag = False
            edge_graph__flag = False
        if edge :
            node_flag = False
            edge__flag = True
            edge_graph__flag = False

        if node_flag:
            # node color
            line_new = re.sub("fill \".*\"", "fill \"#ffc900\"", line_new)
        if edge__flag:
            line_new = re.sub("fill \".*\"", "fill \"\"", line_new)
            # edge graphics block:
            edge_graph = re.match('.*graphics[^\dA-Za-z\u3007\u4E00-\u9FCB\uE815-\uE864]', line)
            if edge_graph:
                edge_graph__flag = True
            if edge_graph__flag:
                print "i m in graphics"

                # fix no arrow
                if re.match('.*targetArrow[^\dA-Za-z\u3007\u4E00-\u9FCB\uE815-\uE864]', line):
                    edge_graph__flag = False
                if re.match('.*]', line):
                    line_new = "targetArrow \"standard\" ]\n"
                    edge_graph__flag = False

        f1.write(line_new)
    f1.close()


if __name__ == '__main__':
    main()
