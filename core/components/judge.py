# -*- coding: utf-8 -*-
from core.components import Base
from core.manages.global_manager import GlobalManager


class Judge(Base):

    def enable_click_loop(self):
        element = self.driver.find_element_by_xpath(self.params['xpath'])
        if element.is_enabled():
            return GlobalManager().loop_turn_on()

        return GlobalManager().loop_turn_off()

    def display_click_loop(self):
        element = self.driver.find_element_by_xpath(self.params['xpath'])
        if element.is_displayed():
            return GlobalManager().loop_turn_on()

        return GlobalManager().loop_turn_off()

    def has_class_terminate(self):
        element = self.driver.find_element_by_xpath(self.params['xpath'])
        if self.params['class'] in element.get_attribute('class'):
            return GlobalManager().loop_turn_off()
        return GlobalManager().loop_turn_on()

    def not_has_element_terminate(self):
        element = self.driver.find_elements_by_xpath(self.params['xpath'])
        if not element:
            return GlobalManager().loop_turn_off()

        return GlobalManager().loop_turn_on()

    def default(self):
        pass
