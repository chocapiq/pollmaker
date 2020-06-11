from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random

class PollMaker():
    def __init__(self, driver=1):
        self.driver = driver

    def getWebdriverInstance(self):
        baseUrl = "https://docs.google.com/forms/d/e/1FAIpQLSf94g2-TSUgduHEoTI8Ecjrd2074M6rB6vEEGwmQwuu7jN3zw/viewform"
        if self.driver == 1:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(baseUrl)
            self.driver.implicitly_wait(3)
            try:
                self.Q01()
                self.Q02()
                self.Q03()
                self.Q04()
                self.Q06()
                self.Q07()
                self.Q09()
                self.Q12()
                self.Q15()
                self.Q17()
                self.Q19()
                self.Q20()
                self.Q21()
                self.Q22()
                self.Q23()
                self.Q24()
                self.Q25()
                self.quit()
            except:
                self.quit()

    def Q01(self):
        a = random.randint(1,8)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element6 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[6]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a == 1:
            element1.click()
        elif a == 2:
            element2.click()
        elif a == 3:
            element3.click()
        elif a == 4:
            element4.click()
        elif a in (5,6):
            element5.click()
        else:
            element6.click()

    def Q02(self):
        a = random.randint(1, 19)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[5]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element6 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[6]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element7 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[7]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element8 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[8]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element9 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[9]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element1.location_once_scrolled_into_view
        if a in range(1,15):
            element1.click()
        if a in range(6,19):
            element2.click()
        if a in (1, 2, 4, 8, 16, 19):
            element3.click()
        if a in (4, 15, 17, 19):
            element4.click()
        if a in (18, 19):
            element5.click()
        if a == 3:
            element6.click()
        if a in (1,3,5,6,10,14,15,17,18):
            element7.click()
        if a in (5, 7, 9):
            element8.click()
        if a in (2,11,12,13,16):
            element9.click()

    def Q03(self):
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)
        d = random.randint(1, 5)
        e = random.randint(1, 5)
        f = random.randint(1, 5)

        element11 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element12 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element13 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element14 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element15 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element21 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element22 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element23 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element24 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element25 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element31 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element32 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element33 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element34 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element35 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element41 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element42 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element43 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element44 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element45 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element51 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element52 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element53 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element54 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element55 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element61 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element62 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element63 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element64 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element65 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element11.location_once_scrolled_into_view
        if a == 1:
            element11.click()
        if a == 2:
            element12.click()
        if a == 3:
            element13.click()
        if a == 4:
            element14.click()
        if a == 5:
            element15.click()
        if b == 1:
            element21.click()
        if b == 2:
            element22.click()
        if b == 3:
            element23.click()
        if b == 4:
            element24.click()
        if b == 5:
            element25.click()
        if c == 1:
            element31.click()
        if c == 2:
            element32.click()
        if c == 3:
            element33.click()
        if c == 4:
            element34.click()
        if c == 5:
            element35.click()
        if d == 1:
            element41.click()
        if d == 2:
            element42.click()
        if d == 3:
            element43.click()
        if d == 4:
            element44.click()
        if d == 5:
            element45.click()
        if e == 1:
            element51.click()
        if e == 2:
            element52.click()
        if e == 3:
            element53.click()
        if e == 4:
            element54.click()
        if e == 5:
            element55.click()
        if f == 1:
            element61.click()
        if f == 2:
            element62.click()
        if f == 3:
            element63.click()
        if f == 4:
            element64.click()
        if f == 5:
            element65.click()

    def Q05(self):
        a = random.randint(1, 12)
        element11 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[2]/label[1]/div[1]/div[1]/div[2]")
        element12 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[2]/label[2]/div[1]/div[1]/div[2]")
        element21 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[4]/label[1]/div[1]/div[1]/div[2]")
        element22 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[4]/label[2]/div[1]/div[1]/div[2]")
        element31 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[6]/label[1]/div[1]/div[1]/div[2]")
        element32 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[6]/label[2]/div[1]/div[1]/div[2]")
        element41 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[8]/label[1]/div[1]/div[1]/div[2]")
        element42 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[8]/label[2]/div[1]/div[1]/div[2]")
        element51 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[10]/label[1]/div[1]/div[1]/div[2]")
        element52 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[10]/label[2]/div[1]/div[1]/div[2]")
        element61 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[12]/label[1]/div[1]/div[1]/div[2]")
        element62 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[12]/label[2]/div[1]/div[1]/div[2]")
        element71 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[14]/label[1]/div[1]/div[1]/div[2]")
        element72 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[14]/label[2]/div[1]/div[1]/div[2]")
        element81 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[16]/label[1]/div[1]/div[1]/div[2]")
        element82 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div/div/div/div/div/div/div[16]/label[2]/div[1]/div[1]/div[2]")
        element11.location_once_scrolled_into_view
        if a in range(1,5):
            element11.click()
            element21.click()
            element31.click()
            element41.click()
            element51.click()
            element61.click()
            element71.click()
            element81.click()
        if a in range (5,10):
            element12.click()
            element22.click()
            element32.click()
            element42.click()
            element52.click()
            element62.click()
            element72.click()
            element82.click()
        if a >= 10 :
            b = random.randint(1,2)
            if b == 1:
                element11.click()
            else:
                element12.click()
            c = random.randint(1, 2)
            if c == 1:
                element21.click()
            else:
                element22.click()
            d = random.randint(1, 2)
            if d == 1:
                element31.click()
            else:
                element32.click()
            e = random.randint(1, 2)
            if e == 1:
                element41.click()
            else:
                element42.click()
            f = random.randint(1, 2)
            if f == 1:
                element51.click()
            else:
                element52.click()
            g = random.randint(1, 2)
            if g == 1:
                element61.click()
            else:
                element62.click()
            h = random.randint(1, 2)
            if h == 1:
                element71.click()
            else:
                element72.click()
            i = random.randint(1, 2)
            if i == 1:
                element81.click()
            else:
                element82.click()

    def Q04(self):
        a = random.randint(1, 6)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element6 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[6]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a == 1:
            element1.click()
            self.Q05()
        if a == 2:
            element2.click()
            self.Q05()
        if a == 3:
            element3.click()
            self.Q05()
        if a == 4:
            element4.click()
            self.Q05()
        if a == 5:
            element5.click()
            self.Q05()
        if a == 6:
            element6.click()


    def Q06(self):
        a = random.randint(1, 6)
        print("Q06 " + str(a))
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[6]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[6]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[6]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[6]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[6]/div[1]/div[2]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a == 1:
            element1.click()
        if a == 2:
            element2.click()
        if a == 3:
            element3.click()
        if a == 4:
            element4.click()
        if a in (5,6):
            element5.click()

    def Q08(self):
        a = random.randint(1, 15)
        b = random.randint(1, 15)
        c = random.randint(1, 15)
        d = random.randint(1, 15)
        e = random.randint(1, 15)
        print("Q08 " + str(a))
        print("Q08 " + str(b))
        print("Q08 " + str(c))
        print("Q08 " + str(d))
        print("Q08 " + str(e))

        element11 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element12 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element13 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element14 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element15 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element21 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element22 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element23 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element24 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element25 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element31 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element32 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element33 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element34 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element35 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element41 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element42 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element43 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element44 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element45 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element51 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element52 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element53 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element54 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element55 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[8]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element11.location_once_scrolled_into_view
        if a == 1:
            element11.click()
        if a in (2,3):
            element12.click()
        if a in range (4, 9):
            element13.click()
        if a in range (9, 14):
            element14.click()
        if a in (14,15):
            element15.click()
        if b == 1:
            element21.click()
        if b == 2:
            element22.click()
        if b in range(3, 12):
            element23.click()
        if b in range(12, 15):
            element24.click()
        if b == 15:
            element25.click()
        if c == 1:
            element31.click()
        if c in (2,3):
            element32.click()
        if c in range(4,13):
            element33.click()
        if c in (13, 14):
            element34.click()
        if c == 15:
            element35.click()
        if d == 1:
            element41.click()
        if d in range(2, 6):
            element42.click()
        if d in range(6, 13):
            element43.click()
        if d in (13, 14):
            element44.click()
        if d == 15:
            element45.click()
        if e == 1:
            element51.click()
        if e in (2, 3):
            element52.click()
        if e in range(4, 8):
            element53.click()
        if e in range(8, 12):
            element54.click()
        if e in range(12, 16):
            element55.click()

    def Q07(self):
        a = random.randint(1, 5)
        print("Q07 " + str(a))
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[7]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[7]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a in (1, 3):
            element1.click()
            self.Q08()
        else:
            element2.click()

    def Q11(self):
        a = random.randint(1, 11)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[11]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[11]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[11]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[11]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[11]/div[1]/div[2]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        if a in (1, 2):
            element1.click()
        if a in (3, 4, 5):
            element2.click()
        if a == 6:
            element3.click()
        if a == 7:
            element4.click()
        if a in range(8,12):
            element5.click()

    def Q10(self):
        a = random.randint(1, 10)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[10]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[10]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[10]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[10]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[10]/div[1]/div[2]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        if a in (1,2):
            element1.click()
        if a in (3,4,5):
            element2.click()
        if a == 6:
            element3.click()
        if a == 7:
            element4.click()
        if a in range(8,11):
            element5.click()
        self.Q11()


    def Q09(self):
        a = random.randint(1, 2)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[9]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[9]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a == 1:
            element1.click()
            self.Q10()
        if a == 2:
            element2.click()

    def Q14(self):
        a = random.randint(1, 12)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[14]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[14]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[14]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[14]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[14]/div[1]/div[2]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        if a in (1,2):
            element1.click()
        if a in range(3,9):
            element2.click()
        if a == 9:
            element3.click()
        if a == 10:
            element4.click()
        if a in (11,12):
            element5.click()

    def Q13(self):
        a = random.randint(1, 19)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[1]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[3]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[4]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[5]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element6 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[6]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element7 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[7]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element8 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[8]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element9 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[9]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element10 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[13]/div[1]/div[2]/div[10]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element1.location_once_scrolled_into_view
        if a in range(1, 15):
            element1.click()
        if a in range(6, 19):
            element2.click()
        if a in (1, 2, 4, 8, 16, 19):
            element3.click()
        if a in (4, 19):
            element4.click()
        if a == 19:
            element5.click()
        if a == 3:
            element6.click()
        if a in (1, 3, 5, 6, 10, 14, 15, 17, 18):
            element7.click()
        if a in (5, 7, 9):
            element8.click()
        if a in (2, 11, 12, 13, 16):
            element9.click()
        if a in (15, 17, 18):
            element10.click()
        self.Q14()

    def Q12(self):
        a = random.randint(1, 20)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[12]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[12]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a in range (1,14):
            element1.click()
            self.Q13()
        else:
            element2.click()

    def Q16(self):
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        c = random.randint(1, 30)
        d = random.randint(1, 30)

        element11 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element12 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element13 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element14 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element15 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element16 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element21 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element22 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element23 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element24 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element25 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element26 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element31 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element32 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element33 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element34 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element35 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element36 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element41 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element42 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element43 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element44 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element45 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element46 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element11.location_once_scrolled_into_view
        scroll1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[16]/div[1]/div[2]/div[1]/div[1]")
        if a in range(1, 7):
            element11.click()
        if a == 7:
            element12.click()
        if a == 8:
            element13.click()
        if a in range(9, 19):
            element14.click()
        if a in range(19, 28):
            element15.click()
        if a in range(28, 31):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element16)
            element16.click()
            ActionChains(self.driver).key_down(Keys.ARROW_LEFT, scroll1).perform()
            ActionChains(self.driver).key_down(Keys.ARROW_LEFT, scroll1).perform()
            ActionChains(self.driver).key_up(Keys.ARROW_LEFT).perform()
        if b in range(1,12):
            element21.click()
        if b == 12:
            element22.click()
        if b == 13:
            element23.click()
        if b in range(14, 22):
            element24.click()
        if b in range(22, 28):
            element25.click()
        if b in range(28, 31):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element16)
            element26.click()
            ActionChains(self.driver).key_down(Keys.ARROW_LEFT, scroll1).perform()
            ActionChains(self.driver).key_down(Keys.ARROW_LEFT, scroll1).perform()
            ActionChains(self.driver).key_up(Keys.ARROW_LEFT).perform()
        if c in range(1,13):
            element31.click()
        if c == 13:
            element32.click()
        if c in range(14,17):
            element33.click()
        if c in range(17,24):
            element34.click()
        if c in range(24,28):
            element35.click()
        if c in range(28,31):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element16)
            element36.click()
            ActionChains(self.driver).key_down(Keys.ARROW_LEFT, scroll1).perform()
            ActionChains(self.driver).key_down(Keys.ARROW_LEFT, scroll1).perform()
            ActionChains(self.driver).key_up(Keys.ARROW_LEFT).perform()
        if d in range(1,20):
            element41.click()
        if d == 20:
            element42.click()
        if d == 21:
            element43.click()
        if d in range(22, 29):
            element44.click()
        if d == 29:
            element45.click()
        if d == 30:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element16)
            element46.click()
            ActionChains(self.driver).key_down(Keys.ARROW_LEFT, scroll1).perform()
            ActionChains(self.driver).key_down(Keys.ARROW_LEFT, scroll1).perform()
            ActionChains(self.driver).key_up(Keys.ARROW_LEFT).perform()

    def Q15(self):
        a = random.randint(1, 20)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[15]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[15]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a in range (1,7):
            element1.click()
            self.Q16()
        else:
            element2.click()

    def Q18(self):
        a = random.randint(1, 13)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[18]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[18]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[18]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[18]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[18]/div[1]/div[2]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a in (1,2):
            element1.click()
        if a in range(3,7):
            element2.click()
        if a in (7,8,9):
            element3.click()
        if a == 10:
            element4.click()
        if a in range(11,14):
            element5.click()

    def Q17(self):
        a = random.randint(1, 5)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[17]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[17]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a in range(1,8):
            element1.click()
            self.Q18()
        else:
            element2.click()

    def Q19(self):
        a = random.randint(1, 12)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[19]/div[1]/div[2]/div[1]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[19]/div[1]/div[2]/div[2]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[19]/div[1]/div[2]/div[3]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[19]/div[1]/div[2]/div[4]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[19]/div[1]/div[2]/div[5]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element6 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[19]/div[1]/div[2]/div[6]/div[1]/label[1]/div[1]/div[1]/div[2]")
        element1.location_once_scrolled_into_view
        if a in range(1, 9):
            element1.click()
        if a in (5, 6, 7, 9, 10):
            element2.click()
        if a in (2, 3, 4, 5, 10, 12):
            element3.click()
        if a in (7, 8, 9, 11, 12):
            element4.click()
        if a in (1, 4, 9, 11):
            element5.click()
        if a in (1,8):
            element6.click()

    def Q20(self):
        a = random.randint(1, 12)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[20]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[20]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[20]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[20]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element5 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[20]/div[1]/div[2]/div[1]/span[1]/div[1]/div[5]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a in (1,2):
            element1.click()
        if a in range (3,7):
            element2.click()
        if a in (7,8):
            element3.click()
        if a == 9:
            element4.click()
        if a in range(10,13):
            element5.click()

    def Q21(self):
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        c = random.randint(1, 30)
        d = random.randint(1, 30)
        e = random.randint(1, 30)
        f = random.randint(1, 30)

        element11 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element12 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element13 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element14 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element15 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element16 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element21 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element22 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element23 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element24 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element25 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element26 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element31 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element32 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element33 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element34 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element35 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element36 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element41 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element42 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element43 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element44 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element45 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element46 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element51 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element52 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element53 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element54 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element55 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element56 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[10]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element61 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[2]/div[1]/div[1]/div[3]/div[1]")
        element62 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[3]/div[1]/div[1]/div[3]/div[1]")
        element63 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[4]/div[1]/div[1]/div[3]/div[1]")
        element64 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[5]/div[1]/div[1]/div[3]/div[1]")
        element65 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[6]/div[1]/div[1]/div[3]/div[1]")
        element66 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[21]/div[1]/div[2]/div[1]/div[1]/div[1]/div[12]/span[1]/div[7]/div[1]/div[1]/div[3]/div[1]")
        element11.location_once_scrolled_into_view
        if a in range(1, 2):
            element11.click()
        if a in range(2, 3):
            element12.click()
        if a in range(3, 5):
            element13.click()
        if a in range(5, 7):
            element14.click()
        if a in range(7, 15):
            element15.click()
        if a in range(15, 31):
            element16.click()
        if b in range(1,2):
            element21.click()
        if b in range(2,4):
            element22.click()
        if b in range(4,8):
            element23.click()
        if b in range(8, 13):
            element24.click()
        if b in range(13, 24):
            element25.click()
        if b in range(24, 31):
            element26.click()
        if c in range(1,12):
            element31.click()
        if c in range(12,15):
            element32.click()
        if c in range(15,19):
            element33.click()
        if c in range(19,26):
            element34.click()
        if c in range(26,30):
            element35.click()
        if c in range(30,31):
            element36.click()
        if d in range(1,9):
            element41.click()
        if d in range(9,21):
            element42.click()
        if d in range(21,25):
            element43.click()
        if d in range(25,28):
            element44.click()
        if d in range(28,30):
            element45.click()
        if d == 30:
            element46.click()
        if e in range(1,10):
            element51.click()
        if e in range(10,22):
            element52.click()
        if e in range(22,26):
            element53.click()
        if e in range(26,29):
            element54.click()
        if e in range(29,30):
            element55.click()
        if e in range(30,31):
            element56.click()
        if f in range(1,8):
            element61.click()
        if f in range(8,17):
            element62.click()
        if f in range(17,22):
            element63.click()
        if f in range(22,25):
            element64.click()
        if f in range(25,30):
            element65.click()
        if f in range(30,31):
            element66.click()
        go_next = self.driver.find_element_by_xpath("//span[contains(text(),'Dalej')]")
        go_next.click()

    def Q22(self):
        a = random.randint(1, 50)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a in range (1,23):
            element1.click()
        else:
            element2.click()

    def Q23(self):
        global z
        z = random.randint(1, 30)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[3]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if z in range(1, 7):
            element1.click()
        if z in range(7, 10):
            element2.click()
        if z in range(11,23):
            element3.click()
        if z in range(23,31):
            element4.click()


    def Q24(self):
        a = random.randint(1, 11)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[4]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a in (1,2):
            element1.click()
        if a in (2,3):
            element2.click()
        if a in range(4,7):
            element3.click()
        if a in range(7,12):
            element4.click()

    def Q25(self):
        x = random.randint(1,2)
        if z in range(1, 7):
            if x == 1:
                a = 1
            else:
                a = random.randint(2,30)
        else:
            a = random.randint(2, 30)
        element1 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[5]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element2 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[5]/div[1]/div[2]/div[1]/span[1]/div[1]/div[2]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element3 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[5]/div[1]/div[2]/div[1]/span[1]/div[1]/div[3]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element4 = self.driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[5]/div[1]/div[2]/div[1]/span[1]/div[1]/div[4]/label[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
        element1.location_once_scrolled_into_view
        if a == 1:
            element1.click()
        if a in range(2,19):
            element2.click()
        if a in range(19,29):
            element3.click()
        if a in range(29,31):
            element4.click()
        send0 = self.driver.find_element_by_xpath("//span[contains(text(),'Prze')]")
        send0.click()
        print('done')

    def quit(self):
        print('done')
        self.driver.quit()

poll = PollMaker()
poll.getWebdriverInstance()

