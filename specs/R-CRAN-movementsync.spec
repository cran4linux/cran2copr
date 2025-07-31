%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  movementsync
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Visualisation of Musical Audio and Video Movement Synchrony Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-osfr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-WaveletComp 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lmtest 
Requires:         R-methods 
Requires:         R-CRAN-osfr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-WaveletComp 
Requires:         R-CRAN-zoo 

%description
Analysis and visualisation of synchrony, interaction, and joint movements
from audio and video movement data of a group of music performers. The
demo is data described in Clayton, Leante, and Tarsitani (2021)
<doi:10.17605/OSF.IO/KS325>, while example analyses can be found in
Clayton, Jakubowski, and Eerola (2019) <doi:10.1177/1029864919844809>.
Additionally, wavelet analysis techniques have been applied to examine
movement-related musical interactions, as shown in Eerola et al. (2018)
<doi:10.1098/rsos.171520>.

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
