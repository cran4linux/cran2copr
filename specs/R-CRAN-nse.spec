%global __brp_check_rpaths %{nil}
%global packname  nse
%global packver   1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.20
Release:          1%{?dist}%{?buildtag}
Summary:          Numerical Standard Errors Computation in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mcmc 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mcmc 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-np 
Requires:         R-CRAN-sandwich 

%description
Collection of functions designed to calculate numerical standard error
(NSE) of univariate time series as described in Ardia et al. (2018)
<doi:10.1515/jtse-2017-0011> and Ardia and Bluteau (2017)
<doi:10.21105/joss.00172>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
