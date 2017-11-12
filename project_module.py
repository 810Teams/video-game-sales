"""
'project' class file
designed for PSIT Project: Video Game Sales
version: 2.0
by Teerapat K.
"""

class project:
    """ 'project' class """
    consoles  = ['2600', '3DO', 'DC', 'GC', 'GEN', 'N64',
                 'NES', 'NG', 'PCFX', 'PS', 'PS2', 'PS3',
                 'PS4', 'SAT', 'SCD', 'SNES', 'TG16', 'Wii',
                 'WiiU', 'X360', 'XB', 'XOne']
    handhelds = ['3DS', 'DS', 'GB', 'GBA', 'GG', 'PSP',
                 'PSV', 'WS']
    windows   = ['PC']
    url       = 'https://goo.gl/PMpp2L'

    def help():
        """ Get help """
        print("Visit {} for all PSIT project documents.".format(project.url))

    def platform_convert_df(data_frame):
        """ Returns a platform-converted data frame """
        for i in project.consoles:
            data_frame = data_frame.replace(i, 'HomeVideoGameConsoles')
        for i in project.handhelds:
            data_frame = data_frame.replace(i, 'HandheldGameConsoles')
        for i in project.windows:
            data_frame = data_frame.replace(i, 'MicrosoftWindows')
        return data_frame

    #Below here are more advanced functions

    def add_relative(values):
        """ Returns an index-relative value-summed of the input list. """
        return [sum([j[i] for j in values]) for i in range(len(values[0]))]

    def platform_convert(platform):
        """ Returns a platform type of a single platform"""
        return ('HomeVideoGameConsoles' if platform in project.consoles
           else 'HandheldGameConsoles'  if platform in project.handhelds
           else 'MicrosoftWindows'      if platform in project.windows
           else None)

    def platform_convert_list(data_list, merge=True):
        """ Convert all platforms to platform type of a list and merge"""
        index = [i for i in range(len(data_list[0])) if isinstance(data_list[0][i], str)][0]

        data_list = [data_list[i][0:index] + [project.platform_convert(data_list[i][index])] + data_list[i][index+1::] for i in range(len(data_list))]

        return [project.add_relative([i[0:index] for i in data_list if i[index] == 'HomeVideoGameConsoles']) + ['HomeVideoGameConsoles'] + project.add_relative([i[index+1::] for i in data_list if i[index] == 'HomeVideoGameConsoles']),
                project.add_relative([i[0:index] for i in data_list if i[index] == 'HandheldGameConsoles'])  + ['HandheldGameConsoles']  + project.add_relative([i[index+1::] for i in data_list if i[index] == 'HandheldGameConsoles']),
                project.add_relative([i[0:index] for i in data_list if i[index] == 'MicrosoftWindows'])      + ['MicrosoftWindows']      + project.add_relative([i[index+1::] for i in data_list if i[index] == 'MicrosoftWindows'])] if merge else data_list
