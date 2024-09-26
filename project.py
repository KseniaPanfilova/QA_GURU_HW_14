import pydantic
import dotenv

class Config(pydantic.BaseSettings):
    remote_url: str = 'http://hub.browserstack.com/wd/hub'
    timeout: float = 10.0
    userName: str = pydantic.Field(None, env=['bs.userName', 'userName'])
    accessKey: str = pydantic.Field(None, env=['bs.accessKey', 'accessKey'])


config = Config(dotenv.find_dotenv('.env'))
