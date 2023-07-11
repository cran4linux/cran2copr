%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixvlmc
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Length Markov Chains with Covariates

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-butcher 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-butcher 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-withr 

%description
Estimates Variable Length Markov Chains (VLMC) models and VLMC with
covariates models from discrete sequences. Supports model selection via
information criteria and simulation of new sequences from an estimated
model. See Bühlmann, P. and Wyner, A. J. (1999)
<doi:10.1214/aos/1018031204> for VLMC and Zanin Zambom, A., Kim, S. and
Lopes Garcia, N. (2022) <doi:10.1111/jtsa.12615> for VLMC with covariates.

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
