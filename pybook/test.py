tizzfuzz_list = ['TizzFuzz' if num%3==0 and num%5==0 else 'Tizz' if num%3==0 else 'Fuzz' if num%5==0
                else num for num in range(1, 31)]

for item in tizzfuzz_list:
        print(item, end=' ')




