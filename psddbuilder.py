import csv


class PSDD:
    '''Device Class'''

    def __init__(self, source_host, source_ip, dst_host, dst_ip, application, port, comment):
        '''line of psdd'''
        self.source_host = source_host
        self.source_ip = source_ip
        self.dst_host = dst_host
        self.dst_ip = dst_ip
        self.application = application
        self.port = port
        self.comment = comment


psdd_doc = csv.reader(open('psdd.csv'))

rules = []

for row in psdd_doc:
    psdd_line = PSDD(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    rulename = psdd_line.comment.replace(' ', '-')
    source_name = (f"{psdd_line.source_host}-{psdd_line.source_ip}")
    destination_name = (f"{psdd_line.dst_host}-{psdd_line.dst_ip}")
    rule_exist = False
    for rule in rules:
        if rule['name'] == rulename:
            rule['src'] = (f"{rule['src']} {source_name}")
            rule['dst'] = (f"{rule['dst']} {destination_name}")
            rule_exist = True
            break
    if rule_exist == False:
        rules.append({'name': rulename, 'src': source_name, 'dst': destination_name,
                      'application': psdd_line.application, 'port': psdd_line.port, 'comment': psdd_line.comment})
        rule_exist = False

for line in rules:
    clean_src = ' '.join(set(line['src'].split()))
    clean_dst = ' '.join(set(line['dst'].split()))
    print(f"set rulebase security rules {line['name']} comment \"{line['comment']}\"")
    print(f"set rulebase security rules {line['name']} from [ {clean_src} ]")
    print(f"set rulebase security rules {line['name']} to [ {clean_dst} ]")
    print(f"set rulebase security rules {line['name']} application {line['application']}")
    print(f"set rulebase security rules {line['name']} port {line['port']}")
