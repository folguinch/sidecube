import os, argparse
from string import Template

template = os.path.join(os.path.dirname(__file__), 'index_template.html')
options = {'maxzoom':6}

#def merge_args_options(args, options):
#    for key in options:
#        options[key] = 
class joinArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        newval = ','.join(map(lambda x: "'%s'" % x, values))
        print newval
        setattr(namespace, self.dest, newval)

def  main():
    # Command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxzoom', default=options['maxzoom'],
            help='Maximum zoom level')
    parser.add_argument('--outfile', default='index.html',
            help='Output file base name')
    parser.add_argument('--overlays', nargs='*', default="'line1'",
            action=joinArgs, 
            help='Overlay names')
    parser.add_argument('--baselayers', nargs='*', default="'continuum'",
            action=joinArgs, 
            help='Base layers names')
    parser.add_argument('outdir',
            help='Output directory name')
    args = parser.parse_args()

    # Open template
    with open(template, 'r') as tmp:
        temp = Template(''.join(tmp.readlines()))

    # Replace
    print args.overlays
    print args.baselayers
    out = temp.safe_substitute(vars(args))

    # Save
    outfile = os.path.join(os.path.expanduser(args.outdir), args.outfile)
    with open(outfile, 'w') as f:
        f.write(out)

if __name__=='__main__':
    main()
