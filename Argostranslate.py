import argostranslate.package
import argostranslate.translate


def zh2en():
    from_code = "zh"
    to_code = "en"
    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

    # Translate
    translatedText = argostranslate.translate.translate("你好", from_code, to_code)

    print(translatedText)

def en2zh():
    from_code = "en"
    to_code = "zh"
    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())


    translatedText = argostranslate.translate.translate("Hello World", from_code, to_code)

    print(translatedText)

if __name__ == '__main__':
    en2zh()
    zh2en()
