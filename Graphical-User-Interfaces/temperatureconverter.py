



"""
Author: Dylon Adams
Instructor: Ralph Giles
File: temperatureconverter.py
This lets the user convert between Fahrenheit and Celsius.
"""




from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):


    """This right here is the window for the temperature converter."""


    def __init__(self):


        """Builds the window and adds everything to it."""


        EasyFrame.__init__(self, title = "Temperature Converter")



            #Labels go here in the top row



        self.addLabel(text = "Fahrenheit", row = 0, column = 0)


        self.addLabel(text = "Celsius", row = 0, column = 1)



              #Entry fields go under the labels, starting at 32.0F and 0.0C



        self.fahrField = self.addFloatField(value = 32.0,

                                            row = 1, column = 0)

        self.celsField = self.addFloatField(value = 0.0,

                                            row = 1, column = 1)

                 #Buttons go in the bottom row, each one will run its own method



        self.addButton(text = ">>>>", row = 2, column = 0,

                       command = self.toCelsius)

        self.addButton(text = "<<<<", row = 2, column = 1,

                       command = self.toFahrenheit)



    def toCelsius(self):


        """Takes the Fahrenheit number and shows it in Celsius."""


        fahr = self.fahrField.getNumber()
        celsius = (fahr - 32) * 5 / 9
        self.celsField.setNumber(celsius)

    def toFahrenheit(self):



        """Takes the Celsius number and shows it in Fahrenheit."""


        celsius = self.celsField.getNumber()
        fahr = celsius * 9 / 5 + 32
        self.fahrField.setNumber(fahr)



def main():


    """Creates the window and keeps it running."""


    TemperatureConverter().mainloop()



if __name__ == "__main__":





    main()
