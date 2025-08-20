import os
import instaloader
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

L = instaloader.Instaloader()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌸 Welcome to Pytoonz Instagram Checker! 🌸\n"
        "Send an Instagram username without @ to get profile info.\n"
        "Use /start to see this message again."
    )

async def get_profile_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.strip()
    if not username:
        await update.message.reply_text("Username cannot be empty.")
        return

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        response = (
            f"💤 *Pytoonz Profile Info* 💤\n\n"
            f"💤 *Name*: {profile.full_name}\n\n"
            f"💤 *Username*: {profile.username}\n\n"
            f"💤 *User ID*: {profile.userid}\n\n"
            f"💤 *Bio*: {profile.biography or 'None'}\n\n"
            f"💤 *Category*: {profile.business_category_name or 'N/A'}\n\n"
            f"💤 *Following*: {profile.followees}\n\n"
            f"💤 *Followers*: {profile.followers}\n\n"
            f"💤 *Business Account*: {profile.is_business_account}\n\n"
            f"💤 *Private Account*: {profile.is_private}\n\n"
            f"💤 *Verified*: {profile.is_verified}\n\n"
            f"💤 *Posts*: {profile.mediacount}\n"
        )
        await update.message.reply_text(response, parse_mode='Markdown')
    except instaloader.exceptions.ProfileNotExistsException:
        await update.message.reply_text(f"Profile '{username}' does not exist.")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    application = Application.builder().token(os.getenv("TOKEN")).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_profile_info))

    # Configure webhook
    webhook_url = os.getenv("WEBHOOK_URL")  # e.g., https://checker-bot-xk2l.onrender.com
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8443)),  # Use Render’s PORT or default to 8443
        url_path="/webhook",
        webhook_url=f"{webhook_url}/webhook"
    )

if __name__ == "__main__":
    main()        await update.message.reply_text(response, parse_mode='Markdown')
    except instaloader.exceptions.ProfileNotExistsException:
        await update.message.reply_text(f"Profile '{username}' does not exist.")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    application = Application.builder().token(os.getenv("TOKEN")).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_profile_info))

    # Configure webhook
    webhook_url = os.getenv("WEBHOOK_URL")  # e.g., https://your-app.onrender.com
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8443)),  # Use Render’s PORT or default to 8443
        url_path="/webhook",
        webhook_url=f"{webhook_url}/webhook"
    )

if __name__ == "__main__":
    main()    except instaloader.exceptions.ProfileNotExistsException:
        await update.message.reply_text(f"Profile '{username}' does not exist.")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    application = Application.builder().token("8441847301:AAGDtDAmpCsDsAWrPku2FLU3pT614Bk8WTE").build()

    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_profile_info))

    
    application.run_polling()

if __name__ == '__main__':
    main()
