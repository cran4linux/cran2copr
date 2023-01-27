%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ldt
%global packver   0.1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Let Data Talk

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-jsonlite 

%description
Methods and tools for creating a model set and estimating and evaluating
the explanation or prediction power of its members. 'SUR' modelling (for
parameter estimation), 'logit'/'probit' modelling (for binary
classification), and 'VARMA' modelling (for time-series forecasting) are
implemented. Evaluations are both in-sample and out-of-sample. It can be
used for stepwise regression analysis
<https://en.wikipedia.org/wiki/Stepwise_regression>, automatic model
selection and model averaging (Claeskens and Hjort (2008, ISBN:1139471805,
9781139471800)), calculating benchmarks, and doing sensitivity analysis
(Leamer (1983) <https://www.jstor.org/stable/1803924> proposal).

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
