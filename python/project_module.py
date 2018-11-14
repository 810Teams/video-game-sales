"""
    Project Class File (project)
    Designed for PSIT Project - Video Game Sales
    Version: 2.2.0
    by Teerapat Kraisrisirikul (810Teams)
"""

import numpy, pandas

class project:
    """ 'project' class """
    consoles  = ['2600', '3DO', 'DC', 'GC', 'GEN', 'N64',
                 'NES', 'NG', 'PCFX', 'PS', 'PS2', 'PS3',
                 'PS4', 'SAT', 'SCD', 'SNES', 'TG16', 'Wii',
                 'WiiU', 'X360', 'XB', 'XOne', 'X']
    handhelds = ['3DS', 'DS', 'GB', 'GBA', 'GG', 'PSP',
                 'PSV', 'WS', 'G']
    windows   = ['PC']

    def fill_missing_year(data_list):
        """ Fill missing year data by using dictionary """
        data_list = [[int(float(i[0])), i[1]] for i in data_list]
        data_list = dict(data_list)
        for i in range(1980, 2017):
            if (i not in data_list):
                data_list[i] = 0
        return [j for j in [[i, data_list[i]] for i in sorted(data_list)] if j[0] < 2017 and j[0] >= 1980]

    def platform_convert(platform):
        """ Returns a platform type of a single platform"""
        if platform in project.consoles:
            return 'Home Video Game Consoles'
        elif platform in project.handhelds:
            return 'Handheld Game Consoles'
        elif platform in project.windows:
            return 'Microsoft Windows'
        return None

    def platform_convert_df(df):
        """ Returns a platform-converted data frame """
        for i in project.consoles:
            df.replace(i, 'Home Video Game Consoles', inplace=True)
        for i in project.handhelds:
            df.replace(i, 'Handheld Game Consoles', inplace=True)
        for i in project.windows:
            df.replace(i, 'Microsoft Windows', inplace=True)
        return df
