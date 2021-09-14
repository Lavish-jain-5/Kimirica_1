from CMText.TextClient import TextClient,WhatsappTemplate

class Myclass():
    key='c412543b-3010-461a-a897-7eef8c4b91b5'
    template_namespace = "b90d0861_9fdb_4223_b92b_b493a2314205"
    template_element_name = "order_confirmation"

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.template_parameters = [{
            "type": "body",
            "parameters": [
                {
                    "type": "text",
                    "text": self.name
                },
                {
                    "type": "text",
                    "text": self.id
                },
                {
                    "type": "text",
                    "text": "https://www.google.com/search?q=201+error+code+in+cm.com+api&oq=&aqs=chrome.0.69i59i450l8.399880j0j7&sourceid=chrome&ie=UTF-8"
                },
                {
                    "type": "text",
                    "text": "Kimirica"
                },
            ]
        }]

    def new_func(self):
        template = WhatsappTemplate(self.template_namespace, self.template_element_name,self.template_parameters)
        client = TextClient(apikey=self.key)

        client.AddWhatsappTemplateMessage(from_='00919584133944', to=['00919826962945'], template=template,)
        response = client.send()

        print(response.text)

