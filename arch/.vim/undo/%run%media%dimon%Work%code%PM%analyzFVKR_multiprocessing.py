Vim�UnDo� ��ƾ�J���?'Ul�n�8�x�P���' ��  �   /        filter2 = df["пол"].isin(["Жен"])  �   (                       c���    _�                             ����                                                                                                                                                                                                                                                                                                                                                             c��[    �  �               �      �       �              �   	import os   import pandas as pd   import numpy as np    from multiprocessing import Pool   from icecream import ic   import glob   import timeit           EVENTS_AGE = (       # [10, 11],       # [8, 9],        [12, 13],        [14, 15],      [16, 17],       # [16, 99],   )   df = pd.DataFrame()           !def count_score_kumite(df_count):       conditions = [   7        (df_count["Занятое \nместо"] == 1),   7        (df_count["Занятое \nместо"] == 2),   7        (df_count["Занятое \nместо"] == 3),   7        (df_count["Занятое \nместо"] == 4),   7        (df_count["Занятое \nместо"] == 5),   7        (df_count["Занятое \nместо"] == 9),   ;        (df_count["Занятое \nместо"] == "nan"),   9        (df_count["Занятое \nместо"] == "1"),   9        (df_count["Занятое \nместо"] == "2"),   9        (df_count["Занятое \nместо"] == "3"),   9        (df_count["Занятое \nместо"] == "4"),   9        (df_count["Занятое \nместо"] == "5"),   ;        (df_count["Занятое \nместо"] == "5-6"),   ;        (df_count["Занятое \nместо"] == "5-7"),   ;        (df_count["Занятое \nместо"] == "5-8"),   9        (df_count["Занятое \nместо"] == "9"),   <        (df_count["Занятое \nместо"] == "9-10"),   <        (df_count["Занятое \nместо"] == "9-11"),   <        (df_count["Занятое \nместо"] == "9-12"),   <        (df_count["Занятое \nместо"] == "9-13"),   <        (df_count["Занятое \nместо"] == "9-14"),   <        (df_count["Занятое \nместо"] == "9-15"),   <        (df_count["Занятое \nместо"] == "9-16"),       ]       values = [   
        5,   
        3,   
        1,           12,           10,   
        5,   
        0,           17,           14,           13,           12,           10,           10,           10,           10,   
        5,   
        5,   
        5,   
        5,   
        5,   
        5,   
        5,   
        5,       ]       # values = [       #     17,       #     14,       #     13,       #     12,       #     # 9,       #     # 8,       #     7,       #     7,       #     7,       #     3,       #     1,       #     7,       #     7,       #     7,       #     7,       #     3,       #     3,       #     3,       #     3,       #     3,       #     3,       #     3,       # ]   8    df_count["Очки"] = np.select(conditions, values)       return df_count           def count_score_kata(df_count):       conditions = [   7        (df_count["Занятое \nместо"] == 1),   7        (df_count["Занятое \nместо"] == 2),   7        (df_count["Занятое \nместо"] == 3),   7        (df_count["Занятое \nместо"] == 4),   7        (df_count["Занятое \nместо"] == 5),   7        (df_count["Занятое \nместо"] == 6),   7        (df_count["Занятое \nместо"] == 7),   7        (df_count["Занятое \nместо"] == 8),   7        (df_count["Занятое \nместо"] == 9),   8        (df_count["Занятое \nместо"] == 10),   8        (df_count["Занятое \nместо"] == 11),   8        (df_count["Занятое \nместо"] == 12),   8        (df_count["Занятое \nместо"] == 13),   8        (df_count["Занятое \nместо"] == 14),   8        (df_count["Занятое \nместо"] == 15),   8        (df_count["Занятое \nместо"] == 16),   ;        (df_count["Занятое \nместо"] == "nan"),       ]       values = [           17,           14,           13,           12,   
        9,   
        8,   
        7,   
        6,   
        5,   
        4,   
        3,   
        2,   
        2,   
        2,   
        2,   
        2,   
        0,       ]   8    df_count["Очки"] = np.select(conditions, values)       return df_count           def scoring(df):       region_more = []       region_less = []   >    for idx, row in df["Регион"].value_counts().items():           if row > 2:   #            region_more.append(idx)           else:   #            region_less.append(idx)   &    df_correct_region = pd.DataFrame()       df_first = pd.DataFrame()       df_second = pd.DataFrame()       for region in region_less:   6        more_region = df[df["Регион"] == region]   ]        df_correct = more_region.sort_values(["Регион", "Занятое \nместо"])   F        df_correct_region = pd.concat([df_correct_region, df_correct])       for region in region_more:   6        more_region = df[df["Регион"] == region]   ^        df_more = more_region.sort_values(["Регион", "Занятое \nместо"])[:2]   ^        df_less = more_region.sort_values(["Регион", "Занятое \nместо"])[2:]   1        df_first = pd.concat([df_first, df_more])   3        df_second = pd.concat([df_second, df_less])   7    df_count = pd.concat([df_correct_region, df_first])   8    cleanedlist = df_count.iloc[:, 10].unique().tolist()   (    if not "ката" in cleanedlist[0]:   /        df_count = count_score_kumite(df_count)   	    else:   -        df_count = count_score_kata(df_count)        df_second["Очки"] = None   B    concatRes = pd.concat([df_count, df_second]).drop_duplicates()       return concatRes           9# wrap your csv importer in a function that can be mapped   def read_excel(filename):   /    "converts a filename to a pandas dataframe"       global df       ic(filename)   L    da = pd.read_excel(filename, header=6, engine="openpyxl", usecols="A:N")       da = da.set_axis(   	        [               "№",               "№ жреб.",               "пол",               "Фамилия",               "Имя",               "Отчество",   (            "Дата рождения",   "            "Полных лет",   )            "Разряд, звание",   "            "Точный вес",   (            "Вид программы",               "Регион",               "Тренер",   *            "Занятое \nместо",   
        ],           axis=1,       )   -    df = da.dropna(subset=["Фамилия"])       result_frame = scoring(df)       return result_frame           # общий список   def work(df):       global list_all   A    list_all = df.sort_values(["Регион", "Фамилия"])   1    list_all.reset_index(drop=True, inplace=True)       list_all.index += 1   C    list_all.to_excel(writer, sheet_name="Общий список")       return list_all           =# регионы и количество участников   def regions(df):       global region       global rr   i    region = df.groupby(["Регион"]).size().to_frame(name="Виды программ").reset_index()   /    region.reset_index(drop=True, inplace=True)       region.index += 1   8    region.to_excel(writer, sheet_name="Регионы")   X    ic("Всего спортсменов: ", region["Виды программ"].sum())       %    # Поиск дубликатов       data = df[   	        [               "пол",               "Фамилия",               "Имя",               "Отчество",   (            "Дата рождения",   "            "Полных лет",   )            "Разряд, звание",               "Регион",   	        ]       ]   \    ic("Всего дубликатов будет убрано: ", data.duplicated().sum())       rr = data.drop_duplicates()   e    region_rr = rr.groupby(["Регион"]).size().to_frame(name="Участники").reset_index()   2    region_rr.reset_index(drop=True, inplace=True)       region_rr.index += 1   s    ic("Количество уникальных спортсменов: ", region_rr["Участники"].sum())   )    rr.to_excel(writer, sheet_name="Dup")   5    region_rr.to_excel(writer, sheet_name="Люди")           3# количество мужчин и женщин   def gender():   b    get_gender = rr.groupby(["пол"]).size().to_frame(name="Количество").reset_index()   N    get_gender.to_excel(writer, sheet_name="Мужчины и женщины")           def list_results(df):       results = pd.DataFrame()   2    cleanedlist = df.iloc[:, 10].unique().tolist()   4    results_gender = df.iloc[:, 2].unique().tolist()   1    results_age = df.iloc[:, 7].unique().tolist()       ic(results_age)       if len(results_age) > 2:   1        results_list = f"{results_gender[0]}_18+"   	    else:   C        results_list = f"{results_gender[0]}_{int(results_age[0])}"   M    sport_discipline = [x for x in cleanedlist if str(x) != "nan" and "None"]       sport_discipline.sort()   '    for discipline in sport_discipline:   1        df_all = df[df.iloc[:, 10] == discipline]           data = (               df_all[                   [   0                    "Вид программы",                       "пол",   %                    "Фамилия",                       "Имя",   '                    "Отчество",   #                    "Регион",   2                    "Занятое \nместо",                   ]               ]   I            .sort_values(["Занятое \nместо", "Регион"])               .head(4)   	        )   f        data["ФИО"] = data["Фамилия"].str.cat(data[["Имя", "Отчество"]], sep=" ")   R        data["ФИО"] = data["ФИО"].str.cat(data[["Регион"]], sep=" \n")   ,        results = pd.concat([results, data])       try:   .        results = results.reset_index().pivot(   g            index="Вид программы", columns="Занятое \nместо", values=["ФИО"]   	        )       except ValueError:   8        ic("нет проставленных мест")   5    results.to_excel(writer, sheet_name=results_list)           ,# статистика по разрядам   def sport():       item = (   m        rr.groupby(["Разряд, звание"]).size().to_frame(name="Количество").reset_index()       )   6    item.to_excel(writer, sheet_name="Разряды")           # занятые места   def medalscommonlist(df):       global medal       medal = (   C        df.groupby(["Регион", "Занятое \nместо"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   s    medal = medal.pivot(index="Регион", columns="Занятое \nместо", values="Количество")   5    medal.to_excel(writer, sheet_name="Медали")           *# Общий командный зачет   def zachet(xlsx_files):           global zachet_all       list = (   U        list_all.groupby(["Регион", "Занятое \nместо", "Очки"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   ?    temp_diff = list["Очки"] * list["Количество"]   "    list["Сумма"] = temp_diff   ,    z = list[["Регион", "Сумма"]]   )    z = z.groupby(["Регион"]).sum()       all = pd.DataFrame(z)   !    all.reset_index(inplace=True)   A    zachet_all = all.sort_values(["Сумма"], ascending=False)   3    zachet_all.reset_index(drop=True, inplace=True)       zachet_all.index += 1   D    ic("Количество категорий: ", len(xlsx_files))       ic(zachet_all)   K    zachet_all.to_excel(writer, sheet_name="Командный зачет")           
