# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

DATA = {1: (0, 1, 0, 2), 2: (0, 1, 0, 1), 3: (0, 1, 0, 1), 4: (0, 1, 0, 1), 5: (0, 1, 0, 2), 6: (0, 0, 0, 1), 7: (0, 1, 0, 2), 8: (0, 0, 1, 2), 9: (1, 1, 0, 4), 10: (1, 1, 0, 4), 11: (0, 1, 0, 2), 12: (1, 1, 0, 4), 13: (0, 1, 0, 2), 14: (0, 1, 0, 2), 15: (0, 0, 1, 3), 16: (0, 0, 0, 1), 17: (0, 1, 0, 1), 18: (0, 1, 0, 1), 19: (0, 1, 0, 1), 20: (0, 0, 0, 1), 21: (0, 0, 0, 1), 22: (0, 1, 0, 1), 23: (0, 1, 0, 1), 24: (0, 1, 0, 2), 25: (0, 1, 0, 1), 26: (0, 1, 0, 2), 27: (0, 1, 0, 2), 28: (1, 1, 0, 3), 29: (0, 0, 0, 1), 30: (1, 1, 0, 4), 31: (1, 1, 0, 3), 32: (0, 1, 0, 2), 33: (0, 0, 0, 1), 34: (0, 1, 0, 2), 35: (1, 1, 0, 4), 36: (0, 1, 0, 1), 37: (1, 1, 0, 4), 38: (1, 1, 0, 4), 39: (0, 1, 0, 1), 40: (1, 1, 0, 4), 41: (1, 1, 0, 4), 42: (0, 1, 0, 1), 43: (1, 1, 0, 4), 44: (1, 1, 0, 4), 45: (0, 1, 0, 1), 46: (1, 1, 0, 4), 47: (1, 1, 0, 4), 48: (0, 1, 0, 2), 49: (0, 1, 0, 1), 50: (1, 1, 0, 4), 51: (0, 1, 0, 2), 52: (1, 1, 0, 4), 53: (0, 1, 0, 1), 54: (0, 1, 0, 1), 55: (0, 1, 0, 2), 56: (0, 1, 0, 2), 57: (1, 1, 1, 4), 58: (1, 1, 0, 4), 59: (0, 1, 0, 1), 60: (1, 1, 0, 4), 61: (1, 1, 0, 3), 62: (0, 1, 0, 2), 63: (1, 1, 0, 4), 64: (1, 1, 0, 3), 65: (0, 1, 0, 1), 66: (1, 1, 0, 3), 67: (0, 1, 0, 2), 68: (1, 1, 0, 4), 69: (0, 1, 0, 2), 70: (1, 1, 0, 4), 71: (1, 1, 0, 4), 72: (1, 1, 0, 3), 73: (0, 1, 0, 2), 74: (0, 1, 0, 3), 75: (0, 0, 0, 2), 76: (0, 1, 0, 2), 77: (1, 1, 0, 3), 78: (0, 1, 0, 2), 79: (0, 1, 0, 2), 80: (1, 1, 0, 3), 81: (0, 1, 0, 1), 82: (0, 0, 1, 2), 83: (0, 1, 0, 2), 84: (1, 1, 0, 3), 85: (0, 1, 0, 2), 86: (0, 1, 0, 2), 87: (0, 1, 0, 3), 88: (1, 1, 0, 4), 89: (1, 1, 0, 4), 90: (1, 1, 0, 4), 91: (1, 1, 0, 4), 92: (1, 1, 0, 4), 93: (0, 1, 0, 2), 94: (0, 1, 0, 2), 95: (0, 1, 0, 3), 96: (0, 1, 0, 1), 97: (0, 1, 0, 2), 98: (0, 1, 0, 2), 99: (1, 1, 0, 3), 100: (0, 0, 0, 2), 101: (1, 1, 0, 4), 102: (1, 1, 0, 4), 103: (0, 1, 0, 1), 104: (0, 1, 1, 3), 105: (1, 1, 0, 3), 106: (0, 1, 0, 3), 107: (0, 1, 0, 1), 108: (1, 1, 0, 3), 109: (1, 1, 0, 4), 110: (1, 1, 0, 3), 111: (1, 1, 0, 3), 112: (1, 1, 0, 4), 113: (1, 1, 0, 4), 114: (1, 1, 0, 4), 115: (0, 1, 0, 2), 116: (0, 0, 0, 1), 117: (1, 1, 0, 3), 118: (0, 1, 0, 2), 119: (0, 1, 0, 2), 120: (0, 1, 0, 2), 121: (0, 1, 0, 3), 122: (0, 1, 0, 1), 123: (0, 1, 0, 1), 124: (0, 1, 0, 2), 125: (0, 1, 0, 2), 126: (0, 1, 0, 2), 127: (0, 1, 0, 1), 128: (0, 1, 0, 1), 129: (1, 1, 0, 3), 130: (0, 1, 0, 2), 131: (1, 1, 0, 3), 132: (0, 1, 0, 2), 133: (0, 1, 0, 2), 134: (1, 0, 0, 3), 135: (0, 0, 1, 2), 136: (0, 1, 0, 2), 137: (0, 1, 0, 1), 138: (0, 1, 0, 2), 139: (0, 1, 0, 2), 140: (1, 1, 0, 4), 141: (1, 1, 0, 4), 142: (1, 1, 0, 4), 143: (0, 1, 0, 1), 144: (0, 1, 0, 1), 145: (1, 1, 0, 3), 146: (0, 0, 0, 2), 147: (0, 1, 0, 2), 148: (0, 1, 0, 2), 149: (1, 1, 0, 4), 150: (1, 1, 0, 4), 151: (1, 1, 0, 3), 152: (1, 1, 0, 4), 153: (1, 1, 0, 4), 154: (1, 1, 0, 4), 155: (0, 1, 0, 1), 156: (1, 1, 0, 4), 157: (0, 1, 0, 1), 158: (1, 1, 0, 4), 159: (0, 1, 0, 2), 160: (1, 1, 0, 3), 161: (0, 1, 0, 3), 162: (1, 1, 0, 3), 163: (1, 1, 0, 4), 164: (1, 1, 0, 3), 165: (0, 1, 0, 2), 166: (0, 1, 0, 3), 167: (1, 1, 0, 2), 168: (0, 1, 0, 2), 169: (0, 1, 0, 2), 170: (1, 1, 0, 4), 171: (0, 1, 0, 1), 172: (0, 1, 0, 1), 189: (0, 1, 0, 2), 190: (0, 1, 0, 2), 191: (0, 1, 0, 1), 192: (1, 1, 1, 3), 193: (0, 1, 0, 1)}

def set_new_parameters(apps, schema_editor):
    Mob = apps.get_model("mobs", "MobRecord")

    for mob in Mob.objects.all():
        if mob.id not in DATA:
            continue

        verbal, gestures, telepathic, intellect = DATA[mob.id]

        mob.communication_verbal = verbal
        mob.communication_gestures = gestures
        mob.communication_telepathic = telepathic

        mob.intellect_level = intellect

        mob.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mobs', '0004_remove_barbarians'),
    ]

    operations = [
        migrations.RunPython(
            set_new_parameters,
        ),
    ]
