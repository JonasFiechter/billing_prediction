'''
    self.rb_data_segregation.setDisabled(True)
    self.rb_linear_regression.setDisabled(True)
    self.rb_mean.setDisabled(True)
    self.rb_standard_deviation.setDisabled(True)
    self.rb_time_series.setDisabled(True)
    self.rb_weighted_average.setDisabled(True)
'''

import __future__

def check_prediction(self):
    '''
    Transformed all radio buttons options into a dictionary with its names, booleans and functions
    with this we can avoid lots of if statements into the code
    '''
    rb_options = {
        self.rb_data_segregation.objectName() : {
            'bool' : self.rb_data_segregation.isChecked(),
            'function': mean
        },
        self.rb_linear_regression.objectName() : {
            'bool' : self.rb_linear_regression.isChecked(),
            'function': mean
        },
        self.rb_mean.objectName() : {
            'bool' : self.rb_mean.isChecked(),
            'function': mean
        },
        self.rb_standard_deviation.objectName() : {
            'bool' : self.rb_standard_deviation.isChecked(),
            'function': mean
        },
        self.rb_time_series.objectName() : {
            'bool' : self.rb_time_series.isChecked(),
            'function': mean
        },
        self.rb_weighted_average.objectName() : {
            'bool' : self.rb_weighted_average.isChecked(),
            'function': mean
        }
    }

    for value in rb_options.values():
        if value['bool']:
            value['function'](self)

def mean(self):
    print(self.table['Billing'].mean())