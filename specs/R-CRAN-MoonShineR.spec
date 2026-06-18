%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MoonShineR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Moonlight, Sunlight, and/or Twilight Ground Illuminance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-suncalc 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-REdaS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-suncalc 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-REdaS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-progress 

%description
Predicts ground-level illuminance from moonlight, sunlight, and twilight
for specified locations and time periods. The package is intended for
field studies in ecology and behavior where natural light levels are used
as predictor variables. See Poon et al. (2024)
<doi:10.1111/2041-210X.14299>. Calculations use astronomical quantities
from 'suncalc' and published illuminance models, including Austin et al.
(1976) <doi:10.2307/2402251> and Seidelmann (1992) <ISBN:0935702687>.

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
