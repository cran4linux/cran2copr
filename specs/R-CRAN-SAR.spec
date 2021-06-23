%global __brp_check_rpaths %{nil}
%global packname  SAR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Smart Adaptive Recommendations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-Rcpp >= 0.12
BuildRequires:    R-CRAN-AzureRMR 
BuildRequires:    R-CRAN-AzureStor 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-Rcpp >= 0.12
Requires:         R-CRAN-AzureRMR 
Requires:         R-CRAN-AzureStor 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-R6 
Requires:         R-parallel 
Requires:         R-CRAN-RcppParallel 

%description
'Smart Adaptive Recommendations' (SAR) is the name of a fast, scalable,
adaptive algorithm for personalized recommendations based on user
transactions and item descriptions. It produces easily
explainable/interpretable recommendations and handles "cold item" and
"semi-cold user" scenarios. This package provides two implementations of
'SAR': a standalone implementation, and an interface to a web service in
Microsoft's 'Azure' cloud:
<https://github.com/Microsoft/Product-Recommendations/blob/master/doc/sar.md>.
The former allows fast and easy experimentation, and the latter provides
robust scalability and extra features for production use.

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
