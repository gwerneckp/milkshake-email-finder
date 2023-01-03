import unittest
from milkshake import MailGenerator


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


if __name__ == '__main__':
    unittest.main()