def pol():           dataroz = (   A        rr.groupby(["Регион", "Дата рождения"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   n    dataroz["Дата рождения"] = pd.to_datetime(dataroz["Дата рождения"], dayfirst=True)   L    dataroz["Data"] = dataroz["Дата рождения"].dt.strftime("%Y")       dataroz = (   1        dataroz.groupby(["Регион", "Data"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   `    dataroz = dataroz.pivot(index="Регион", columns="Data", values="Количество")   k    pol = rr.groupby(["Регион", "пол"]).size().to_frame(name="Количество").reset_index()       raz = (   B        rr.groupby(["Регион", "Разряд, звание"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   Z    pol = pol.pivot(index="Регион", columns="пол", values="Количество")   n    raz = raz.pivot(index="Регион", columns="Разряд, звание", values="Количество")   C    pol.to_excel(writer, sheet_name="ПОЛ по регионам")   K    raz.to_excel(writer, sheet_name="Разряды по регионам")   X    dataroz.to_excel(writer, sheet_name="Год рождения по регионам")           1# with pd.ExcelWriter("итог.xlsx") as writer:   #     df.to_excel(writer)   =writer = pd.ExcelWriter("итог.xlsx", engine="xlsxwriter")   "starttime = timeit.default_timer()           def main():           # get a list of file names       xlsx_files = []       xlsx_files = [   l        y for x in os.walk("Отчет/Протоколы") for y in glob.glob(os.path.join(x[0], "*.xlsx"))       ]   V    ic("________________Количество категорий____", len(xlsx_files))           # set up your pool   L    with Pool(processes=8) as pool:  # or whatever your hardware can support       9        # have your pool map the file names to dataframes   2        df_list = pool.map(read_excel, xlsx_files)       =        # reduce the list of dataframes to a single dataframe   2        df = pd.concat(df_list, ignore_index=True)   /        filter1 = df["пол"].isin(["Муж"])   /        filter2 = df["пол"].isin(["Жен"])           man = df[filter1]           women = df[filter2]           work(df)           for i in EVENTS_AGE:   O            frame = man[man["Полных лет"].isin(range(i[0], i[1] + 1))]   =            # frame = man[man["Полных лет"].isin(i)]               list_results(frame)           for i in EVENTS_AGE:   S            frame = women[women["Полных лет"].isin(range(i[0], i[1] + 1))]   A            # frame = women[women["Полных лет"].isin(i)]               list_results(frame)           work(df)           regions(df)           gender()           sport()           medalscommonlist(df)           zachet(xlsx_files)           # pol()           if __name__ == "__main__":   
    main()       writer.save()   b    ic("Время выполнения программы :", timeit.default_timer() - starttime)5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             c��r    �  ~  �  �      9        for x in os.walk("Отчет/Протоколы")5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             c��s    �  ~  �  �      /        for x in os.walk("/Протоколы")5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             c��t    �  �               �      �       �              �   	import os   import pandas as pd   import numpy as np    from multiprocessing import Pool   from icecream import ic   import glob   import timeit           EVENTS_AGE = (       # [10, 11],       # [8, 9],       [12, 13],       [14, 15],       [16, 17],       # [16, 99],   )   df = pd.DataFrame()           !def count_score_kumite(df_count):       conditions = [   7        (df_count["Занятое \nместо"] == 1),   7        (df_count["Занятое \nместо"] == 2),   7        (df_count["Занятое \nместо"] == 3),   7        (df_count["Занятое \nместо"] == 4),   7        (df_count["Занятое \nместо"] == 5),   7        (df_count["Занятое \nместо"] == 9),   ;        (df_count["Занятое \nместо"] == "nan"),   9        (df_count["Занятое \nместо"] == "1"),   9        (df_count["Занятое \nместо"] == "2"),   9        (df_count["Занятое \nместо"] == "3"),   9        (df_count["Занятое \nместо"] == "4"),   9        (df_count["Занятое \nместо"] == "5"),   ;        (df_count["Занятое \nместо"] == "5-6"),   ;        (df_count["Занятое \nместо"] == "5-7"),   ;        (df_count["Занятое \nместо"] == "5-8"),   9        (df_count["Занятое \nместо"] == "9"),   <        (df_count["Занятое \nместо"] == "9-10"),   <        (df_count["Занятое \nместо"] == "9-11"),   <        (df_count["Занятое \nместо"] == "9-12"),   <        (df_count["Занятое \nместо"] == "9-13"),   <        (df_count["Занятое \nместо"] == "9-14"),   <        (df_count["Занятое \nместо"] == "9-15"),   <        (df_count["Занятое \nместо"] == "9-16"),       ]       values = [   
        5,   
        3,   
        1,           12,           10,   
        5,   
        0,           17,           14,           13,           12,           10,           10,           10,           10,   
        5,   
        5,   
        5,   
        5,   
        5,   
        5,   
        5,   
        5,       ]       # values = [       #     17,       #     14,       #     13,       #     12,       #     # 9,       #     # 8,       #     7,       #     7,       #     7,       #     3,       #     1,       #     7,       #     7,       #     7,       #     7,       #     3,       #     3,       #     3,       #     3,       #     3,       #     3,       #     3,       # ]   8    df_count["Очки"] = np.select(conditions, values)       return df_count           def count_score_kata(df_count):       conditions = [   7        (df_count["Занятое \nместо"] == 1),   7        (df_count["Занятое \nместо"] == 2),   7        (df_count["Занятое \nместо"] == 3),   7        (df_count["Занятое \nместо"] == 4),   7        (df_count["Занятое \nместо"] == 5),   7        (df_count["Занятое \nместо"] == 6),   7        (df_count["Занятое \nместо"] == 7),   7        (df_count["Занятое \nместо"] == 8),   7        (df_count["Занятое \nместо"] == 9),   8        (df_count["Занятое \nместо"] == 10),   8        (df_count["Занятое \nместо"] == 11),   8        (df_count["Занятое \nместо"] == 12),   8        (df_count["Занятое \nместо"] == 13),   8        (df_count["Занятое \nместо"] == 14),   8        (df_count["Занятое \nместо"] == 15),   8        (df_count["Занятое \nместо"] == 16),   ;        (df_count["Занятое \nместо"] == "nan"),       ]       values = [           17,           14,           13,           12,   
        9,   
        8,   
        7,   
        6,   
        5,   
        4,   
        3,   
        2,   
        2,   
        2,   
        2,   
        2,   
        0,       ]   8    df_count["Очки"] = np.select(conditions, values)       return df_count           def scoring(df):       region_more = []       region_less = []   >    for idx, row in df["Регион"].value_counts().items():           if row > 2:   #            region_more.append(idx)           else:   #            region_less.append(idx)   &    df_correct_region = pd.DataFrame()       df_first = pd.DataFrame()       df_second = pd.DataFrame()       for region in region_less:   6        more_region = df[df["Регион"] == region]   ]        df_correct = more_region.sort_values(["Регион", "Занятое \nместо"])   F        df_correct_region = pd.concat([df_correct_region, df_correct])       for region in region_more:   6        more_region = df[df["Регион"] == region]   ^        df_more = more_region.sort_values(["Регион", "Занятое \nместо"])[:2]   ^        df_less = more_region.sort_values(["Регион", "Занятое \nместо"])[2:]   1        df_first = pd.concat([df_first, df_more])   3        df_second = pd.concat([df_second, df_less])   7    df_count = pd.concat([df_correct_region, df_first])   8    cleanedlist = df_count.iloc[:, 10].unique().tolist()   (    if not "ката" in cleanedlist[0]:   /        df_count = count_score_kumite(df_count)   	    else:   -        df_count = count_score_kata(df_count)        df_second["Очки"] = None   B    concatRes = pd.concat([df_count, df_second]).drop_duplicates()       return concatRes           9# wrap your csv importer in a function that can be mapped   def read_excel(filename):   /    "converts a filename to a pandas dataframe"       global df       ic(filename)   L    da = pd.read_excel(filename, header=6, engine="openpyxl", usecols="A:N")       da = da.set_axis(   	        [               "№",               "№ жреб.",               "пол",               "Фамилия",               "Имя",               "Отчество",   (            "Дата рождения",   "            "Полных лет",   )            "Разряд, звание",   "            "Точный вес",   (            "Вид программы",               "Регион",               "Тренер",   *            "Занятое \nместо",   
        ],           axis=1,       )   -    df = da.dropna(subset=["Фамилия"])       result_frame = scoring(df)       return result_frame           # общий список   def work(df):       global list_all   A    list_all = df.sort_values(["Регион", "Фамилия"])   1    list_all.reset_index(drop=True, inplace=True)       list_all.index += 1   C    list_all.to_excel(writer, sheet_name="Общий список")       return list_all           =# регионы и количество участников   def regions(df):       global region       global rr   i    region = df.groupby(["Регион"]).size().to_frame(name="Виды программ").reset_index()   /    region.reset_index(drop=True, inplace=True)       region.index += 1   8    region.to_excel(writer, sheet_name="Регионы")   X    ic("Всего спортсменов: ", region["Виды программ"].sum())       %    # Поиск дубликатов       data = df[   	        [               "пол",               "Фамилия",               "Имя",               "Отчество",   (            "Дата рождения",   "            "Полных лет",   )            "Разряд, звание",               "Регион",   	        ]       ]   \    ic("Всего дубликатов будет убрано: ", data.duplicated().sum())       rr = data.drop_duplicates()   e    region_rr = rr.groupby(["Регион"]).size().to_frame(name="Участники").reset_index()   2    region_rr.reset_index(drop=True, inplace=True)       region_rr.index += 1   s    ic("Количество уникальных спортсменов: ", region_rr["Участники"].sum())   )    rr.to_excel(writer, sheet_name="Dup")   5    region_rr.to_excel(writer, sheet_name="Люди")           3# количество мужчин и женщин   def gender():   b    get_gender = rr.groupby(["пол"]).size().to_frame(name="Количество").reset_index()   N    get_gender.to_excel(writer, sheet_name="Мужчины и женщины")           def list_results(df):       results = pd.DataFrame()   2    cleanedlist = df.iloc[:, 10].unique().tolist()   4    results_gender = df.iloc[:, 2].unique().tolist()   1    results_age = df.iloc[:, 7].unique().tolist()       ic(results_age)       if len(results_age) > 2:   1        results_list = f"{results_gender[0]}_18+"   	    else:   C        results_list = f"{results_gender[0]}_{int(results_age[0])}"   M    sport_discipline = [x for x in cleanedlist if str(x) != "nan" and "None"]       sport_discipline.sort()   '    for discipline in sport_discipline:   1        df_all = df[df.iloc[:, 10] == discipline]           data = (               df_all[                   [   0                    "Вид программы",                       "пол",   %                    "Фамилия",                       "Имя",   '                    "Отчество",   #                    "Регион",   2                    "Занятое \nместо",                   ]               ]   I            .sort_values(["Занятое \nместо", "Регион"])               .head(4)   	        )   f        data["ФИО"] = data["Фамилия"].str.cat(data[["Имя", "Отчество"]], sep=" ")   R        data["ФИО"] = data["ФИО"].str.cat(data[["Регион"]], sep=" \n")   ,        results = pd.concat([results, data])       try:   .        results = results.reset_index().pivot(   g            index="Вид программы", columns="Занятое \nместо", values=["ФИО"]   	        )       except ValueError:   8        ic("нет проставленных мест")   5    results.to_excel(writer, sheet_name=results_list)           ,# статистика по разрядам   def sport():       item = (   m        rr.groupby(["Разряд, звание"]).size().to_frame(name="Количество").reset_index()       )   6    item.to_excel(writer, sheet_name="Разряды")           # занятые места   def medalscommonlist(df):       global medal       medal = (   C        df.groupby(["Регион", "Занятое \nместо"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   s    medal = medal.pivot(index="Регион", columns="Занятое \nместо", values="Количество")   5    medal.to_excel(writer, sheet_name="Медали")           *# Общий командный зачет   def zachet(xlsx_files):           global zachet_all       list = (   U        list_all.groupby(["Регион", "Занятое \nместо", "Очки"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   ?    temp_diff = list["Очки"] * list["Количество"]   "    list["Сумма"] = temp_diff   ,    z = list[["Регион", "Сумма"]]   )    z = z.groupby(["Регион"]).sum()       all = pd.DataFrame(z)   !    all.reset_index(inplace=True)   A    zachet_all = all.sort_values(["Сумма"], ascending=False)   3    zachet_all.reset_index(drop=True, inplace=True)       zachet_all.index += 1   D    ic("Количество категорий: ", len(xlsx_files))       ic(zachet_all)   K    zachet_all.to_excel(writer, sheet_name="Командный зачет")           
def pol():           dataroz = (   A        rr.groupby(["Регион", "Дата рождения"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   n    dataroz["Дата рождения"] = pd.to_datetime(dataroz["Дата рождения"], dayfirst=True)   L    dataroz["Data"] = dataroz["Дата рождения"].dt.strftime("%Y")       dataroz = (   1        dataroz.groupby(["Регион", "Data"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   `    dataroz = dataroz.pivot(index="Регион", columns="Data", values="Количество")   k    pol = rr.groupby(["Регион", "пол"]).size().to_frame(name="Количество").reset_index()       raz = (   B        rr.groupby(["Регион", "Разряд, звание"])           .size()   .        .to_frame(name="Количество")           .reset_index()       )   Z    pol = pol.pivot(index="Регион", columns="пол", values="Количество")   n    raz = raz.pivot(index="Регион", columns="Разряд, звание", values="Количество")   C    pol.to_excel(writer, sheet_name="ПОЛ по регионам")   K    raz.to_excel(writer, sheet_name="Разряды по регионам")   X    dataroz.to_excel(writer, sheet_name="Год рождения по регионам")           1# with pd.ExcelWriter("итог.xlsx") as writer:   #     df.to_excel(writer)   =writer = pd.ExcelWriter("итог.xlsx", engine="xlsxwriter")   "starttime = timeit.default_timer()           def main():           # get a list of file names       xlsx_files = []       xlsx_files = [   	        y   .        for x in os.walk("Протоколы")   8        for y in glob.glob(os.path.join(x[0], "*.xlsx"))       ]   V    ic("________________Количество категорий____", len(xlsx_files))           # set up your pool   L    with Pool(processes=8) as pool:  # or whatever your hardware can support       9        # have your pool map the file names to dataframes   2        df_list = pool.map(read_excel, xlsx_files)       =        # reduce the list of dataframes to a single dataframe   2        df = pd.concat(df_list, ignore_index=True)   /        filter1 = df["пол"].isin(["Муж"])   /        filter2 = df["пол"].isin(["Жен"])           man = df[filter1]           women = df[filter2]           work(df)           for i in EVENTS_AGE:   O            frame = man[man["Полных лет"].isin(range(i[0], i[1] + 1))]   =            # frame = man[man["Полных лет"].isin(i)]               list_results(frame)           for i in EVENTS_AGE:   S            frame = women[women["Полных лет"].isin(range(i[0], i[1] + 1))]   A            # frame = women[women["Полных лет"].isin(i)]               list_results(frame)           work(df)           regions(df)           gender()           sport()           medalscommonlist(df)           zachet(xlsx_files)           # pol()           if __name__ == "__main__":   
    main()       writer.save()   b    ic("Время выполнения программы :", timeit.default_timer() - starttime)5�_�                   �   (    ����                                                                                                                                                                                                                                                                                                                                                             c���     �  �  �  �      /        filter1 = df["пол"].isin(["Муж"])5�_�                   �   (    ����                                                                                                                                                                                                                                                                                                                                                             c���    �  �  �  �      -        filter1 = df["пол"].isin(["Мж"])5�_�                   �   (    ����                                                                                                                                                                                                                                                                                                                                                             c���    �  �  �  �      /        filter2 = df["пол"].isin(["Жен"])5�_�                    �   (    ����                                                                                                                                                                                                                                                                                                                                                             c���    �  �  �  �      -        filter2 = df["пол"].isin(["Жн"])5��