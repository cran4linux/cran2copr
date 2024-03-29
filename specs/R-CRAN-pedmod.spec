%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pedmod
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Pedigree Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-psqn 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-alabama 

%description
Provides functions to estimate mixed probit models using, for instance,
pedigree data like in <doi:10.1002/sim.1603>. The models are also commonly
called liability threshold models. The approximation is based on direct
log marginal likelihood approximations like the randomized Quasi-Monte
Carlo suggested by <doi:10.1198/106186002394> with a similar procedure to
approximate the derivatives. The minimax tilting method suggested by
<doi:10.1111/rssb.12162> is also supported. Graph-based methods are also
provided that can be used to simplify pedigrees.

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
