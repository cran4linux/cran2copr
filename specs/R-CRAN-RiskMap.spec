%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RiskMap
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geostatistical Modeling of Spatially Referenced Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-spatialEco 
BuildRequires:    R-CRAN-spatialsample 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sns 
BuildRequires:    R-CRAN-stars 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-xtable 
Requires:         R-graphics 
Requires:         R-CRAN-spatialEco 
Requires:         R-CRAN-spatialsample 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sns 
Requires:         R-CRAN-stars 

%description
Geostatistical analysis of continuous and count data. Implements
stationary Gaussian processes with Matérn correlation for spatial
prediction, as described in Diggle and Giorgi (2019, ISBN:
978-1-138-06102-7).

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
