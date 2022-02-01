import pandas as pd



if __name__ == '__main__':
    rawtable = pd.read_csv('action_button_renaming_test.csv')

    rawtable = rawtable.query('first_visit_after_test_start != False')  #  Відсіюємо користувачів,
                                                                         #  що не взяли участі в тестуванні

    rawtable = rawtable[rawtable.platform == 'Web']  #  Обираємо користувачів лише з веб-версії

    control_group = rawtable[rawtable['group'] == 'control']  #  Фрейм з контрольною групою

    test_group = rawtable[rawtable['group'] == 'test']  #  Фрейм з тестовою групою

    AWPU_test = 0
    AWPU_control = 0
    count = 0

    for date_check in test_group.date.unique():
        test_group_day = test_group[test_group['date'] == f'{date_check}']
        AWPU_test_day = (test_group_day['contact_views_number'].sum() / test_group_day['user_id'].count()) * 100
        AWPU_test += AWPU_test_day
        count += 1


    AWPU_test = AWPU_test / count   #  Середнє значення конверсії переглядів тестової групи за день (у відсотках)

    count = 0

    for date_check in control_group.date.unique():
        control_group_day = control_group[control_group['date'] == f'{date_check}']
        AWPU_control_day = (control_group_day['contact_views_number'].sum() / control_group_day['user_id'].count()) \
                                                                                                                * 100
        AWPU_control += AWPU_control_day
        count += 1


    AWPU_control = AWPU_control / count   #  Середнє значення конверсії переглядів контрольної
                                                                                         # групи за день (у відсотках)

    AWPU_change = AWPU_test - AWPU_control # Різниця середніх значень конверсії переглядів контрольної
                                                                                         # групи за день (у відсотках)

    if AWPU_change > 0:
        message_part = 'більше'
    else:
        message_part = 'менше'
        AWPU_change = -AWPU_change

    print(f'Конверсія переглядів у веб-версії тестової групи {message_part} на {AWPU_change} відсоткових пункти'
          f' ніж у контрольної групи')








    #print(control_group)
    #print(test_group)
    #print(rawtable.platform.unique())
    #print(rawtable.device_type.unique())
    #print(rawtable.first_visit_after_test_start.unique())
    #print(rawtable.contact_views_number.unique())
    #print(rawtable.date.unique())
    #print(rawtable.columns.tolist())
