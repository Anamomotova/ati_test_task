from time import sleep

def test_task__for_autotrans_info(drv):
    drv.implicitly_wait(10)
    drv.maximize_window()
    drv.get('https://ati.su')
    assert drv.title == "АТИ – биржа грузоперевозок. Грузы, транспорт, тендеры."

    drv.find_element_by_css_selector("[aria-controls = 'react-autowhatever-from']").send_keys('Санкт-Петербург')
    drv.find_element_by_xpath("//div[contains(@class, 'suggestion') and contains(., 'Санкт-Петербург, РФ')]").click()

    drv.find_element_by_css_selector("[aria-controls = 'react-autowhatever-to']").send_keys('Москва')
    drv.find_element_by_xpath("//div[contains(@class, 'suggestion') and contains(., 'Москва, РФ')]").click()
    drv.find_element_by_class_name('_2c8wr-2-0-239').click()
    sleep(2)
    drv.switch_to.window('https://trace.ati.su/?Ferries=1&Cities=1_1-2_3611')

    distance = drv.find_element_by_css_selector('.text___3D_of.value___3PnpS').text
    assert distance == "724"