%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WaverideR
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extracting Signals from Wavelet Spectra

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-colorednoise 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-astrochron 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-trapezoid 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-DecomposeR 
BuildRequires:    R-CRAN-doSNOW 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-Matrix 
Requires:         R-utils 
Requires:         R-CRAN-colorednoise 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-truncnorm 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-astrochron 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-trapezoid 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-DecomposeR 
Requires:         R-CRAN-doSNOW 

%description
The continuous wavelet transform enables the observation of
transient/non-stationary cyclicity in time-series. The goal of
cyclostratigraphic studies is to define frequency/period in the depth/time
domain. By conducting the continuous wavelet transform on
cyclostratigraphic data series one can observe and extract cyclic
signals/signatures from signals. These results can then be visualized and
interpreted enabling one to identify/interpret cyclicity in the geological
record, which can be used to construct astrochronological age-models and
identify and interpret cyclicity in past and present climate systems. The
'WaverideR' R package builds upon existing literature and existing
codebase. The list of articles which are relevant can be grouped in four
subjects; cyclostratigraphic data analysis,example data sets,the
(continuous) wavelet transform and astronomical solutions. References for
the cyclostratigraphic data analysis articles are: Stephen Meyers (2019)
<doi:10.1016/j.earscirev.2018.11.015>. Mingsong Li, Linda Hinnov, Lee Kump
(2019) <doi:10.1016/j.cageo.2019.02.011> Stephen Meyers
(2012)<doi:10.1029/2012PA002307> Mingsong Li, Lee R. Kump, Linda A.
Hinnov, Michael E. Mann (2018) <doi:10.1016/j.epsl.2018.08.041>. Wouters,
S., Crucifix, M., Sinnesael, M., Da Silva, A.C., Zeeden, C., Zivanovic,
M., Boulvain, F., Devleeschouwer, X. (2022)
<doi:10.1016/j.earscirev.2021.103894>. Wouters, S., Da Silva, A.-C.,
Boulvain, F., and Devleeschouwer, X. (2021) <doi:10.32614/RJ-2021-039>.
Huang, Norden E., Zhaohua Wu, Steven R. Long, Kenneth C. Arnold, Xianyao
Chen, and Karin Blank (2009) <doi:10.1142/S1793536909000096>. Cleveland,
W. S. (1979)<doi:10.1080/01621459.1979.10481038> Hurvich, C.M., Simonoff,
J.S., and Tsai, C.L. (1998) <doi:10.1111/1467-9868.00125>, Golub, G.,
Heath, M. and Wahba, G. (1979) <doi:10.2307/1268518>. References for the
example data articles are: Damien Pas, Linda Hinnov, James E. (Jed) Day,
Kenneth Kodama, Matthias Sinnesael, Wei Liu (2018)
<doi:10.1016/j.epsl.2018.02.010>. Steinhilber, Friedhelm, Abreu, Jacksiel,
Beer, Juerg , Brunner, Irene, Christl, Marcus, Fischer, Hubertus,
HeikkilA, U., Kubik, Peter, Mann, Mathias, Mccracken, K. , Miller,
Heinrich, Miyahara, Hiroko, Oerter, Hans , Wilhelms, Frank. (2012
<doi:10.1073/pnas.1118965109>. Christian Zeeden, Frederik Hilgen, Thomas
Westerhold, Lucas Lourens, Ursula Röhl, Torsten Bickert (2013)
<doi:10.1016/j.palaeo.2012.11.009>. References for the (continuous)
wavelet transform articles are: Morlet, Jean, Georges Arens, Eliane
Fourgeau, and Dominique Glard (1982a) <doi:10.1190/1.1441328>. J. Morlet,
G. Arens, E. Fourgeau, D. Giard (1982b) <doi:10.1190/1.1441329>. Torrence,
C., and G. P. Compo
(1998)<https://paos.colorado.edu/research/wavelets/bams_79_01_0061.pdf>,
Gouhier TC, Grinsted A, Simko V (2021)
<https://github.com/tgouhier/biwavelet>. Angi Roesch and Harald
Schmidbauer (2018) <https://CRAN.R-project.org/package=WaveletComp>.
Russell, Brian, and Jiajun Han
(2016)<https://www.crewes.org/Documents/ResearchReports/2016/CRR201668.pdf>.
Gabor, Dennis (1946) <http://genesis.eecg.toronto.edu/gabor1946.pdf>. J.
Laskar, P. Robutel, F. Joutel, M. Gastineau, A.C.M. Correia, and B.
Levrard, B. (2004) <doi:10.1051/0004-6361:20041335>. Laskar, J., Fienga,
A., Gastineau, M., Manche, H. (2011a) <doi:10.1051/0004-6361/201116836>.
References for the astronomical solutions articles are: Laskar, J.,
Gastineau, M., Delisle, J.-B., Farres, A., Fienga, A. (2011b
<doi:10.1051/0004-6361/201117504>. J. Laskar (2019)
<doi:10.1016/B978-0-12-824360-2.00004-8>. Zeebe, Richard E (2017)
<doi:10.3847/1538-3881/aa8cce>. Zeebe, R. E. and Lourens, L. J. (2019)
<doi:10.1016/j.epsl.2022.117595>. Richard E. Zeebe Lucas J. Lourens (2022)
<doi:10.1126/science.aax0612>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
