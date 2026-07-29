from textwrap import fill

WIDTH = 80


def header(title: str) -> None:
    '''Major section.'''
    print()
    print('╔' + '═' * WIDTH + '╗')
    print(f'║{title.upper():^{WIDTH}}║')
    print('╚' + '═' * WIDTH + '╝')
    print()


def subheader(title: str) -> None:
    '''Minor section.'''
    print()
    print(f'┏━━ {title}')
    print('┗' + '━' * (WIDTH - 1))
    print()


def section(title: str) -> None:
    '''Execution step.'''
    print(f'\n[▶] {title}')


def divider() -> None:
    '''Horizontal divider.'''
    print('─' * WIDTH)
    print()


def blank() -> None:
    '''Blank line.'''
    print()


def info(message: str) -> None:
    print(f'[ℹ] {message}')


def success(message: str) -> None:
    print(f'[✓] {message}')

def warning(message: str) -> None:
    print(f'[⚠] {message}')

def error(message: str) -> None:
    print(f'[✗] {message}')

def action(message: str) -> None:
    print(f'[🛠] {message}')

def input_(message: str) -> None:
    print(f'📥 {message}')


def output(message: str) -> None:
    print(f'📤 {message}')


def thinking(message: str) -> None:
    print(f'🧠 {message}')


def search(message: str) -> None:
    print(f'🔍 {message}')


def state(message: str) -> None:
    print(f'💾 {message}')


def complete(message: str = 'Execution Complete') -> None:
    print(f'🏁 {message}')


def bullet(message: str) -> None:
    print(f' • {message}')


def kv(key: str, value) -> None:
    '''Pretty key-value output.'''
    print(f'  {key:<20}: {value}')


def block(text: str) -> None:
    '''Indented wrapped text.'''
    print(fill(text, width=WIDTH, subsequent_indent='    '))
