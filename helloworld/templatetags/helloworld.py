# Copyright (C) 2009  David Roberts <d@vidr.cc>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random

from django import template

register = template.Library()

items = (
    # from <http://helloworldsite.he.funpic.de/hello.htm#Human>
    ('Albanian',        u'Persh\xebndetje Bot\xeb'),
    ('Armenian',        u'\u0532\u0561\u0580\u0565\u055b\u0582, '
                        u'\u0561\u0577\u056d\u0561\u0580\u0570\u0589'),
    ('Azeri',           u'Salam D\xfcnya'),
    ('Czech',           u'Ahoj Sv\u011bte!'),
    ('Basque/Euskara',  u'Kaixo mundua!'),
    ('Bemba',           u'Shani Mwechalo!'),
    ('Bengali',         u'Shagatam Prithivi!'),
    ('Bosnian',         u'Zdravo Svijete!'),
    ('Catalan',         u'Hola m\xf3n!'),
    ('Croatian',        u'Bok Svijete!'),
    ('Danish',          u'Hej, Verden!'),
    ('Dutch',           u'Hallo, wereld!'),
    ('English',         u'Hello World!'),
    ('Esperanto',       u'Saluton mondo!'),
    ('Estonian',        u'Tere maailm!'),
    ('Finnish',         u'Hei maailma!'),
    ('French',          u'Salut le Monde!'),
    ('Frisian',         u'Hallo, wr\xe2ld!'),
    ('Galician',        u'Ola mundo!'),
    ('German',          u'Hallo Welt!'),
    ('Greek',           u'\u0393\u03b5\u03b9\u03b1 \u03c3\u03bf\u03c5 '
                        u'\u03ba\u03cc\u03c3\u03bc\u03b5!'),
    ('Hawaiian',        u'Aloha Honua'),
    ('Hmong',           u'Nyob zoo ntiaj teb.'),
    ('Hungarian',       u'Hell\xf3 vil\xe1g!'),
    ('Icelandic',       u'Hall\xf3 heimur!'),
    ('Indonesian',      u'Halo Dunia!'),
    ('Irish',           u'Dia dhaoibh, a dhomhain!'),
    ('Italian',         u'Ciao Mondo!'),
    ('Kiswahili',       u'Habari dunia!'),
    ('Kikuyu',          u'Niatia thi!'),
    ('Latin',           u'AVE MVNDE'),
    ('Latvian',         u'Sveika, Pasaule!'),
    ('Lithuanian',      u'Sveikas, Pasauli'),
    ('Luxembourgish',   u'Moien Welt!'),
    ('Malagasy',        u'Manao ahoana ry tany!'),
    ('Malayalam',       u'Namaskaram, lokame'),
    ('Maltese',         u'Merhba lid-dinja'),
    ('Norwegian',       u'Hallo verden!'),
    #('Persian',         u'!\u0633\u0644\u0627\u0645 '
    #                    u'\u062f\u0646\u06cc\u0627'),
    ('Polish',          u'Witaj, Swiecie!'),
    ('Portuguese',      u'Ol\xe1, mundo!'),
    ('Romanian',        u'Salut lume!'),
    ('Serbian',         u'Zdravo Svete!'),
    ('Slovak',          u'Ahoj, svet!'),
    ('Slovenian',       u'Pozdravljen svet!'),
    ('Spanish',         u'\xa1Hola mundo!'),
    ('Swedish',         u'Hejsan v\xe4rlden!'),
    ('Tagalog',         u'Kamusta mundo!'),
    ('Turkish',         u'Merhaba D\xfcnya!'),
    ('Vietnamese',      u'Xin ch\xe0o th\u1ebf gi\u1edbi'),
    ('Welsh',           u'S\'mae byd!'),
)

@register.simple_tag
def helloworld():
    lang, phrase = random.choice(items)
    phrase = phrase.encode('ascii', 'xmlcharrefreplace')
    return '<h2>' + phrase + '</h2> <!-- "Hello World!" in ' + lang + ' -->'
