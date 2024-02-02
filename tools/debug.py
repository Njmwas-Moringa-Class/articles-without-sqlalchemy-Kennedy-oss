#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

import ipdb
# Import your classes with the corrected path
from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
    # Create sample instances
    author1 = Author("J.K. Rowling")
    magazine1 = Magazine("Fantasy Today", "Fantasy")
    magazine2 = Magazine("Tech Innovators", "Technology")

    # Add articles
    article1 = author1.add_article(magazine1, "The Magic of Technology")
    article2 = author1.add_article(magazine2, "Innovating Magic")

    # Testing methods
    print(f"Author: {author1.name}")
    print("Articles written by the author:")
    for article in author1.articles:
        print(f"- {article.title} in {article.magazine.name}")

    print("\nMagazines contributed to by the author:")
    for magazine in author1.magazines:
        print(f"- {magazine.name} ({magazine.category})")

    print("\nMagazine contributors for 'Fantasy Today':")
    for contributor in magazine1.contributors():  # Corrected method name here
        print(f"- {contributor.name}")

    # Test Magazine class methods
    print("\nTesting Magazine class methods:")
    print("Magazine.find_by_name('Fantasy Today').name:", Magazine.find_by_name("Fantasy Today").name)
    print("Magazine article titles for 'Fantasy Today':", magazine1.article_titles())

    # Test contributing_authors method
    print("\nContributing authors for 'Tech Innovators':")
    for author in magazine2.contributing_authors():
        print(f"- {author.name}")

    # Start ipdb debugging session
    ipdb.set_trace()

    
    
