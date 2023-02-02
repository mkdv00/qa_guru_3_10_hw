from allure_commons.types import Severity

from demo_qa.model.pages.practise_form import Form
from demo_qa.data.user_data import test_user
import allure


def test_submitting_form():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'kudaev.m')
    allure.dynamic.feature('Проверка отправки формы')

    with allure.step('Открываем demoqa'):
        form = Form()

    with allure.step('Заполняем данные формы'):
        form.submit_form(test_user)

    with allure.step('Проверяем, что данные формы есть в результирующей таблице'):
        form.validate_form(test_user)
