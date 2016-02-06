import debruijn

def test_create():
   k = 4
   text = 'AAGATTCTCTAAGA'

   expected = {'AAG': ['AGA', 'AGA'], 'TCT': ['CTC', 'CTA'], 'GAT': ['ATT'], 'AGA': ['GAT'], 'ATT': ['TTC'], 'CTA': ['TAA'], 'CTC': ['TCT'], 'TTC': ['TCT'], 'TAA': ['AAG']}
   actual = debruijn.create(text, k)

   assert(expected == actual)
