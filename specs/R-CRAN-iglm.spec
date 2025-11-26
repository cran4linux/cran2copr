%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iglm
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression under Network Interference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-igraph 

%description
An implementation of generalized linear models (GLMs) for studying
relationships among attributes in connected populations, where responses
of connected units can be dependent, as introduced by Fritz et al. (2025)
<doi:10.1080/01621459.2025.2565851>. 'igml' extends GLMs for independent
responses to dependent responses and can be used for studying spillover in
connected populations and other network-mediated phenomena.

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
