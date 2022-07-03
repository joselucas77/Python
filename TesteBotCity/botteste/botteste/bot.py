from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.

        # Bot com o Telegram
        # executando/abrindo o Telegram
        self.execute(r"C:\Users\jose_\AppData\Roaming\Telegram Desktop\Telegram.exe")
        # codigo para encotrar algo na tela, neste caso a barra de pesquisa do app
        if not self.find( "pesquisar contato", matching=0.97, waiting_time=10000):
            self.not_found("pesquisar contato")
        # comando de para clicar
        self.click()
        # comando para escrever
        self.paste('rascunho')
        
        if not self.find( "contato", matching=0.97, waiting_time=10000):
            self.not_found("contato")
        self.click()

        self.paste('O pai ta ON...receeeba!')
        # comando para dar enter
        self.enter()
        

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

 
    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()



