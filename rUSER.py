import smtplib
import email.message


#essa def envia o e-mail para o admin, informando que sua notícia teve um comentário e exibe qual foi o comentário
# vou ajeitar dps
'''def send_email(email_adm, comment, id):
    x = email_adm[id][0]
    y = comment[id][1]

    msg = email.message.Message()
    msg['Subject'] = 'Comentaram na sua notícia'
    msg['From'] = 'jamesbot.ifpb@gmail.com'
    msg['To'] = x
    password = 'lied uthj dsde rdax'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(y)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('E-mail enviado')'''


#essa def serve para o usuário buscar uma noticia
def user_search_news(news, usuario):
    emoji_like = '👍'
    while True:
        id_to_search = int(input('Informe o id da noticia para busca-la:'))
        for x, y in news.items():
            if id_to_search in y:
                print(f'\033[96mAutor: {x}\033[0m')
                for z in y:
                    print(f'Título: {y[z][0]}')
                    print(f'Artigo: {y[z][1]}')
                    print('_' * 26)
            else:
                print('\033[91mID inexistente!\033[0m')
                break
        comment_question = input('Deseja fazer um comentário? sim/nao')
        if comment_question == 'sim':
            comment = str(input('Comentário:'))
            question = input('Deseja comentar mais? sim/nao')
            for x, y in news.items():
                if id_to_search in y:
                    news[x][id_to_search][2].append(comment)
                    print('Comentário adicionado')
            if question == 'sim':
                continue
            elif question == 'nao':
                break
            else:
                print('Digite algo válido')
                break
        elif comment_question == 'nao':
            break

    '''send_email(data_news, all_news, search_id)'''
    '''yes_or_no = input('Ainda quer comentar mais alguma coisa? sim/nao')
                                    if yes_or_no == 'nao':
                                        break
                                    like_question = input('Deseja curtir essa notícia? sim/nao')
                                    if like_question == 'sim':
                                        news[search_id].append(emoji_like)
    
                                    yes_or_no = input('Deseja continuar procurando? sim/nao')
                                    if yes_or_no == 'nao':
                                        break
    
                                else:
                                    print('Não existe nenhuma notícia com esse ID.')
                                    yes_or_no = input('Deseja continuar procurando? sim/nao')
                                    if yes_or_no == 'nao':
                                        break'''


#essa def serve para o usuário comentar na notícia
def user_comment_news(news):
    while True:
        comment_id = int(input('Informe o ID da notícia para comentar:'))
        comment = str(input('Comentário:'))
        for x, y in news.items():
            if comment_id in y:
                news[x][comment_id][2].append(comment)
        yes_or_no = input('Ainda quer comentar mais alguma coisa? sim/nao')
        if yes_or_no == 'nao':
            break
        elif yes_or_no == 'sim':
            continue
        else:
            print('Digite algo válido')
            break





#essa def serve para o usuário curtir a notícia
def user_like_news(news):
    while True:
        emoji_like = 1
        like_id = int(input('Informe o ID da notícia para curti-la:'))
        for x, y in news.items():
            if emoji_like in y:
                news[x][like_id][3].append(emoji_like)
                print('Curtida adicionada')
        question = input('Deseja curtir mais? sim/nao')
        if question == 'nao':
            break
        elif question == 'sim':
            continue
        else:
            print('Id invalido')
            break


#essa def serve para o usuário listar as notícias
def user_list_news(news):
    for x, y in news.items():
        print(f'Autor: {x}')
        for z in y:
            print(f'Publicado em {y[z][4]}')
            print(f'Título: {y[z][0]}')
            print(f'Artigo: {y[z][1]}')
            comment = ', '.join(y[z][2])
            print(f'Comentários: {comment}') if comment else ''
            print(f'{y[z][3]}❤️')
            print('_' * 26)
