{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Display Message in Python"
      ],
      "metadata": {
        "id": "ntm-gByNssKo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#This is single comment\n",
        "'''multiline \n",
        "comment'''\n",
        "print(\"Hello all\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HbBZShF7tAbt",
        "outputId": "6b9437d4-eabf-44cb-d620-d89baf3ad738"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello all\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Input in Python"
      ],
      "metadata": {
        "id": "W540UbzvtnGe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "name=input(\"Enter your name:\")\n",
        "print(name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xoQuUUjettZ7",
        "outputId": "f07de7c8-9d93-4aa5-8a25-7489c8b4d7a4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name:Akshata\n",
            "Akshata\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Data Type In Python\n",
        "\n",
        "1. Number"
      ],
      "metadata": {
        "id": "Mjwfplc4uFE-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n1=234\n",
        "n2=214\n",
        "print(n1)\n",
        "print(n2)\n",
        "print(n1+n2)\n",
        "n3=432.90\n",
        "print(type(n3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jNAmmHPTuMp3",
        "outputId": "3d95e6f4-e8bd-4897-c55c-79aa5ea54f9e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "234\n",
            "214\n",
            "448\n",
            "<class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. String"
      ],
      "metadata": {
        "id": "9teCEQTXutAi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "str=\"Welcome to python\"\n",
        "print(str)\n",
        "print(str[1:4])\n",
        "print(str[-2])\n",
        "print(str*2)\n",
        "print(str+' language')\n",
        "print(str.upper())\n",
        "print(str.lower())\n",
        "print(str.replace('to','programming'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EJz3uXsN2iYZ",
        "outputId": "f92efb48-f108-4228-c449-483e6a873bcc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to python\n",
            "elc\n",
            "o\n",
            "Welcome to pythonWelcome to python\n",
            "Welcome to python language\n",
            "WELCOME TO PYTHON\n",
            "welcome to python\n",
            "Welcome programming python\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. List"
      ],
      "metadata": {
        "id": "Ow2gUbZU3JLG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "list1=[10,20,30,40,50]\n",
        "list2=[\"Akshata\",\"Pinki\",\"Shravani\",\"Rutuja\",\"Riya\"]\n",
        "list3=[101,\"Akshata\",102,\"Riya\",103,\"Rutuja\"]\n",
        "print(\"List elements are:\")\n",
        "i=0\n",
        "while i<list2.__len__():\n",
        "  print(\"At index\",i,\"element is\",list2[i])\n",
        "  i=i+1\n",
        "\n",
        "#list operations\n",
        "#slice\n",
        "print(list2[0:3])\n",
        "print(list1[-4:-1])\n",
        "\n",
        "#append\n",
        "list1.append(60)\n",
        "print(\"after append:\",list1)\n",
        "\n",
        "#insert\n",
        "list2.insert(2,\"aditi\")\n",
        "print(\"after insert:\",list2)\n",
        "\n",
        "#extend\n",
        "list2.extend(list3)\n",
        "print(\"after extend:\",list2)\n",
        "\n",
        "#update\n",
        "list3[1]=100\n",
        "print(\"updated list:\",list3)\n",
        "\n",
        "#delete\n",
        "del list1[2]\n",
        "list2.remove(\"Akshata\")\n",
        "print(\"after delete:\",list1,\"after remove:\",list2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SOp17Xdh4qJG",
        "outputId": "9d23766e-adf7-4c33-f7dc-267869f83a71"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "List elements are:\n",
            "At index 0 element is Akshata\n",
            "At index 1 element is Pinki\n",
            "At index 2 element is Shravani\n",
            "At index 3 element is Rutuja\n",
            "At index 4 element is Riya\n",
            "['Akshata', 'Pinki', 'Shravani']\n",
            "[20, 30, 40]\n",
            "after append: [10, 20, 30, 40, 50, 60]\n",
            "after insert: ['Akshata', 'Pinki', 'aditi', 'Shravani', 'Rutuja', 'Riya']\n",
            "after extend: ['Akshata', 'Pinki', 'aditi', 'Shravani', 'Rutuja', 'Riya', 101, 'Akshata', 102, 'Riya', 103, 'Rutuja']\n",
            "updated list: [101, 100, 102, 'Riya', 103, 'Rutuja']\n",
            "after delete: [10, 20, 40, 50, 60] after remove: ['Pinki', 'aditi', 'Shravani', 'Rutuja', 'Riya', 101, 'Akshata', 102, 'Riya', 103, 'Rutuja']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Tuples"
      ],
      "metadata": {
        "id": "RGuYabuq9LDc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tuple1=(10,20,30,40)\n",
        "tuple2=(\"ak\",\"pk\",\"ck\",\"dk\",\"mk\")\n",
        "print(tuple1[2])\n",
        "print(type(tuple2))\n",
        "print(tuple1[-4:-1])\n",
        "for element in tuple2:\n",
        " print(element)\n",
        "a=tuple1.__len__()\n",
        "print(\"length of tuple1:\",a)\n",
        "tuple3=tuple1+tuple2\n",
        "print(tuple3)\n",
        "del tuple3\n",
        "#we cannot add or delete particular element because tuples are immutable"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zp3DXnck-Qq4",
        "outputId": "6d79d84e-3be6-4ba4-d31d-5ab00e7339a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n",
            "<class 'tuple'>\n",
            "(10, 20, 30)\n",
            "ak\n",
            "pk\n",
            "ck\n",
            "dk\n",
            "mk\n",
            "length of tuple1: 4\n",
            "(10, 20, 30, 40, 'ak', 'pk', 'ck', 'dk', 'mk')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. Set"
      ],
      "metadata": {
        "id": "7AzrkKkj_53k"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "set1={10,20,30,40,50}\n",
        "set2={100,13.24,\"hello\",(1,2,3,4)}\n",
        "set3={1,2,3,4,5}\n",
        "set4={6,4,3,5,7}\n",
        "print(set2)\n",
        "\n",
        "#set operations\n",
        "set1.discard(20)\n",
        "print(\"after discard:\",set1)\n",
        "\n",
        "set2.remove(\"hello\")\n",
        "print(\"after remove:,set2\")\n",
        "\n",
        "set1.pop()\n",
        "print(\"after pop:\",set1)\n",
        "\n",
        "set5=set3|set4\n",
        "print(\"after union:\",set5)\n",
        "\n",
        "set6=set3.intersection(set4)\n",
        "print(\"after inmtersection:\",set6)\n",
        "\n",
        "set7=set3-set4\n",
        "print(\"after set difference:\",set7)\n",
        "\n",
        "set8=set3^set4\n",
        "print(\"after symmetric difference:\",set8)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X9qtUsQj_7kf",
        "outputId": "2f63b882-549f-4738-8641-a5198ca3a0f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'hello', (1, 2, 3, 4), 100, 13.24}\n",
            "after discard: {40, 10, 50, 30}\n",
            "after remove:,set2\n",
            "after pop: {10, 50, 30}\n",
            "after union: {1, 2, 3, 4, 5, 6, 7}\n",
            "after inmtersection: {3, 4, 5}\n",
            "after set difference: {1, 2}\n",
            "after symmetric difference: {1, 2, 6, 7}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. Dictionary"
      ],
      "metadata": {
        "id": "NT9IM_31CS1k"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dict1={1:\"ak\",2:\"pk\",3:\"dk\",5:\"sk\"}\n",
        "print(dict1[2])\n",
        "for i in dict1:\n",
        "  print(\"elements in dict1 at key:\",i,\"value:\",dict1[i])\n",
        "\n",
        "#dictonary operations\n",
        "print(\"print all keys:\",dict1.keys())\n",
        "print(\"print all values:\",dict1.values())\n",
        "\n",
        "dict1[1]=\"bk\"\n",
        "print(\"after update:\",dict1)\n",
        "\n",
        "del dict1[5]\n",
        "print(\"after delete:\",dict1)\n",
        "\n",
        "dict1.pop(1)\n",
        "print(\"after pop:\",dict1)\n",
        "\n",
        "print(\"get value of key 2:\",dict1.get(2))\n",
        "\n",
        "dict1.clear()\n",
        "print(\"after clear:\",dict1)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ctsNlPDeCVrY",
        "outputId": "43d246f9-68e9-43d2-99d3-7db21c18c43a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "pk\n",
            "elements in dict1 at key: 1 value: ak\n",
            "elements in dict1 at key: 2 value: pk\n",
            "elements in dict1 at key: 3 value: dk\n",
            "elements in dict1 at key: 5 value: sk\n",
            "print all keys: dict_keys([1, 2, 3, 5])\n",
            "print all values: dict_values(['ak', 'pk', 'dk', 'sk'])\n",
            "after update: {1: 'bk', 2: 'pk', 3: 'dk', 5: 'sk'}\n",
            "after delete: {1: 'bk', 2: 'pk', 3: 'dk'}\n",
            "after pop: {2: 'pk', 3: 'dk'}\n",
            "get value of key 2: pk\n",
            "after clear: {}\n"
          ]
        }
      ]
    }
  ]
}
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mzO7eURbt474"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "frozenset in list"
      ],
      "metadata": {
        "id": "a1TA5mtrxHL_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "l = [\"Akshata\", \"Rgit\", \"Akshata\"]\n",
        "\n",
        "# converting tuple to frozenset\n",
        "fnum = frozenset(l)\n",
        "\n",
        "# printing empty frozenset object\n",
        "print(\"frozenset Object is : \", fnum)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e8S9TRdzxbtv",
        "outputId": "caf6c946-fd1b-4bae-da19-0471f9a02c42"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "frozenset Object is :  frozenset({'Rgit', 'Akshata'})\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "frozenset in dictonery"
      ],
      "metadata": {
        "id": "0BroLUO4ymgT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# creating a dictionary\n",
        "Student = {\"name\": \"Akshata\", \"age\": 20, \"sex\": \"female\",\n",
        "\t\t\"college\": \"RGIT\", \"address\": \"virar\"}\n",
        "\n",
        "# making keys of dictionary as frozenset\n",
        "key = frozenset(Student)\n",
        "\n",
        "# printing dict keys as frozenset\n",
        "print('The frozen set is:', key)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pFy6dB86yqBC",
        "outputId": "b47c1598-5754-42b0-9699-a1511562b4e1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The frozen set is: frozenset({'age', 'college', 'address', 'sex', 'name'})\n"
          ]
        }
      ]
    }
  ]
}
