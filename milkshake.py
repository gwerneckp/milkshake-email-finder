"""
Created on Sep 8, 2005 in PHP
Author: Ricardo Paiva

Reimplemented on July 9, 2022 in Typescript
Author: Gabriel Paiva

Rewritten on September 7, 2022 in Python
Author: Gabriel Paiva
"""

import unittest


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

    def add_domain(self, domains):
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
        self.add_domain(domains)
        self.combine_names()
        self.combine_separators()
        self.combine_domains()
        return self.result


class TestEmails(unittest.TestCase):
    def test_single_name(self):
        mb = MailGenerator()
        mb.add_name("gabriel")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['gabriel'], mb.combined_names)

    def test_single_name_from_full_name(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['gabriel'], mb.combined_names)

    def test_full_name_from_full_name(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['gabriel', 'werneck'], mb.combined_names)

    def test_full_name_three_names(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck paiva")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['gabriel', 'werneck', 'paiva'], mb.combined_names)

    def test_half_name_with_full_name(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck paiva")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['gabriel', 'werneck'], mb.combined_names)

    def test_first_name_one_letter(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['g', 'werneck'], mb.combined_names)

    def test_my_email(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck paiva")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['g', 'werneck', 'paiva'], mb.combined_names)

    def test_middle_letter(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck paiva")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['gabriel', 'w', 'paiva'], mb.combined_names)

    def test_one_name_big(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck paiva")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['g', 'w', 'paiva'], mb.combined_names)

    def test_simple_reverse(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['werneck', 'gabriel'], mb.combined_names)

    def test_reverse_complex(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck paiva")
        mb.add_domain('gmail.com')
        mb.combine_names()
        self.assertIn(['paiva', 'werneck', 'g'], mb.combined_names)

    def test_combined_separators(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck paiva")
        mb.add_domain('gmail.com')
        mb.combine_names()
        mb.combine_separators()
        self.assertIn('gwerneckpaiva', mb.combined_separators)

    def test_result(self):
        mb = MailGenerator()
        mb.add_name("gabriel werneck paiva")
        mb.add_domain('gmail.com')
        mb.combine_names()
        mb.combine_separators()
        mb.combine_domains()
        self.assertIn('gwerneckpaiva@gmail.com', mb.result)


if __name__ == "__main__":
    unittest.main()
