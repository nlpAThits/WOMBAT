from wombat_api.core import connector as wb_conn
from wombat_api.analyse import get_most_similar

wbpath="data/wombat-data/"
wbc = wb_conn(path=wbpath, create_if_missing=False)

wec_ids="algo:glove;dataset:6b;dims:50;fold:1;unit:token"

get_most_similar(wbc, wec_ids, "car")