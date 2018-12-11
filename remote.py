from commands.remote_commands import write, open, new_file, save_file, undo
from keypress.navigate import up, down, left, right, enter, backspace, tab

def keywords_overall(x):
    return {
        'edit': 'remote.write(words_list["transcription"])',
        'open': 'remote.open(words_list["transcription"])',
        'new' : 'remote.new_file()',
        'save' : 'remote.save_file(words_list["transcription"])',
        'undo' : 'remote.undo()',
        'up' : 'remote.up()',
        'down' : 'remote.down()',
        'left' : 'remote.left()',
        'right' : 'remote.right()',
        'enter' : 'remote.enter()',
        'backspace' : 'remote.backspace()',
        'tab' : 'remote.tab()',
    }.get(x, 'none')