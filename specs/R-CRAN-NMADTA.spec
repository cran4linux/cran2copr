%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NMADTA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Network Meta-Analysis of Multiple Diagnostic Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plotrix 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-Rdpack 

%description
Implements HSROC (hierarchical summary receiver operating characteristic)
model developed by Ma, Lian, Chu, Ibrahim, and Chen (2018)
<doi:10.1093/biostatistics/kxx025> and hierarchical model developed by
Lian, Hodges, and Chu (2019) <doi:10.1080/01621459.2018.1476239> for
performing meta-analysis for 1-5 diagnostic tests to simultaneously
compare multiple tests within a missing data framework. This package
evaluates the accuracy of multiple diagnostic tests and also gives
graphical representation of the results.

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
