Vim�UnDo� -c����?������e��ByȊ_+���rl                                     d��    _�                             ����                                                                                                                                                                                                                                                                                                                                       !           V        d���    �                def test_sidebar_callback():       def run_callback_close():           context_value.set(   S            AttributeDict(**{"triggered_inputs": [{"sidebar-toggle": "n_clicks"}]})   	        )   &        return toggle_classname(1, "")           def run_callback_open():           context_value.set(   S            AttributeDict(**{"triggered_inputs": [{"sidebar-toggle": "n_clicks"}]})   	        )   /        return toggle_classname(0, "collapsed")           ctx = copy_context()   '    output = ctx.run(run_callback_open)       assert output == ""   (    output = ctx.run(run_callback_close)        assert output == "collapsed"5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d���    �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d���    �                ;from src.callbacks.sidebar_callback import toggle_classname5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d��    �                 $from contextvars import copy_context   0from dash._callback_context import context_value   %from dash._utils import AttributeDict5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d��    �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d��    �                 9# Import the names of callback functions you want to test5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        d��    �                  �              �                  ;from src.utils.dataframe import get_all_sportsmen_dataframe           'def test_get_all_sportsmen_dataframe():   *    output = get_all_sportsmen_dataframe()       result = output.columns[11]   0    assert result == "Вид программы"    5��