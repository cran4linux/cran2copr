%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VectorCodeR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Analyze Your Gait Patterns Using Vector Coding Technique

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tidyverse 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 

%description
Facilitate the analysis of inter-limb and intra-limb coordination in human
movement. It provides functions for calculating the phase angle between
two segments, enabling researchers and practitioners to quantify the
coordination patterns within and between limbs during various motor tasks.
Needham, R., Naemi, R., & Chockalingam, N. (2014)
<doi:10.1016/j.jbiomech.2013.12.032>. Needham, R., Naemi, R., &
Chockalingam, N. (2015) <doi:10.1016/j.jbiomech.2015.07.023>. Tepavac, D.,
& Field-Fote, E. C. (2001) <doi:10.1123/jab.17.3.259>.

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
