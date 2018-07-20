from cefpython3 import cefpython as cef
import sys

smartDataOwnerUrl = "http://127.0.0.1:8000/owner/start"
requesterUrl = "http://127.0.0.1:8000/requester/start"

class Client:
    def __init__(self, url, title):
        self.openCliet(url, title)

    def openCliet(self, url="http://google.com", title="Client"):
        cef.CreateBrowser(url=url,
                              window_title=title)

if __name__ == "__main__":
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()

    smartDataOwnerClient = Client(smartDataOwnerUrl, "Smart Data Owner - Client")
    requesterClient = Client(requesterUrl, "Requester - Client")

    cef.MessageLoop()
    cef.Shutdown()
