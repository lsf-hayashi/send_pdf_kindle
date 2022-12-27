import aiosmtplib

class Server():
    def __init__(self, username, password):
        self.hostname='smtp.gmail.com'
        self.port=465
        self.username = username
        self.password = password
        self.use_tls = True
    
    async def send(self, msg):
        await aiosmtplib.send(
            msg,
            hostname=self.hostname,
            port=self.port,
            username=self.username,
            password=self.password,
            use_tls=self.use_tls)