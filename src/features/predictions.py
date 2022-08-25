import __future__

def check_prediction(self):
    '''
    Transformed all radio buttons options into a dictionary with its names, booleans and functions
    with this we can avoid lots of if statements into the code
    '''
    rb_options = {
        self.rb_data_segregation.objectName() : {
            'bool' : self.rb_data_segregation.isChecked(),
            'function': data_segregation
        },
        self.rb_linear_regression.objectName() : {
            'bool' : self.rb_linear_regression.isChecked(),
            'function': linear_regression
        },
        self.rb_mean.objectName() : {
            'bool' : self.rb_mean.isChecked(),
            'function': mean
        },
        self.rb_standard_deviation.objectName() : {
            'bool' : self.rb_standard_deviation.isChecked(),
            'function': standard_deviation
        },
        self.rb_time_series.objectName() : {
            'bool' : self.rb_time_series.isChecked(),
            'function': time_series
        },
        self.rb_weighted_average.objectName() : {
            'bool' : self.rb_weighted_average.isChecked(),
            'function': weighted_average
        }
    }

    for value in rb_options.values():
        if value['bool']:
            value['function'](self)

def data_segregation(self):
    print('data_segregation')

def linear_regression(self):
    print('linear_regression')

def mean(self, show_on_screen=True):
    mean_result = self.table['Billing'].mean()
    if show_on_screen:
        self.line_result.setText(str(f'Mean => {mean_result:.2f}'))
    else:
        return mean_result

def standard_deviation(self):
    std_dev = self.table['Billing'].std()
    percentage_var = (std_dev / mean(self, show_on_screen=False)) * 100
    message = f'Standard deviation => {std_dev:.2f} | Variation percentage => {percentage_var}%'
    self.line_result.setText(message)

def time_series(self):
    print('time series')

def weighted_average(self):
    print('weighted_average')