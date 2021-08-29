#Importent : Change the TOKEN if you made a new bot

import logging
#import pytesseract
import requests

import codecs


from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
# def start(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     update.message.reply_markdown_v2(
#         fr'Hi {user.mention_markdown_v2()}\!',
#         reply_markup=ForceReply(selective=True),
#     )



def start(update,context):
    user = update.effective_user
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id, text= f'Hi {user.first_name} 👋 ' + '\n\nYou can convert an IMG to TEXT. Only you have to do, Just <i><b>send an image</b> witch you wish to extract text. And <b>choose your language.</b></i>' +'''\n\nWe support over <b>20+ languages</b> and our AI is fully optimized. You can send even low quality photos as well. But if you want <b>to know how to get the most accurate result, use</b> /help to get an idea.''' + "\n\nAnd also don't forget to send us your opinion about how far this bot helped you to extract text from an image. It would be very helpful for us. And we expect some bugs will occur when you're using this bot. Don't forget to send some bug reports as well.\n\n<i>Feel free to report or suggest anything to</i>\n@Me_llamo_TOKIO\npawanvikasitha2001@gamil.com (Main Developer)" ,
                     parse_mode=ParseMode.HTML)

    chat_id_convert_to_str = str(chat_id)
    f = open("chat_id.txt", "r+")
    f.write(chat_id_convert_to_str)
    f.close()


    context.bot.send_message(chat_id=378984038, text='1 subs')










