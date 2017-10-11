# Programming Collective Intelligence, by Toby Segaran

- **Author**: Valter Nepomuceno
- **When**: October, 2017
- **Based in**: Lisbon, Portugal
- **Current Job**: Software Developer
- **Email Address**: valter.nep@gmail.com
- **Reference Links**: [LinkedIn](https://pt.linkedin.com/in/valternepomuceno) | [GitHub](https://github.com/Vnepomuceno) | [Facebook](https://www.facebook.com/valter.nepomuceno)

## Chapter 3

### Word Vectors

Generate word count file from the feedlist from file ```feedlist.txt``` that contains blog feeds.

```python
$ python generatefeedvector.py
```

Running the script above generates the output of word count into file ```blogdata.txt```

### Hierarchical Clustering

Run the hierarchical clustering over the data generated in the previous section into the output file ```blogdata.txt```, executing the following commands.

```python
$ python
>> import clusters
>> blog_names, words, data = clusters.read_file('blogdata.txt')
>> clust = clusters.hcluster(data)
>> clusters.print_clust(clust, labels = blog_names)
```

The last command traverses the clustering tree recursively and prints it in the Terminal like a file system hierarchy.