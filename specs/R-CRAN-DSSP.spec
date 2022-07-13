%global __brp_check_rpaths %{nil}
%global packname  DSSP
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of the Direct Sampling Spatial Prior

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-rust 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-rust 
Requires:         R-CRAN-sp 

%description
Draw samples from the direct sampling spatial prior model as described in
G. White, D. Sun, P. Speckman (2019) <arXiv:1906.05575>. The basic model
assumes a Gaussian likelihood and derives a spatial prior based on
thin-plate splines.

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
