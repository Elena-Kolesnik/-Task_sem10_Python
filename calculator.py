from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import mytoken
import cmath


async def plus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    num1 = msg_split[1]
    num2 = msg_split[2]
    await update.message.reply_text(f'{num1} + {num2} = {float(num1) + float(num2)}')


async def minus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    num1 = msg_split[1]
    num2 = msg_split[2]
    await update.message.reply_text(f'{num1} - {num2} = {float(num1) - float(num2)}')


async def mult(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    num1 = msg_split[1]
    num2 = msg_split[2]
    await update.message.reply_text(f'{num1} * {num2} = {float(num1) * float(num2)}')


async def div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    num1 = msg_split[1]
    num2 = msg_split[2]
    await update.message.reply_text(f'{num1} / {num2} = {float(float(num1) / float(num2))}')


async def compl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    print(msg_split)
    num1 = msg_split[1]
    num2 = complex(msg_split[2])
    await update.message.reply_text(f'{num1} + {num2} = {abs((float(num1) + num2))}')

    


async def helpp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Сумма - /plus число число\nРазница - /minus число число\nУмножение - /mult число число\nДеление - /div число число\nКомплексное сложение - /comp число комплексное число")

if __name__ == '__main__':
    app = ApplicationBuilder().token(mytoken.MYTOKEN).build()
    app.add_handler(CommandHandler("plus", plus))
    app.add_handler(CommandHandler("minus", minus))
    app.add_handler(CommandHandler("mult", mult))
    app.add_handler(CommandHandler("div", div))
    app.add_handler(CommandHandler("help", helpp))
    app.add_handler(CommandHandler("comp", compl))
    app.run_polling()
