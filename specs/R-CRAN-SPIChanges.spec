%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SPIChanges
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Improves the Interpretation of the Standardized Precipitation Index Under Changing Climate Conditions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-spsUtil 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-brglm2 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-spsUtil 
Requires:         R-stats 
Requires:         R-CRAN-brglm2 
Requires:         R-CRAN-zoo 

%description
Improves the interpretation of the Standardized Precipitation Index under
changing climate conditions. The package uses the nonstationary approach
proposed in Blain et al. (2022) <doi:10.1002/joc.7550> to detect trends in
rainfall quantities and to quantify the effect of such trends on the
probability of a drought event occurring.

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
