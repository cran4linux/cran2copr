%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  saeczi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Small Area Estimation for Continuous Zero Inflated Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rcpp 

%description
Simplifies the process of fitting a zero-inflated estimator onto a
dataset. This estimator is a combination of a linear mixed effects
regression model and a logistic mixed effects regression model which is
summarized by White and others (2024, <arXiv:2402.03263>). The variance is
estimated through a parametric bootstrapping method which is given by
Chandra and others (2012, <doi:10.1080/03610918.2011.598991>).

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
