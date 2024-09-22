%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  profoc
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Forecast Combination Using CRPS Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-rcpptimer >= 1.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-splines2 >= 0.4.4
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.7.5.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 

%description
Combine probabilistic forecasts using CRPS learning algorithms proposed in
Berrisch, Ziel (2021) <doi:10.48550/arXiv.2102.00968>
<doi:10.1016/j.jeconom.2021.11.008>. The package implements multiple
online learning algorithms like Bernstein online aggregation; see
Wintenberger (2014) <doi:10.48550/arXiv.1404.1356>. Quantile regression is
also implemented for comparison purposes. Model parameters can be tuned
automatically with respect to the loss of the forecast combination.
Methods like predict(), update(), plot() and print() are available for
convenience. This package utilizes the optim C++ library for numeric
optimization <https://github.com/kthohr/optim>.

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
