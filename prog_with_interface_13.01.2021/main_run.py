import sooruzhenija
import zdanija
import ons
import mashino_mesta
import pomeshhenija
import zemelnije_uchastki

use_module = {
        "Здания": zdanija.run,
        "Сооружения": sooruzhenija.run,
        "ОНС": ons.run,
        "Машино-места": mashino_mesta.run,
        "Помещения": pomeshhenija.run,
        "Земельные участки": zemelnije_uchastki.run,
    }


def run(module_name, source_directory, save_directory):
    use_module[module_name](source_directory, save_directory)


if __name__ == '__main__':
    # test run
    pass
