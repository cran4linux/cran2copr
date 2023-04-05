%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  publipha
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Meta-Analysis with Publications Bias and P-Hacking

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-rstan >= 2.21.8
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0.7
BuildRequires:    R-CRAN-BH >= 1.72.0.2
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.21.8
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-methods 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-rstantools

%description
Tools for Bayesian estimation of meta-analysis models that account for
publications bias or p-hacking. For publication bias, this package
implements a variant of the p-value based selection model of Hedges (1992)
<doi:10.1214/ss/1177011364> with discrete selection probabilities. It also
implements the mixture of truncated normals model for p-hacking described
in Moss and De Bin (2019) <arXiv:1911.12445>.

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
