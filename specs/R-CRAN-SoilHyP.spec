%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SoilHyP
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Soil Hydraulic Properties

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-data.table >= 1.13
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-data.table >= 1.13

%description
Provides functions for (1) soil water retention (SWC) and unsaturated
hydraulic conductivity (Ku) (van Genuchten-Mualem (vGM or vG) [1, 2],
Peters-Durner-Iden (PDI) [3, 4, 5], Brooks and Corey (bc) [8]), (2)
fitting of parameter for SWC and/or Ku using Shuffled Complex Evolution
(SCE) optimisation and (3) calculation of soil hydraulic properties (Ku
and soil water contents) based on the simplified evaporation method (SEM)
[6, 7]. Main references: [1] van Genuchten (1980)
<doi:10.2136/sssaj1980.03615995004400050002x>, [2] Mualem (1976)
<doi:10.1029/WR012i003p00513>, [3] Peters (2013) <doi:10.1002/wrcr.20548>,
[4] Iden and Durner (2013) <doi:10.1002/2014WR015937>, [5] Peters (2014)
<doi:10.1002/2014WR015937>, [6] Wind G. P. (1966), [7] Peters and Durner
(2008) <doi:10.1016/j.jhydrol.2008.04.016> and [8] Brooks and Corey
(1964).

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
