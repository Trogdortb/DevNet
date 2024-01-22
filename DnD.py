import codecs

Artificer = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.3wFSjqwXndAQ8P2i]{Artificer}"
Bard = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.e3CsvRMWDlHBgznh]{Bard}"
Cleric = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.G7cm1ctzhtxEOvxS]{Cleric}"
Druid = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.1IHQ3bZ4aCi15dlH]{Druid}"
Paladin = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.W3kyKNUWc0dPFJXe]{Paladin}"
Ranger = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.e9xuvCZ8ZjUNZnwN]{Ranger}"
Sorcerer = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.NX28XQnco4pjOzF6]{Sorcerer}"
Warlock = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.JsbrmCx9VF1Sizn8]{Warlock}"
Wizard = "@UUID[Compendium.5e-complete.5e-journals.7iH4qANs2gxn0MIs.JournalEntryPage.5YX3k6END6NQWHOB]{Wizard}"

target = codecs.open('5e-spells.txt', 'r', 'utf-8')
text_utf8 = target.read()
spell = text_utf8.splitlines()
target2 = codecs.open("finished.txt", 'w', "utf-8")
# text_bytes = text_utf8.encode()
# chunks = text_bytes.split()

def url_replace(character):
    if character == "Artificer":
        return Artificer
    if character == "Bard":
        return Bard
    if character == "Cleric":
        return Cleric
    if character == "Druid":
        return Druid
    if character == "Paladin":
        return Paladin
    if character == "Ranger":
        return Ranger
    if character == "Sorcerer":
        return Sorcerer
    if character == "Warlock":
        return Warlock
    if character == "Wizard":
        return Wizard


for f in spell:
    classes = f.partition("<p><strong>Spell Lists.</strong>")[-1].partition("</p>")[0].split(", ")
    target2.write(f.partition("<p><strong>Spell Lists.</strong>")[0] + "<p><strong>Spell Lists.</strong>")
    for i in classes:
        if i.find("@") == 1:
            target2.write(i)
        else:
            replace = url_replace(i)
            if type(replace) is str:
                target2.write(replace)
    end = f.partition("<p><strong>Spell Lists.</strong>")[-1].partition("</p>")[-1]
    print(end)
    target2.write("</p>" + end + "\r")
target.close()
