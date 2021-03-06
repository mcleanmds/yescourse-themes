#!/usr/bin/env python
"""
 Read Font Awesome svg web font files to generate an SCSS map that can be used
 by the yc-icon-url() function in _icons.scss
 TODO: optimise the SVG path (perhaps using svgo)
"""
from __future__ import absolute_import, print_function, unicode_literals

from lxml import etree
import re


def main(svg_file_name, fa_vars_scss_file_name):
    # read the icon names from the vars file
    name_map = {}  # unicode id v/s name
    var_regex = re.compile(r'@fa-var-([\w-]+):\s*"(.*)"')
    with open(fa_vars_scss_file_name, 'r') as vars_file:
        for line in vars_file.readlines():
            m = var_regex.match(line)
            if not m:
                continue

            name, hex_id_str = m.groups()
            # remove the '\' in the beginning of the hex_id_str
            name_map[int(hex_id_str[1:], 16)] = name

    svg_data = []

    with open(svg_file_name, 'r') as f:
        parser = etree.XMLParser(ns_clean=True)
        tree = etree.parse(f, parser=parser)
        root = tree.getroot()
        default_ns = root.nsmap.get(None, '')

        def fqname(name):
            if default_ns:
                return '{%s}%s' % (default_ns, name)
            return name

        if root.tag != fqname('svg'):
            print ('Unknown root element %s, expect svg' % root.tag)
            return 1

        # find the font element
        font = root.find('.//' + fqname('font'))
        default_horiz_adv_x = font.get('horiz-adv-x')

        # find the font-face element
        font_face = root.find('.//' + fqname('font-face'))
        ascent = font_face.get('ascent')
        descent = font_face.get('descent')
        units_per_em = font_face.get('units-per-em')

        for child in list(font):
            if child.tag == fqname('glyph'):
                horiz_adv_x = child.get('horiz-adv-x', default_horiz_adv_x)
                if child.get('unicode'):
                    unicode_id = ord(child.get('unicode'))
                    path = child.get('d')
                    name = name_map.get(unicode_id)
                    if name and path:
                        data = {
                            'iconname': name,
                            'view_box': '0 0 %s %s' % (horiz_adv_x, units_per_em),
                            'width': horiz_adv_x,
                            'height': units_per_em,
                            'path': path,
                            'transform': 'scale(1,-1) translate(0,-%s)' % ascent,
                        }
                        svg_data.append("""
        %(iconname)s: (
            view_box: %(view_box)s,
            width: %(width)s,
            height: %(height)s,
            path: "%(path)s",
            transform: "%(transform)s"
        )""" % data)
        print ('// Auto generated by fa-svg-font-to-scss.py.')
        print ('$YC-FA_DATA: (')
        print (',\n'.join(svg_data))
        print (');')
        return 0


if __name__ == '__main__':
    import sys
    argv = sys.argv
    if len(argv) < 3:
        print ('Usage: %s <path/to/fontawesome-webfont.svg> '
               '<path/to/variables.less>' % argv[0])
        sys.exit(1)
    sys.exit(main(argv[1], argv[2]))
