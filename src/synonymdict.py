import logging
import csv

logger = logging.getLogger('SynonymDict')
logger.setLevel(logging.DEBUG)


class SynonymDict:
    """
    Class that load synonyms lists form CSV file and return them as a dictionary
    """

    def __init__(self):
        self.dict = list()
        logger.debug('{} created!'.format(self.__class__.__name__))

    def __str__(self):
        return str(self.dict)

    def load_synonyms(self, loaded_dict):
        # obsolate
        # for dic in loaded_dict:
        #     self.dict.append(dic)
        spamreader = csv.reader(loaded_dict, delimiter=';')
        for x in spamreader:
            self.dict.append(x)

    def load_from_file(self, file_path, delimiter=';'):
        """
        Loads synonyms from CSV file
        """
        logger.debug('Loading from: {}'.format(file_path))
        logger.debug('Before: {}'.format(str(self.dict)))
        with open(file_path, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=delimiter)
            for x in spamreader:
                self.dict.append(x)
        logger.debug('Loaded into dictionary: {}'.format(str(self.dict)))

    def synonyms(self, words):
        """
        Returns a dictionary wheres key is word and value is list of synonyms 
        """
        d = {}
        if type(words) != list:
            tmp = words
            words = list()
            words.append(tmp)

        for word in words:
            d[word] = list()
            for synonyms in self.dict:
                if word in synonyms:
                    d[word].extend(filter(lambda x: x != word, synonyms))
        return d

    def is_synonym(self, firstWord, secondWord):
        """
        Returns True if words are synonyms or False if they don't
        """
        # logging.debug('If {} in: '.format(firstWord) + str(self.synonyms(secondWord)[secondWord]))
        # logging.debug('If {} in: '.format(secondWord) + str(self.synonyms(firstWord)[firstWord]))
        if firstWord in self.synonyms(secondWord)[secondWord] \
                or secondWord in self.synonyms(firstWord)[firstWord]:
            return True
        else:
            return False

    def clear(self):
        """
        Clears build in synonyms lists
        """
        self.dict = list()


# if __name__ == '__main__':
#     dic = SynonymDict()
#     dic.load_from_file('test_dic.csv')
#     print dic
#     print '\n'
    # print dic.synonyms(sys.argv[1:])

    # print dic.is_synonym(sys.argv[1], sys.argv[2])
