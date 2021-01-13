import zdanija_ons
import sooruzhenija
import pomeshhenija
import zemelnije_uchastki

module_map = {
        "Здания": zdanija_ons.run,
        "Сооружения": sooruzhenija.run,
        "Помещения и машино-места": pomeshhenija.run,
        "Земельные участки": zemelnije_uchastki.run,
    }


def run(module_name, source_directory, save_directory):
    module_map[module_name](source_directory, save_directory)


if __name__ == '__main__':
    # test run
    pass
