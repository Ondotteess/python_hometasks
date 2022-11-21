import io
import sys
from typing import TextIO
import os



def solution(script: TextIO, output: TextIO) -> None:

        def file_in_dir(path, ext):
                for file in os.listdir(path):
                        if ext in file:
                                return 1
                return 0

        def tree(path, level=0, pattern=None, depth=-1, exten=0, first = '│'):

                if depth == 0:
                        return 0
                p = path.split('\\')


                if level == 1 and (pattern == 1 or pattern == 3) and exten != 0:
                        ident = '├' + '─' * 2 + ' '

                elif level == 1 and pattern == 1 and exten == 0:
                        ident = '├' + '─' * 2 + ' '

                elif level == 1 and pattern == 3 and exten == 0:
                        ident = '└' + '─' * 2 + ' '

                elif level == 2 and pattern == 1:
                        ident = first + ' ' * (level - 1) * 3 + '├' + 2 * '─' + ' '

                elif level == 2 and pattern == 2:
                        ident = first + ' ' * (level-1) * 3  + '└' + 2 * '─' + ' '

                elif level == 2 and pattern == 3:
                        ident = first + ' ' * (level-1) * 3 + '└' + 2 * '─' + ' '

                elif level > 2 and pattern == 1:
                        ident = first + ' ' * (level-1) * 3 + ' ' + '├' + 2 * '─' + ' '

                elif level > 2 and pattern == 2:
                        ident = first + ' ' * (level-1) * 3 + ' ' + '└' + 2 * '─' + ' '

                elif level > 2 and pattern == 3:
                        ident = first + ' ' * (level-1) * 3 + ' ' + '└' + 2 * '─' + ' '



                if os.path.isdir(path):

                        if level == 1 and exten != 0:
                                l = os.listdir(os.path.join(path, os.pardir))
                                _l = [x for x in l if os.path.isdir(x)]
                                if p[-1] == _l[-1]:
                                        print(_l)
                                        ident = '└' + '─' * 2 + ' '
                                        first = ' '


                        if level != 0 and exten == 0:
                                #print(f"{ident}{p[-1]}")
                                output.write(f"{ident}{p[-1]}\n")

                        elif level != 0 and exten != 0:
                                output.write(f"{ident}{p[-1]}\n")
                                #print(f"{ident}{p[-1]}")


                        for dir in os.listdir(path):
                                sort_dir = sorted(os.listdir(path))

                                #if len(os.listdir(path)) == 0:
                                #        tree(path + '\\' + dir, level + 1, pattern=2, depth=depth-1, exten=exten, first= first)

                                if dir == sort_dir[-1]:
                                        tree(path + '\\' + dir, level + 1, pattern=3, depth=depth-1, exten=exten, first = first)

                                else:
                                        tree(path + '\\' + dir, level + 1, pattern=1, depth=depth-1, exten=exten, first=first)

                else:
                        if exten != 0:
                                if exten in p[-1]:
                                        output.write(f"{ident}{p[-1]}\n")
                                        #print(f"{ident}{p[-1]}")


                        else:
                                output.write(f"{ident}{p[-1]}\n")





        path = os.getcwd()

        cmd = []
        for line in script:
                cmd.append(line)

        for i in range(len(cmd)):
                command = cmd[i].strip().split(' ')


                if command[0] == 'mkdir':
                        os.mkdir(command[1])
                        #print('dir maked')


                if command[0] == 'cd':
                        if command[1] != '..':
                                os.chdir(command[1])
                                #print('dir changed')
                        else:
                                for _ in range(len(command[-1].split('\\'))):
                                        os.chdir(os.pardir)
                                #print('dir changed')


                if command[0] == 'ls':
                        if len(command) == 1:
                                for filename in os.listdir(os.getcwd()):
                                        output.write(filename+' ')
                                output.write('\n')
                        else:
                                for filename in command[1]:
                                        output.write(filename+' ')
                                output.write('\n')

                if command[0] == 'cat':
                        if '>' not in command and '>>' not in command:
                                for i in range(1, len(command)):
                                        with open(command[i], 'r', encoding='utf-8') as file:
                                                lines = file.readlines()
                                                for line in lines:
                                                        output.write(line)
                                                        print(line.strip())

                        if '>' in command:
                                lines = []
                                for i in range(1, len(command)-2):
                                        with open(command[i], 'r', encoding='utf-8') as file:
                                                lines += file.readlines()

                                with open(command[-1], 'w', encoding='utf-8') as file:
                                        for line in lines:
                                                file.write(line)

                        if '>>' in command:
                                lines = []
                                for i in range(1, len(command)-2):
                                        with open(command[i], 'r', encoding='utf-8') as file:
                                                lines += file.readlines()
                                with open(command[-1], 'a', encoding='utf-8') as file:
                                        for line in lines:
                                                file.write(line.strip()+'\n')


                if command[0] == 'tac':
                        if '>' not in command and '>>' not in command:
                                for i in range(1, len(command)):
                                        with open(command[i], 'r', encoding='utf-8') as file:
                                                lines = file.readlines()
                                                lines.reverse()
                                                for line in lines:
                                                        #print(line.strip())
                                                        output.write(line+' ')
                                                        print(line.strip())

                        if '>' in command:
                                lines = []
                                sub = []
                                for i in range(1, len(command)-2):
                                        with open(command[i], 'r', encoding='utf-8') as file:
                                                sub+= file.readlines()
                                        sub.reverse()
                                        lines += sub
                                        sub = []
                                with open(command[-1], 'w', encoding='utf-8') as file:
                                        #lines.reverse()
                                        for line in lines:
                                                file.write(line.strip()+'\n')

                        if '>>' in command:
                                lines = []
                                sub = []
                                for i in range(1, len(command)-2):
                                        with open(command[i], 'r', encoding='utf-8') as file:
                                                sub += file.readlines()
                                        sub.reverse()
                                        lines += sub
                                        sub = []
                                with open(command[-1], 'a', encoding='utf-8') as file:
                                        #lines.reverse()
                                        for line in lines:
                                                file.write(line.strip()+'\n')

                if command[0] == 'pwd':
                        #output.write(os.getcwd())
                        print(os.getcwd())
                        if '>' in command:
                                with open(command[-1], 'w', encoding='utf-8') as file:
                                        file.write(os.getcwd())

                        print(os.getcwd())

                if command[0] == 'tree':
                        output.write('.\n')
                        d = -1
                        ext = 0
                        if '-L' in command:
                                d = int(command[command.index('-L')+1])+1

                        if '-P' in command:
                                ext ='.'+command[command.index('-P')+1].strip('""').split(".")[-1]

                        tree(os.getcwd(), depth=d, exten = ext)




    


if __name__ == '__main__':
    print("$ ", end="")
    for line in sys.stdin:
        solution(io.StringIO(line), sys.stdout)
        print("$ ", end="")
