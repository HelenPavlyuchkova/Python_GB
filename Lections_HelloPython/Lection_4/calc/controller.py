# модуль, который связывает model и view 

# import model_sum as model
import model_mult as model
# import model_sub as model
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, 'result')
    
