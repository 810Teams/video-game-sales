"""
'project' class file
designed for PSIT Project: Video Game Sales
version: 2.1
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
    url       = 'https://goo.gl/WEnczC'

    def help():
        """ Get help """
        print("Visit {} for all PSIT project documents.".format(project.url))

    def fill_missing_year(data_list):
        """ Fill missing year data by using dictionary """
        data_list = dict(data_list)
        for i in range(1980, 2017):
            if (i in data_list) == False:
                data_list[i] = 0
        return [j for j in [[i, data_list[i]] for i in sorted(data_list)] if j[0] < 2017]

    def add_relative(values):
        """ Returns an index-relative value-summed of the input list. """
        return [sum([j[i] for j in values]) for i in range(len(values[0]))]

    def platform_convert(platform):
        """ Returns a platform type of a single platform"""
        return ('Home Video Game Consoles' if platform in project.consoles
           else 'Handheld Game Consoles'   if platform in project.handhelds
           else 'Microsoft Windows'        if platform in project.windows
           else None)

    def platform_convert_df(data_frame):
        """ Returns a platform-converted data frame """
        _ = [data_frame.replace(i, 'Home Video Game Consoles', inplace=True) for i in project.consoles]
        _ = [data_frame.replace(i, 'Handheld Game Consoles',   inplace=True) for i in project.handhelds]
        _ = [data_frame.replace(i, 'Microsoft Windows',        inplace=True) for i in project.windows]
        return data_frame

    def platform_convert_list(data_list, merge=True):
        """ Convert all platforms to platform type of a list and merge"""
        index = [i for i in range(len(data_list[0])) if isinstance(data_list[0][i], str)][0]

        data_list = [data_list[i][0:index] + [project.platform_convert(data_list[i][index])] + data_list[i][index+1::] for i in range(len(data_list))]

        return [project.add_relative([i[0:index] for i in data_list if i[index] == 'Home Video Game Consoles']) + ['Home Video Game Consoles'] + project.add_relative([i[index+1::] for i in data_list if i[index] == 'Home Video Game Consoles']),
                project.add_relative([i[0:index] for i in data_list if i[index] == 'Handheld Game Consoles'])   + ['Handheld Game Consoles']   + project.add_relative([i[index+1::] for i in data_list if i[index] == 'Handheld Game Consoles']),
                project.add_relative([i[0:index] for i in data_list if i[index] == 'Microsoft Windows'])        + ['Microsoft Windows']        + project.add_relative([i[index+1::] for i in data_list if i[index] == 'Microsoft Windows'])] if merge else data_list
