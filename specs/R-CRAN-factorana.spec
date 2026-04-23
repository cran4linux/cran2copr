%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  factorana
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Factor Model Estimation with Latent Variables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
A flexible framework for estimating factor models with multiple latent
variables. Supports linear, probit, ordered probit, and multinomial logit
model components. Features include multi-stage estimation, automatic
parameter initialization, analytical gradients and Hessians, and parallel
estimation. Methods are described in Heckman, Humphries, and Veramendi
(2016) <doi:10.1016/j.jeconom.2015.12.001>, Heckman, Humphries, and
Veramendi (2018) <doi:10.1086/698760>, and Humphries, Joensen, and
Veramendi (2024) <doi:10.1257/pandp.20241026>.

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
