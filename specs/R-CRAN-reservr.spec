%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reservr
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Distributions and Neural Networks to Censored and Truncated Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-keras >= 2.2.5.0
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-keras >= 2.2.5.0
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-generics 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Define distribution families and fit them to interval-censored and
interval-truncated data, where the truncation bounds may depend on the
individual observation. The defined distributions feature density,
probability, sampling and fitting methods as well as efficient
implementations of the log-density log f(x) and log-probability log P(x0
<= X <= x1) for use in 'TensorFlow' neural networks via the 'tensorflow'
package. Allows training parametric neural networks on interval-censored
and interval-truncated data with flexible parameterization. Applications
include Claims Development in Non-Life Insurance, e.g. modelling reporting
delay distributions from incomplete data, see Bücher, Rosenstock (2022)
<doi:10.1007/s13385-022-00314-4>.

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
