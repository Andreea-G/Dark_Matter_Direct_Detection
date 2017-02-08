"""
Copyright (c) 2015 Andreea Georgescu

Created on Tue Apr  7 17:25:46 2015

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import
from __future__ import division
import numpy as np
from scipy.interpolate import interp1d
pi = np.pi

name = "XENON100"
modulated = False

energy_resolution_type = "Poisson"
#energy_resolution_type = "Gaussian"

def EnergyResolution(e):
    return 0.5 * np.ones_like(e)
#    return np.ones_like(e)

FFSD = 'GaussianFFSD'
FFSI = 'HelmFF'
FF = {'SI': FFSI,
      'SDPS': FFSD,
      'SDAV': FFSD,
      }

target_nuclide_AZC_list = \
    np.array([[124, 54, 0.0008966], [126, 54, 0.0008535], [128, 54, 0.018607],
              [129, 54, 0.25920], [130, 54, 0.040280], [131, 54, 0.21170],
              [132, 54, 0.27035], [134, 54, 0.10644], [136, 54, 0.09168]])
target_nuclide_JSpSn_list = \
    np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0],
              [1./2, 0.010 * np.sqrt(3./2 / pi), .329 * np.sqrt(3./2 / pi)], [0, 0, 0],
              [3./2, -0.009 * np.sqrt(5./2 / pi), -.272 * np.sqrt(5./2 / pi)],
              [0, 0, 0], [0, 0, 0], [0, 0, 0]])
target_nuclide_mass_list = np.array([115.418, 117.279, 119.141, 120.074, 121.004,
                                     121.937, 122.868, 124.732, 126.597])
num_target_nuclides = target_nuclide_mass_list.size

x = np.array([0., 0.395837, 0.431065, 0.451241, 0.473339, 0.582546, 0.7747, 0.995997,
              1.09303, 1.18078, 1.30024, 1.41681, 1.4783, 1.6948, 1.76781, 1.9004,
              2.01954, 2.14444, 2.23187 ])
y = np.array([0., 0.0745321, 0.0792141, 0.0831369, 0.0941459, 0.0999667, 0.116417,
              0.144003, 0.147293, 0.154252, 0.159694, 0.169311, 0.17665, 0.191076,
              0.194872, 0.198035, 0.197403, 0.2, 0.2])

QuenchingFactor_interp = interp1d(x, y)

def QuenchingFactor(e_list):
    # Absolutely no clue what this is...
    Ly = 2.28
    Snr = 0.95
    See = 0.58
    try:
        len(e_list)
    except TypeError:
        e_list = [e_list]
    q = np.array([0. if e < 1 \
                  else  QuenchingFactor_interp(np.log10(e)) if e < 10**2.23187 \
                  else 0.2
                  for e in e_list])
    return Ly * Snr / See * q


Ethreshold = 3
Emaximum = 30
ERmaximum = 30.

x = np.array([2.97005128, 2.97105641, 3.54297436, 4.14605128, 5.02051282, 5.96533333,
              6.71917949, 7.54338462, 8.40779487, 9.09128205, 9.9054359 , 10.83015385,
              11.75487179, 13.2625641, 15.27282051, 18.26810256, 20.68041026, 24.39938462,
              50.])
y = np.array([0., 0.91225403, 0.92039356, 0.92790698, 0.93729875, 0.94794275,
              0.95420394, 0.96109123, 0.96797853, 0.97330054, 0.9773703, 0.98175313,
              0.98488372, 0.98864043, 0.99177102, 0.99490161, 0.99740608, 1., 1.])
Efficiency_interp = interp1d(x, y, kind='linear', bounds_error=False, fill_value=0.)

def Efficiency(e):
    return 0. if e < Ethreshold else Efficiency_interp(e) if e < Emaximum else 1.

x = np.array([0.45873015388911353, 0.79316185645953996, 1.1047296966584195,
              1.3339624100643037, 1.5788937330123782, 1.8395236655026428,
              2.11846261362495, 2.4176732628301867, 2.733790809700237, 3.0591810343745269,
              3.3668383101962784, 3.6856409633686673, 4.0157335336200459, 4.36013287450145,
              4.7160548854819346, 5.068284380849537, 5.3752218745180862, 5.6867234768752404,
              6.0027273139948027, 6.315978602730234, 6.6331656861279313, 6.9542885641878982,
              7.2806666750698437, 7.6113056697975887, 7.9459965299245168, 8.2642583411746262,
              8.5811421338246934, 8.9004230893443221, 9.2310291754597742, 9.5687236360144983,
              9.9096124567931945, 10.247157132999988, 10.585121195345602, 10.925779087105665,
              11.263232923201789, 11.601398672758791, 11.941866817431467, 12.298606540357159,
              12.661253862553222, 13.026420408803665, 13.387011658133231, 13.750345017371975,
              14.116837128282128, 14.487005380132757, 14.859972261059944, 15.236853390803718,
              15.617256837830194, 16.000533954032001, 16.388937555597099, 16.780297856854304,
              17.175812181713805, 17.575867061630351, 17.978978111340922, 18.388210068907725,
              18.800775668167184, 19.20192365642944, 19.592050316037895, 19.984402111527807,
              20.355710628687937, 20.727523677796597, 21.10220097102351, 21.482263207974235,
              21.863937733048484, 22.238731593061619, 22.610132582697098, 22.982755304390349,
              23.381030023425701, 23.782419887341085, 24.178961702154695, 24.569174246952645,
              24.960927617389938, 25.359855432956063, 25.761104236792402, 26.158285929219527,
              26.548491215842752, 26.940036576765863, 27.330076644790548, 27.720866334997794,
              28.114903840747406, 28.515236420501825, 28.916993446597463, 29.309379083410001,
              29.700099953644887, 30.096124660451906])
y = np.array([4.5716130497434311e-05, 0.052970474143870218, 0.0992277655385298,
              0.14545640475276153, 0.18409119848103203, 0.21538389389828494,
              0.24243309617309067, 0.26696382719072514, 0.29068062952239782,
              0.30688153631739323, 0.32083478457434889, 0.33372924164897683,
              0.3420772002158034, 0.3493623794514587, 0.35215034898195652,
              0.35558585970880063, 0.35734012238318341, 0.35759742129414634,
              0.35661852706294861, 0.35417826111743872, 0.35181076645901505,
              0.34825286604189565, 0.34452810728043748, 0.34117170619945236,
              0.33862897949282489, 0.3358178475826521, 0.33090706449584739,
              0.32699585578957147, 0.32310877975940155, 0.31912657466973376,
              0.31505921055569114, 0.31116078898500749, 0.30720800155483052,
              0.30284832932772071, 0.29948970590613566, 0.29614297168952225,
              0.29260746304894419, 0.28875944830293648, 0.28487601935955786,
              0.28093145361003991, 0.27719150073916771, 0.27343150504161029,
              0.26977337017840242, 0.26698332191755486, 0.26414862979588138,
              0.26130178422517364, 0.2584041292364665, 0.25450723337428421,
              0.2505340262295459, 0.24655184174613295, 0.24254204907134402,
              0.23807980903102405, 0.23362622611428574, 0.22916197345990266,
              0.22468716519411966, 0.22020184969273002, 0.21570340762983239,
              0.21128334737948765, 0.20692854144489092, 0.20256355799255335,
              0.19821829021133827, 0.19368706839752711, 0.18907777435867026,
              0.18445210837604167, 0.18038848872660862, 0.17661647043162032,
              0.17279654362081981, 0.16892023022803374, 0.16503426622806205,
              0.16113865162090468, 0.15855735804474885, 0.15649985228734214,
              0.15459788323694762, 0.153797971449464, 0.15309376199857713,
              0.1554166657743882, 0.15810372102057421, 0.16314603797178423,
              0.16858735610788259, 0.17577842336975949, 0.18430146286315846,
              0.19450738576869805, 0.20680835396890743, 0.22319940077087433])
Efficiency_ER_interp = interp1d(x, y, kind='linear', bounds_error=False, fill_value=0.)

def Efficiency_ER(er):
    try:
        len(er)
    except TypeError:
        er = [er]
    return np.array([1. if e >= 1.4 else 0. for e in er])
            #return np.array([0. if e < 0.4588
            #        else Efficiency_ER_interp(e) if e < 30.095
            #         else 0.2232
            #         for e in er])
    # TODO! Check the 0.2232 value!


Exposure = 224.56 * 34.0
ERecoilList = np.array([3.22, 3.68])
