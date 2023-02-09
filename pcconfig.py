import pynecone as pc


config = pc.Config(
    app_name="Connect_Us",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
