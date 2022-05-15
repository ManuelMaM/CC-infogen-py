# CC-infogen-py

Python clas for generating randon valid credit cards numbers expiration dates and security codes, for testing proposes.

```
def gen(self, quant : int,length = 16, cc_number = 0) -> list:
```
**USAGE EXEMPLES**

Create credit cards info with a given bin number:
```
from ccgenerator import Cgen
cc_generator = Cgen()
my_cc_list = cc_generator.gen(10,16,123456)
```
Create multiple credit cards info with randon bins:
```
from ccgenerator import Cgen
cc_generator = Cgen()
my_cc_list = []

for i in range(10000):
  temp_cc = cc_generator.gen(1)
  my_cc_list.append(temp_cc)
```
