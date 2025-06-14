from asyncio import Event

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
from telegram.ext import ApplicationBuilder, ChatMemberHandler, CommandHandler

from . import config
from .handler.chat_handler import addition
from .handler.command_handler import hello, resinday
from .scheduler import scheduled_task


async def runner():
    application = ApplicationBuilder().token(config.BOTTOKEN).build()
    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(ChatMemberHandler(addition))
    application.add_handler(CommandHandler(["resin", "r"], resinday))
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    config.logger.info("Telegram command handler started.")

    scheduler = AsyncIOScheduler(timezone=timezone(config.TIMEZONE))
    for iter in config.HOURLIST:
        scheduler.add_job(scheduled_task, trigger="cron", hour=iter, minute=0)
    scheduler.start()
    config.logger.info("Scheduler started.")

    try:
        await Event().wait()
    except (KeyboardInterrupt, SystemExit):
        config.logger.warning("Shutting down.")
