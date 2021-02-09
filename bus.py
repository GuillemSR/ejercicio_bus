{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "test3.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMbMlRkanGpdx0p6EXBl06x",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/GuillemSR/ejercicio_bus/blob/master/bus.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "66c4pK21Kf4t",
        "outputId": "e7f0bbd6-c1f7-44a9-e5d1-34d6e42311dc"
      },
      "source": [
        "!git clone https://github.com/GuillemSR/ejercicio_bus.git"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cloning into 'ejercicio_bus'...\n",
            "remote: Enumerating objects: 8, done.\u001b[K\n",
            "remote: Counting objects: 100% (8/8), done.\u001b[K\n",
            "remote: Compressing objects: 100% (6/6), done.\u001b[K\n",
            "remote: Total 8 (delta 0), reused 4 (delta 0), pack-reused 0\u001b[K\n",
            "Unpacking objects: 100% (8/8), done.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PYX9NGTKKlh7",
        "outputId": "09d4e987-e31d-4624-bc0c-4b0961a045aa"
      },
      "source": [
        "# class Billete:\r\n",
        "#   def __init__(self, name):\r\n",
        "#     self.name = name\r\n",
        "#   def x(self):\r\n",
        "#     print('Hola')\r\n",
        "\r\n",
        "  \r\n",
        "# bill = Billete('Juan')\r\n",
        "# l = []\r\n",
        "# l.append(bill)\r\n",
        "# l[0].x()\r\n",
        "\r\n",
        "# ids = []\r\n",
        "    # if id not in ids:\r\n",
        "    #   self.id = id\r\n",
        "    #   ids.append(id)\r\n",
        "    # else:\r\n",
        "    #   print('Este bus ya existe')\r\n",
        "\r\n",
        "\r\n",
        "class Bus:\r\n",
        "\r\n",
        "  def __init__(self, id, plazas):\r\n",
        "    self.plazas = plazas\r\n",
        "    self.billetes = [None]*self.plazas\r\n",
        "\r\n",
        "  def venta(self, name, cnt):\r\n",
        "    contador = 0\r\n",
        "    if self.billetes.count(None) <= cnt:\r\n",
        "      while contador < cnt:\r\n",
        "        for i, billete in enumerate(self.billetes):\r\n",
        "          if billete is None:\r\n",
        "            self.billetes[i] = Billete(name)\r\n",
        "            contador += 1\r\n",
        "    else:\r\n",
        "      print('La venta no es posible')\r\n",
        "\r\n",
        "  def vuelta(self, canti, name):\r\n",
        "    list_names = []\r\n",
        "    for i in range(len(self.billetes)):\r\n",
        "      old = self.billetes[i].GetName()\r\n",
        "      if old == name:\r\n",
        "        list_names.append(i)\r\n",
        "    if len(list_names) >= canti:\r\n",
        "      for i in canti:\r\n",
        "        self.billetes[list_names[i]] = None\r\n",
        "    else:\r\n",
        "      print('La devolucion no es posible')\r\n",
        "\r\n",
        "    \r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "    \r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "    \r\n",
        "\r\n",
        "\r\n",
        "  def total(self):\r\n",
        "\r\n",
        "\r\n",
        "\r\n"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}