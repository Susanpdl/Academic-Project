import kivy
import json
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class DataBase(GridLayout):    
    """creates an interface for the application
    """
    def __init__(self, **kwargs):                       #Initialized interface layout
        super().__init__(**kwargs)

        self.cols = 1

        self.label1 = Label(text="Student's Email", font_size=30)
        self.input1 = TextInput(multiline=False)
        self.label2 = Label(text="Age of the Std.", font_size=30)
        self.input2 = TextInput(multiline=False)
    
        self.label3 = Label(text="", font_size = 30)        #empty label to display messages to the user

        self.add_widget(self.label1)
        self.add_widget(self.input1)
        self.add_widget(self.label2)
        self.add_widget(self.input2)

        '''Creating buttons for to perform essential function i.e save, load, update, and delete the student info 
        '''
        self.save_button = Button(text='Save the Student info', on_press=self.save_data,font_size=25,
                                  background_normal='img.jpg')
        self.load_button = Button(text="load the Email address", on_press=self.load_data,font_size=25,
                                  background_normal='img.jpg')
        self.update_button = Button(text='Update the email', on_press=self.update_data,font_size=25,
                                  background_normal='img.jpg')
        self.delete_button = Button(text="Delete the Email", on_press=self.delete_data, font_size=25,
                                  background_normal='img.jpg')

        ''' Adding buttons and label to the layout'''
        self.add_widget(self.save_button)
        self.add_widget(self.load_button)
        self.add_widget(self.update_button)
        self.add_widget(self.delete_button)
        self.add_widget(self.label3)

    def save_data(self, instance):
        '''Saves the data entered
        '''
        data = {'Email Address of the Student': self.input1.text, 'Age': self.input2.text}

        with open('std_data.json', 'w') as f:       #opening the file in write mode
            json.dump(data, f)

        self.label3.text = 'Data saved successfully'

    def load_data(self, instance):
        '''load the data by accessing the json file.'''
        try:
            with open('std_data.json', 'r') as f:               #opening the file in read mode
                data = json.load(f)

            self.input1.text = data['Email Address of the Student']
            self.input2.text = data['Age']

            self.label3.text = 'Data loaded successfully'

        except FileNotFoundError as e:
            self.label3.text = 'No Data Found'


    def update_data(self, instance):
        '''Updates the student email address and age
        '''
        data = {'Email Address of the new Student': self.input1.text, ' New age': self.input2.text}

        try:
            with open('std_data.json', 'r') as f:
                old_data = json.load(f)

            old_data.update(data)

            with open('std_data.json', 'w') as f:
                json.dump(old_data, f)

            self.label3.text = 'Email Updated Successfully'

        except FileNotFoundError:
            self.label3.text = 'Not Found'

    def delete_data(self, instance):
        '''Deletes json file
        '''
        try:
            import os
            os.remove('std_data.json')

            self.label3.text = 'Deleted successfully'

        except FileNotFoundError:
            self.label3.text = 'Not Found'


class StudentData(App):
    def build(self):                                    #inherents all the functionality from DataBase class
        return DataBase()

if __name__ == '__main__':
    StudentData().run()