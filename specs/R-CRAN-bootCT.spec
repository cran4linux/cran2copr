%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bootCT
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrapping the ARDL Tests for Cointegration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-ARDL 
BuildRequires:    R-CRAN-dynamac 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-ARDL 
Requires:         R-CRAN-dynamac 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-usethis 

%description
The bootstrap ARDL tests for cointegration is the main functionality of
this package. It also acts as a wrapper of the most commond ARDL testing
procedures for cointegration: the bound tests of Pesaran, Shin and Smith
(PSS; 2001 - <doi:10.1002/jae.616>) and the asymptotic test on the
independent variables of Sam, McNown and Goh (SMG: 2019 -
<doi:10.1016/j.econmod.2018.11.001>). Bootstrap and bound tests are
performed under both the conditional and unconditional ARDL models.

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
