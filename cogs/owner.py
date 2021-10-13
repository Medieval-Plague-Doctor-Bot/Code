import io
import discord
import contextlib
from traceback import format_exception
from discord.ext import commands
from discord.ext.buttons import Paginator
from tools import utils

class Pag(Paginator):
  async def teardown(self):
    try:
      await self.page.delete()
    except discord.HTTPException:
      pass


class owner(commands.Cog):
  
  def __init__(self,bot):
    self.bot = bot


  @commands.command(name = "eval")
  @commands.is_owner()
  async def _eval(self,ctx, *, _code):
      code = utils.clean_code(_code)
      code = utils.indent(_code,"    ")
      local_variables = {
          "ctx" : ctx,
          "bot" : self.bot,
          "guild" : ctx.guild,
          "channel" : ctx.channel,
          "message" : ctx.message
      }

      stdout = io.StringIO()
      await ctx.message.add_reaction("▶")
      try:
        with contextlib.redirect_stdout(stdout):
          exec(f"async def func():\n{code}", local_variables,)
          obj = await local_variables["func"]()
          result = f"{stdout.getvalue()}\n-- {obj}\n"
      
      except Exception as e:
          result = "".join(format_exception(e, e, e.__traceback__))

      output = [result[i: i + 2000] for i in range(0, len(result), 2000)]
  
      pager = Pag(
          timeout = None,
          entries = output,
          length = 1,
          prefix = "```py\n",
          suffix = "```"
      )
      
      await pager.start(ctx)
      await ctx.message.add_reaction("✅")


def setup(bot: commands.Bot):
  bot.add_cog(owner(bot))
