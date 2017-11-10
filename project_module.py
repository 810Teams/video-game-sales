"""
'project' class file
designed for PSIT Project: Video Game Sales
by Teerapat K.
"""

import numpy, pandas

class project:
    """ 'project' class """
    platform_types = ['HomeVideoGameConsoles', 'HandheldGameConsoles', 'MicrosoftWindows']
    consoles  = ['2600', '3DO', 'DC', 'GC', 'GEN', 'N64',
                 'NES', 'NG', 'PCFX', 'PS', 'PS2', 'PS3',
                 'PS4', 'SAT', 'SCD', 'SNES', 'TG16', 'Wii',
                 'WiiU', 'X360', 'XB', 'XOne']
    handhelds = ['3DS', 'DS', 'GB', 'GBA', 'GG', 'PSP',
                 'PSV', 'WS']
    windows   = ['PC']

    def help():
        """ Get help """
        print(" --------------------------")
        print("  'Project' Custom Module  ")
        print("      for PSIT project     ")
        print("       by Teerapat K.      ")
        print(" --------------------------\n")

        print(" project.platform_types")
        print(" project.consoles")
        print(" project.handhelds")
        print(" project.windows\n")

        print(" project.count_list(<DataFrame>, <key>, <list_of_values>)")
        print("  --> Returns a counted data frame in list format.\n")

        print(" project.sum_list(<DataFrame>, <key>, <list_of_values>)")
        print("  --> Returns a summed data frame in list format.\n")

        print(" project.add_relative(<list>)")
        print("  --> Returns an index-relative value-summed of the input list.")
        print("  --> EXAMPLE: pass-in: [[a, b, c], [d, e, f], [g, h, i]]")
        print("               returns: [a+d+g, b+e+h, c+f+i]\n")

        print(" project.platform_convert(<platform>)")
        print("  --> Returns a platform type from a single platform.\n")

        print(" project.platform_convert_list(<data_list>, merge=True)")
        print("  --> Returns a data-merged list, which platforms have been converted to platform types.")
        print("  --> WARNING: Index 0 must be <platform>, other indexes must be a 'int' or 'float'.")
        print("  --> EXAMPLE: [[<platform>, <int/float values>, ...], ...]\n")

    def count_list(data_frame, key, columns):
        """ Return count """
        if len(columns) == 1:
            columns = columns[0]
        return numpy.array(data_frame.groupby(key, as_index=False).count()[columns]).tolist()

    def sum_list(data_frame, key, columns):
        """ Return sum """
        if len(columns) == 1:
            columns = columns[0]
        return numpy.array(data_frame.groupby(key, as_index=False).sum()[columns]).tolist()

    def add_relative(values):
        """ Add a[i] with b[i] to get x[i] """
        return [sum([j[i] for j in values]) for i in range(len(values[0]))]

    def platform_convert(platform):
        """ Return platform type of a single platform"""
        return ('HomeVideoGameConsoles' if platform in project.consoles
           else 'HandheldGameConsoles'  if platform in project.handhelds
           else 'MicrosoftWindows'      if platform in project.windows
           else None)

    def platform_convert_list(data_list, merge=True):
        """ Convert all platforms to platform type of a list and merge"""
        data_list = [[project.platform_convert(data_list[i][0])]+data_list[i][1::] for i in range(len(data_list))]

        return [['HomeVideoGameConsoles'] + project.add_relative([i[1::] for i in data_list if i[0] == 'HomeVideoGameConsoles']),
                ['HandheldGameConsoles']  + project.add_relative([i[1::] for i in data_list if i[0] == 'HandheldGameConsoles']),
                ['MicrosoftWindows']      + project.add_relative([i[1::] for i in data_list if i[0] == 'MicrosoftWindows'])] if merge else data_list
