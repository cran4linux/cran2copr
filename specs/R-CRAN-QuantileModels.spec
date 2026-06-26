%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuantileModels
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Different Quantile Related Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ufRisk 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ufRisk 
Requires:         R-CRAN-GenSA 

%description
Estimation of different quantile models, at the moment only Conditional
autoregressive value at risk (CAViaR) proposed by Engle & Manganelli
(2004) <doi:10.1198/073500104000000370> with also the specification
proposed in Huang et al. (2009) <doi:10.1016/j.eneco.2008.12.006> and it's
multivariate extension, Multi-variate multi-quantile CAViaR (MVMQ-CAViaR)
proposed by White et al. (2015) <doi:10.1016/j.jeconom.2015.02.004> are
available, however, in further updates, other models and extensions will
be included.

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
