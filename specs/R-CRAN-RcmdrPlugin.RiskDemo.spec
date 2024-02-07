%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcmdrPlugin.RiskDemo
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plug-in for Risk Demonstration

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr 
BuildRequires:    R-CRAN-demography 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ftsa 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Rcmdr 
Requires:         R-CRAN-demography 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ftsa 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 

%description
R Commander plug-in to demonstrate various actuarial and financial risks.
It includes valuation of bonds and stocks, portfolio optimization,
classical ruin theory, demography and epidemic.

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
