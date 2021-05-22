import configparser


def load_config():
    config = configparser.ConfigParser()

    config.read("config.ini")

    config_data = {}
    for section in config.sections():
        config_data[section] = {}
        for option in config.options(section):
            config_data[section][option] = config.get(section, option)

    return config_data


if __name__ == "__main__":
    c = load_config()
    print(c)