def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id,
                             text="<i><b>TEXTER</b> is a most <b>powerful Image to Text converter.</b> And It supports over 20+ languages. Thank you for choosing <b>TEXTER.</b></i>" +
                                    "\n\n<b><u>How do get the best result?</u></b>  🎫" +
                                    "\n\n>> You can simply send or forward an image with text to extract the words." +
                                    "\n\n>> Choose the language correctly." +
                                    "\n\n>> If you are converting a printed media, Then <i>TEXTER</i> will give you the best result. It doesn't care about font or font size. " +
                                    "\n\n>>  If your image got a solid background, Then <i>TEXTER</i> will work perfectly."+
                                    "\n\n>> When you getting a photograph of your book or newspaper, etc, Don't focus only on the area you want to extract. Just get the photograph with some additional areas." +
                                    "\n\n\n\n\n<b><u>For advanced usages only:</u></b>  🌈" +
                                    "\n\n>> <i>TEXTER</i> is a fully automated image-to-text converter. So you don't need to press any special command. Just send an image to extract words from it."+
                                    "\n\n>> If your image got written in 2 languages, <i>TEXTER</i> automatically ignores one language. Most of the time <i>TEXTER</i> gives priority to extract English letters. But if want to extract words from a different languages, You can customize the language."+
                                    "\n\n>> If your image is dark or in low brightness, <i>TEXTER</i> will be getting confused. Because <i>TEXTER</i> will be getting confused. Because TEXTER isn't working on absolutely dark images. But image quality doesn't matter. Even you can send photos of less than 1kb.",
                             parse_mode=ParseMode.HTML)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def OCR_Convert(update, context):
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.get_file(file_id)
    print(newFile)
    newFile.download('downloads.png')
    chat_id = update.message.chat.id
    # context.bot.send_message(chat_id=chat_id,
    #                          text="<i>Your image is being processed..</i>" +
    #                               "<b>\nIt may take some time. Hold On!</b>  🕔",
    #                          parse_mode=ParseMode.HTML)
    print(chat_id)
    print(chat_id)

    #If API is working, then uncomment this and try again.
    '''
    def ocr_space_file(filename, overlay=False, api_key='eab3f8fedd88957', language='eng'):
            payload = {'isOverlayRequired': overlay,
                       'apikey': api_key,
                       'language': language,
                       }
            with open(filename, 'rb') as f:
                r = requests.post('https://api.ocr.space/parse/image',
                                  files={filename: f},
                                  data=payload,
                                  )
            return r.content.decode()

    txt = ocr_space_file(filename='downloads.png')
    # print(type(txt))
    # print(txt)
    '''

    y = 1
    if y != 0:
        keyboard = [
            [
                InlineKeyboardButton("Sinhala [beta]", callback_data='Sinhala'),
                InlineKeyboardButton("Arabic", callback_data='ara'),
                InlineKeyboardButton("Bulgarian", callback_data='bul'),
            ],
            [
                InlineKeyboardButton("Chinese (Sim)", callback_data='chs'),
                InlineKeyboardButton("Chinese (Tra)", callback_data='cht'),
                InlineKeyboardButton("Croatian", callback_data='hrv'),
            ],
            [
                InlineKeyboardButton("Czech", callback_data='cze'),
                InlineKeyboardButton("Danish", callback_data='dan'),
                InlineKeyboardButton("Dutch", callback_data='dut')
            ],
            [
                InlineKeyboardButton("English", callback_data='eng'),
                InlineKeyboardButton("Finnish", callback_data='fin'),
                InlineKeyboardButton("French", callback_data='fre')
            ],
            [
                InlineKeyboardButton("German", callback_data='ger'),
                InlineKeyboardButton("Greek", callback_data='gre'),
                InlineKeyboardButton("Hungarian", callback_data='hun')
            ],
            [
                InlineKeyboardButton("Korean", callback_data='kor'),
                InlineKeyboardButton("Italian", callback_data='ita'),
                InlineKeyboardButton("Japanese", callback_data='jpn')
            ],
            [
                InlineKeyboardButton("Polish", callback_data='pol'),
                InlineKeyboardButton("Portuguese", callback_data='por'),
                InlineKeyboardButton("Russian", callback_data='rus')
            ],
            [
                InlineKeyboardButton("Solvenian", callback_data='slv'),
                InlineKeyboardButton("Spanish", callback_data='spa'),
                InlineKeyboardButton("Swedish", callback_data='swe')
            ],
            [
                InlineKeyboardButton("Turkish", callback_data='tur'),
                InlineKeyboardButton("Hindi [beta]", callback_data='Hindi'),
                InlineKeyboardButton("Norwegian [beta]", callback_data='Norwegian')
            ],
            [InlineKeyboardButton("Detect Automatically [beta version]", callback_data='3')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)


        update.message.reply_text(
            "<b>Select the language your image is written in :</b>", reply_markup=reply_markup ,parse_mode= ParseMode.HTML)




def button(update, context):
        query = update.callback_query
        query.answer()
        query.edit_message_text(text=f"Your langauge is: {query.data}")
        OCR_SPACE_API_KEY = 'eab3f8fedd88957'
        #print(chat_id)

        f = open("chat_id.txt", "r")
        with open('chat_id.txt', 'r') as f2:
            data = f2.read()
            chat_id = int(data)
            print(chat_id)



        if query.data == 'Sinhala':
            language = "Sinhala (සිංහල)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Sinhala (සිංහල)")
            query.edit_message_text(text="This language doesn't available yet")

        if query.data == 'ara':
            language = "Arabic (العربية)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Arabic (العربية)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='ara'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'bul':
            language = "Bulgarian (български)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Bulgarian (български)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='bul'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'chs':
            language = "Chinese (Simplified) (中文)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Chinese (Simplified) (中文)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='chs'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)



        if query.data == 'cht':
            language = "Chinese (Traditional) (中文)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Chinese (Traditional) (中文)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='cht'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'hrv':
            language = "Croatian (Hrvatski)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Croatian (Hrvatski)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='hrv'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'cze':
            language = "Czech (čeština)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Czech (čeština)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='cze'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'dan':
            language = "Danish (dansk)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Danish (dansk)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='dan'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'dut':
            language = "Dutch (Nederlands)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Dutch (Nederlands)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='dut'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)


        if query.data == 'eng':
            language = "English"
            print("Yes")
            query.edit_message_text(text="<b>Hold on...  🕐</b>",parse_mode= ParseMode.HTML )

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='eng'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)





            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            #Don't confused. You only have to change this. This is a tresserat module
            # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
            # txt = (pytesseract.image_to_string(r'downloads.png'))
            # print(txt)

            if len(extracted_text) == 0:
                query.edit_message_text("<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>", parse_mode=ParseMode.HTML)
            else:
                f = open("CorrectAlign.txt", "w")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', 'r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)



                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id, text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>", parse_mode=ParseMode.HTML)

        if query.data == 'fin':
            language = "Finnish (suomi)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Finnish (suomi)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='fin'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'fre':
            language = "French (français)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: French (français)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='fre'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'ger':
            language = "German (Deutsch)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: German (Deutsch)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='ger'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'gre':
            language = "Greek (ελληνικά)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Greek (ελληνικά)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='gre'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'hun':
            language = "Hungarian (magyar)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Hungarian (magyar)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='hun'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'kor':
            language = "Korean (한국어)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Korean (한국어)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='kor'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'ita':
            language = "Italian (italiano)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Italian (italiano)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='ita'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'jpn':
            language = "Japanese (日本語)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Japanese (日本語)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='jpn'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'pol':
            language = "Polish (język)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Polish (język)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='pol'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'por':
            language = "Portuguese (português)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Portuguese (português)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='por'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)





        if query.data == 'rus':
            language = "Russian (Русский)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Russian (Русский)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='rus'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))


            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w","utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding = 'utf-16', mode = 'r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)




        if query.data == 'slv':
            language = "Slovenian (slovenščina)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Slovenian (slovenščina)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='slv'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)

        if query.data == 'spa':
            language = "Spanish (español)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Spanish (español)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='spa'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)



        if query.data == 'swe':
            language = "Swedish (Svenska)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Swedish (Svenska)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='swe'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)


        if query.data == 'tur':
            language = "Turkish (Türkçe)"
            print("Yes")
            query.edit_message_text(text="Your langauge is: Turkish (Türkçe)")
            query.edit_message_text(text="<b>Hold on...  🕐</b>", parse_mode=ParseMode.HTML)

            def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='tur'):

                payload = {'isOverlayRequired': overlay,
                           'apikey': api_key,
                           'language': language,
                           }
                with open(filename, 'rb') as f:
                    r = requests.post('https://api.ocr.space/parse/image',
                                      files={filename: f},
                                      data=payload,
                                      )
                return r.content.decode()

            txt = ocr_space_file(filename='downloads.png')
            print(txt)

            def find_between(txt, first, last):
                try:
                    start = txt.index(first) + len(first)
                    end = txt.index(last, start)
                    return txt[start:end]
                except ValueError:
                    return ""

            extracted_text = (find_between(txt, '''"ParsedText":"''', '''","ErrorMessage"'''))

            if len(extracted_text) == 0:
                query.edit_message_text(
                    "<b>¯\_(ツ)_/¯ Sorry! Couldn't extract anything from this image.</b>\n\n<i><b>But you can try:  ♻️</b>\n - Send the image again\n - Make sure that, image contain words.\n - Change the language\n - Try again later\n - Send us a bug report\n\n<b>click on /help to get a best result</b></i>",
                    parse_mode=ParseMode.HTML)
            else:
                f = codecs.open("CorrectAlign.txt", "w", "utf-16")
                f.write(extracted_text)
                f.close()

                with open('CorrectAlign.txt', encoding='utf-16', mode='r') as f2:
                    data = f2.read()
                    print(data)
                    data.encode('unicode_escape')
                    Temresult = data.replace("\\n", "\n")
                    result = Temresult.replace("\\r", "\r")
                    print(result)

                query.edit_message_text(result)
                context.bot.send_message(chat_id=chat_id,
                                         text="<i>If you are not satisfy with the result,</i> <b>\nClick on /help</b> or <b>try again.</b>",
                                         parse_mode=ParseMode.HTML)


        if query.data == 'Hindi':
            language = "HINDI [Beta]"
            print("NO")
            query.edit_message_text(text="This language doesn't available yet")


        if query.data == 'Norwegian':
            language = "Norwegian [Beta]"
            print("Yes")
            query.edit_message_text(text="This language doesn't available yet")

        # else:
        #     query.edit_message_text(text="BETA Versions didn't released yet")
        #     print(query.data)





def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1974731904:AAFw966PHgny7S5UuQphAb94iA1V8FHo9gk")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher


    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("OCR", OCR_Convert))
    dispatcher.add_handler(MessageHandler(Filters.forwarded & Filters.photo, OCR_Convert))
    dispatcher.add_handler(MessageHandler(Filters.photo, OCR_Convert))
    dispatcher.add_handler(CallbackQueryHandler(button))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



if __name__ == '__main__':
    main()
