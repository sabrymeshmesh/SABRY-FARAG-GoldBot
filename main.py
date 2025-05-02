
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "8092979081:AAGyPMOkWyBz0tjdWuA1FF1-E4iNrPZLSOQ"

reply_keyboard = [['🟡 تقرير الذهب', '⚪ سعر الفضة'], ['📊 توقعات الفضة', '📈 آخر توصية']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

CONTACT = (
    "\n\n🟢 للتواصل والاستفسار:\n"
    "📞 ميلاد صبري: 01001757313\n"
    "📞 عماد صبري:\n  – 01001750710\n  – 01276169518"
)

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if "تقرير" in text:
        report = (
            "📊 التقرير الرسمي لسوق الذهب – أولاد صبري:\n\n"
            "▪️ أسعار الذهب في مصر (من iSagha):\n"
            "- عيار 21: 4680 ج\n"
            "- عيار 24: 5330 ج\n"
            "- عيار 18: 3990 ج\n"
            "- جنيه الذهب: 37440 ج\n\n"
            "▪️ السعر العالمي للأوقية: 2324.10 دولار\n"
            "▪️ نسبة التغير اليومية: -12.50 دولار (0.53%) انخفاض\n\n"
            "▪️ التحليل الفني:\n"
            "- الاتجاه العام: هابط\n"
            "- الدعم: 2300 دولار\n"
            "- المقاومة: 2360 دولار\n\n"
            "▪️ التوصية: البيع بحذر\n\n"
            "📰 أهم الأخبار:\n"
            "- توقعات بتثبيت الفائدة الأمريكية – Reuters\n"
            "- ارتفاع الدولار يضغط على الذهب – Bloomberg\n"
            "- DailyForex: كسر دعم 2300 قد يُحفّز البيع\n"
            f"{CONTACT}"
        )
        update.message.reply_text(report)
    elif "فضة" in text:
        silver = (
            "📢 من أولاد صبري – تقارير وتحليلات الذهب والفضة:\n\n"
            "▪️ أسعار الفضة في مصر (من iSagha):\n"
            "- عيار 999: بيع 59.00 ج | شراء 57.25 ج\n"
            "- عيار 925: بيع 54.75 ج | شراء 53.00 ج\n"
            "- عيار 900: بيع 53.25 ج | شراء 51.50 ج\n"
            "- عيار 800: بيع 47.25 ج | شراء 45.75 ج\n"
            "- عيار 600: بيع 35.50 ج | شراء 34.25 ج\n\n"
            "▪️ الأوقية عالميًا: بيع 32.16 $ | شراء 32.14 $\n"
            "📌 المصدر: iSagha + NetDania"
            f"{CONTACT}"
        )
        update.message.reply_text(silver)
    elif "توصية" in text:
        update.message.reply_text(
            "📢 من أولاد صبري – التوصية الحالية:\n\n"
            "📈 البيع بحذر – السوق في اتجاه هابط.\n"
            "📌 المصدر: Arincen / ArabicTrader"
            + CONTACT
        )
    elif "توقعات" in text:
        forecast = (
            "📢 من أولاد صبري – توقعات الفضة:\n\n"
            "- الاتجاه: صعود معتدل\n"
            "- المقاومة القادمة: 26.10 دولار\n"
            "- الدعم الحالي: 24.90 دولار\n\n"
            "📌 التوصية: الشراء بحذر\n"
            "📌 المصدر: DailyForex – Arincen"
            + CONTACT
        )
        update.message.reply_text(forecast)
    else:
        update.message.reply_text("اكتب: تقرير، فضة، توصية، توقعات")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
