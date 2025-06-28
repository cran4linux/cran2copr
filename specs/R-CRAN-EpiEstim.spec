%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiEstim
%global packver   2.2-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Time Varying Reproduction Numbers from Epidemic Curves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-incidence >= 1.7.0
BuildRequires:    R-CRAN-coarseDataTools >= 0.6.4
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-incidence >= 1.7.0
Requires:         R-CRAN-coarseDataTools >= 0.6.4
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 

%description
Tools to quantify transmissibility throughout an epidemic from the
analysis of time series of incidence as described in Cori et al. (2013)
<doi:10.1093/aje/kwt133> and Wallinga and Teunis (2004)
<doi:10.1093/aje/kwh255>.

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
