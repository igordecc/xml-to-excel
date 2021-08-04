import ConverterMashinoMesta
import ConverterONS
import ConverterPomeshhenija
import ConverterSooruzhenija
import ConverterZdanija
import ConverterZemelnieUchastki
import sooruzhenija
import zdanija
import ons
import mashino_mesta
import pomeshhenija
import zemelnije_uchastki

use_module = {
        "Здания": ConverterZdanija.run,
        "Сооружения": ConverterSooruzhenija.run,
        "ОНС": ConverterONS.run,
        "Машино-места": ConverterMashinoMesta.run,
        "Помещения": ConverterPomeshhenija.run,
        "Земельные участки": ConverterZemelnieUchastki.run,
    }


def run(module_name, source_directory, save_directory):
    import os.path
    use_module[module_name](source_directory, save_directory)


if __name__ == '__main__':
    # test run
    pass
