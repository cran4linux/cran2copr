%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SANvi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Shared Atoms Nested Models via Variational Bayes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixStats 

%description
An efficient tool for fitting the nested common and shared atoms models
using variational Bayes approximate inference for fast computation.
Specifically, the package implements the common atoms model (Denti et al.,
2023), its finite version (D'Angelo et al., 2023), and a hybrid
finite-infinite model. All models use Gaussian mixtures with a
normal-inverse-gamma prior distribution on the parameters. Additional
functions are provided to help analyze the results of the fitting
procedure. References: Denti, Camerlenghi, Guindani, Mira (2023)
<doi:10.1080/01621459.2021.1933499>, D’Angelo, Canale, Yu, Guindani (2023)
<doi:10.1111/biom.13626>.

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
