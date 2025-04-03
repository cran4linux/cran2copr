%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ieTest
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Indirect Effects Testing Methods in Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
BuildRequires:    R-CRAN-twosamples 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppDist 
Requires:         R-CRAN-twosamples 
Requires:         R-CRAN-MASS 

%description
Used in testing if the indirect effect from linear regression mediation
analysis is equal to 0. Includes established methods such as the Sobel
Test, Joint Significant test (maxP), and tests based off the distribution
of the Product or Normal Random Variables. Additionally, this package adds
more powerful tests based on Intersection-Union theory. These tests are
the S-Test, the ps-test, and the ascending squares test. These new methods
are uniformly more powerful than maxP, which is more powerful than Sobel
and less anti-conservative than the Product of Normal Random Variables.
These methods are explored by Kidd and Lin, (2024)
<doi:10.1007/s12561-023-09386-6> and Kidd et al., (2025)
<doi:10.1007/s10260-024-00777-7>.

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
