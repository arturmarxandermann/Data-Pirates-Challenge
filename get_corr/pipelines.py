from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter
import json
import os


class RemoveDuplicates:
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        #THIS METHOD IS USED TO VERIFY IF ANY
        # ITEM HAS ALREADY BEEN ADDED
        adapter = ItemAdapter(item)
        if adapter['Faixa_de_CEP'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ids_seen.add(adapter['Faixa_de_CEP'])
            return item

class JsonLineWriterPipeline:

    def process_item(self, item, spider):
        # THIS METHOD IS USED TO PROCESS AND SAVE
        # EACH ITEM TAKEN IN CORRS SPIDER
        save_path = './Data'
        file_name = f"{item['UF']}.jsonl"
        complete_name = os.path.join(save_path, file_name)
        print(f"COLLECTING THE ZIP CODE OF {item['Cidade']} FROM {item['UF']}.")

        with open(complete_name, 'a') as file:
            line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
            file.write(line)

