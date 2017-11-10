""" Video game sales class file """

import numpy, pandas

class Project:
    """ Video game sales class """
    def help():
        """ Get help """
        print(" ------------------------------")
        print("   ProjectHelper Custom Module ")
        print("        for PSIT project       ")
        print("         by Teerapat K.        ")
        print(" ------------------------------")
        print("ProjectHelper.countlist(<DataFrame>, <key>, <list_of_values>)")
        print("ProjectHelper.sumlist(<DataFrame>, <key>, <list_of_values>)")

    def count_list(data_frame, key, columns):
        """ Return count """
        if len(columns) == 1:
            columns = columns[0]
        return numpy.array(data_frame.groupby(key, as_index=False).count()[columns]).tolist()

    def sum_list(data_frame, key, columns):
        """ Return sum """
        return numpy.array(data_frame.groupby(key, as_index=False).sum()[columns]).tolist()

    def platform_type(platform, convert_list=False):
        """ Return platform type """
        homeVideoGameConsoles = ['2600', '3DO', 'DC', 'GC', 'GEN', 'N64',
                                 'NES', 'NG', 'PCFX', 'PS', 'PS2', 'PS3',
                                 'PS4', 'SAT', 'SCD', 'SNES', 'TG16', 'Wii',
                                 'WiiU', 'X360', 'XB', 'XOne']
        handheldGameConsoles =  ['3DS', 'DS', 'GB', 'GBA', 'GG', 'PSP',
                                 'PSV', 'WS']
        microsoftWindows = ['PC']

        if platform in homeVideoGameConsoles:
            return 'homeVideoGameConsoles'
        elif platform in handheldGameConsoles:
            return 'handheldGameConsoles'
        elif platform in microsoftWindows:
            return 'microsoftWindows'
        else:
            return None

    def convert_platform_type(data_list, index=0):
        """ Convert all platforms to platform type of a list """
        homeVideoGameConsoles = ['2600', '3DO', 'DC', 'GC', 'GEN', 'N64',
                                 'NES', 'NG', 'PCFX', 'PS', 'PS2', 'PS3',
                                 'PS4', 'SAT', 'SCD', 'SNES', 'TG16', 'Wii',
                                 'WiiU', 'X360', 'XB', 'XOne']
        handheldGameConsoles =  ['3DS', 'DS', 'GB', 'GBA', 'GG', 'PSP',
                                 'PSV', 'WS']
        microsoftWindows = ['PC']

        for i in range(len(data_list)):
            if data_list in homeVideoGameConsoles:
                data_list[i][index] = 'homeVideoGameConsoles'
            elif data_list in handheldGameConsoles:
                data_list[i][index] = 'handheldGameConsoles'
            elif data_list in microsoftWindows:
                data_list[i][index] = 'microsoftWindows'
