import tw2.core as twc


class Dyntext(twc.Widget):
    template = "genshi:tw.dyntext.templates.dyntext"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/dyntext.js'),
        twc.CSSLink(modname=__name__, filename='static/dyntext.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Dyntext, self).prepare()
        # put code here to run just before the widget is displayed
