from commands.remote_commands import write, open, new_file, save_file, undo
from keypress.navigate import up, down, left, right, enter, backspace, tab, activate_mark, copy, paste, select_explorer

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
        'mark' : 'remote.activate_mark()',
        'copy' : 'remote.copy()',
        'paste' : 'remote.paste()',
        'Explorer' : 'remote.select_explorer()'
    }.get(x, 'none')