%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SIS
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Sure Independence Screening

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-gcdnet 
BuildRequires:    R-CRAN-msaenet 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-gcdnet 
Requires:         R-CRAN-msaenet 
Requires:         R-CRAN-foreach 
Requires:         R-methods 

%description
Variable selection techniques are essential tools for model selection and
estimation in high-dimensional statistical models. Through this publicly
available package, we provide a unified environment to carry out variable
selection using iterative sure independence screening (SIS) (Fan and Lv
(2008)<doi:10.1111/j.1467-9868.2008.00674.x>) and all of its variants in
generalized linear models (Fan and Song (2009)<doi:10.1214/10-AOS798>) and
the Cox proportional hazards model (Fan, Feng and Wu
(2010)<doi:10.1214/10-IMSCOLL606>).

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
