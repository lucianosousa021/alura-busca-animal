from django.test import LiveServerTestCase
from selenium import webdriver
from animais.models import Animal


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path='/home/luciano/Documentos/tdd_busca_animal/geckodriver')
        self.animal = Animal.objects.create(
            nome_animal = 'leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    def tearDown(self):
        self.browser.quit()

    def test_buscnado_um_animal(self):
        """ TESTE SE UM USUARIO ENCONTRA UM ANIMAL NA PESQUISA """

        #ele encontra o busca animal e decide usar o site
        home_page = self.browser.get(self.live_server_url + '/')
        #ele ve no site o menu busca animal
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Buscar Animal', brand_element.text)

        #ele ve um campo para pesquisar animais pelo NotImplemented
        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...')

        #ele pesquisa por leão e clica no botão pesquisar anim
        buscar_animal_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()

        #o site exibe 4 caracteristicas do animal pesquisado
        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)