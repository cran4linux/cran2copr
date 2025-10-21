%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stratEst
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Strategy Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.900.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-stats 
Requires:         R-graphics 

%description
Variants of strategy estimation (Dal Bo & Frechette, 2011,
<doi:10.1257/aer.101.1.411>), including the model with parameters for the
choice probabilities of the strategies (Breitmoser, 2015,
<doi:10.1257/aer.20130675>), and the model with individual level
covariates for the selection of strategies by individuals (Dvorak &
Fehrler, 2018, <doi:10.2139/ssrn.2986445>).

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
