from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key="7b5a17e458f64dc0ba3d6ed8e8dde1d9",    
)


# فرمان شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('سلام! به فروشگاه بیوتی سنتر خوش آمدید. چه کمکی می‌تونم بکنم؟')

# پاسخ به پیام‌های متنی
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user_message = update.message.text
    userid= update.message.chat['id']

        
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
             {
                "role": "system",
                "content": "تو مشاور آرایشی بهداشتی یه فروشگاه هستی که محصولاتی چون لوازم آرایشی و لوازم برقی مثل ریش تراش  اتو مو،لیزر بابلیس مو،اصلاح مو و از این دست لوازم قیچی،پیشبند،دستکش،انواع برس،مانیکور ،پدیکور،لاین ناخن،لوازم آرایشی هم تمام برند های معتبر موجود است،کیف لوازم آرایشی ساعت کاری مغازه  از ۱۰ صبه تا ۲۲ شب می باشدآدرس مغازه تهران چهار راه منوچهری نبش لاله زار فروشگاه بیوتی سنتر آقای محمدپور تلفن مغازه ۳۳۱۱۲۱۲۵ می باشد با لحنه ای مودب و ایموجی و ههربان پاسخ بده و فقط به سوالات پیرامون محصولات ارایشی و بهداشتی و محصولات ما جواب بده و می تونی نکاتی درباره پوست بهتر نحوه مراقبت از پوست و ناخن و مو هم صحبت کنی "},
            {
                "role": "user",
                "content": user_message
            },
        ],
    )

    message = response.choices[0].message.content
  
    await update.message.reply_text(message)

    # تابع اصلی
def main():
    # توکن ربات تلگرام خود را اینجا جایگزین کنید
    TOKEN = "8080896218:AAFyiqN0jnBryG6-_lXezBmDZt4rFkO7AgU"
    
    # ساخت برنامه
    app = ApplicationBuilder().token(TOKEN).build()
    
    # افزودن هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # شروع ربات
    print("!آماده ام")
    app.run_polling()

if __name__== "__main__":
    main()


#python '.\beuty center.py'

