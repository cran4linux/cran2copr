%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rainerosr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Rainfall Intensity and Erosivity Indices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-lubridate >= 1.9.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-lubridate >= 1.9.0
Requires:         R-CRAN-dplyr >= 1.1.0

%description
Calculates I30 (maximum 30-minute rainfall intensity) and EI30 (erosivity
index) from rainfall breakpoint data. Supports multiple storm events,
rainfall validation, and visualization for soil erosion modeling and
hydrological analysis. Methods are based on Brown and Foster (1987)
<doi:10.13031/2013.30422>, Wischmeier and Smith (1978) "Predicting
Rainfall Erosion Losses: A Guide to Conservation Planning"
<doi:10.22004/ag.econ.171903>, and Renard et al. (1997) "Predicting Soil
Erosion by Water: A Guide to Conservation Planning with the Revised
Universal Soil Loss Equation (RUSLE)" (USDA Agriculture Handbook No. 703).

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
