"""
Created on Sep 8, 2005 in PHP
Author: Ricardo Paiva

Reimplemented on July 9, 2022 in Typescript
Author: Gabriel Paiva

Rewritten on September 7, 2022 in Python
Author: Gabriel Paiva
"""

from sys import argv

class MailGenerator:
    def __init__(self):
        self.SEPARATORS = ['', '.', '_']
        self.CONNECTORS = ['du', 'de', 'des', "l'",
                           'la', 'le', 'da', 'do', 'dos', 'das', 'of']

        self.name_list = []
        self.domain_list = []

        self.combined_names = []
        self.combined_separators = set()
        self.result = []

    def add_name(self, full_name):
        filtered_full_name = full_name
        for connector in self.CONNECTORS:
            if connector.endswith("'"):
                # remove connectors ending with <<'>>
                filtered_full_name = filtered_full_name.replace(
                    f' {connector}', ' ')
            else:
                # remove others connectors
                filtered_full_name = filtered_full_name.replace(
                    f' {connector} ', ' ')

        # split full filtered name into array
        self.name_list = filtered_full_name.split(' ')

    def add_domains(self, domains):
        self.domain_list = domains.split(' ')

    def combine_names(self):
        # single names
        for name in self.name_list:
            self.combined_names.append([name])
        # full name
        self.combined_names.append(self.name_list)

        # remove one name
        for i in range(len(self.name_list)):
            half_name = self.name_list[:]
            half_name.pop(i)
            self.combined_names.append(half_name)

        for combined_name_i in range(len(self.combined_names)):
            for name_index in range(len(self.combined_names[combined_name_i])):
                # one single letter
                new_combination = self.combined_names[combined_name_i][:]
                new_combination[name_index] = new_combination[name_index][0]
                self.combined_names.append(new_combination)

                # one entire name
                new_combination = self.combined_names[combined_name_i][:]
                for name_index2 in range(len(new_combination)):
                    if name_index == name_index2:
                        continue
                    new_combination[name_index2] = new_combination[name_index2][0]
                self.combined_names.append(new_combination)

        # reversed
        for combined_name_i in range(len(self.combined_names)):
            reversed_combination = self.combined_names[combined_name_i][::-1]
            self.combined_names.append(reversed_combination)

    def combine_separators(self):
        for separator in self.SEPARATORS:
            for combination in self.combined_names:
                self.combined_separators.add(separator.join(combination))

    def combine_domains(self):
        for domain in self.domain_list:
            for combination in self.combined_separators:
                self.result.append(f'{combination}@{domain}')

    def generate(self, names, domains):
        self.add_name(names)
        self.add_domains(domains)
        self.combine_names()
        self.combine_separators()
        self.combine_domains()
        return self.result


