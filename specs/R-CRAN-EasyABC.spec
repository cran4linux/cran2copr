%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EasyABC
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Approximate Bayesian Computation Sampling Schemes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-abc 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-tensorA 
Requires:         R-CRAN-abc 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-tensorA 

%description
Enables launching a series of simulations of a computer code from the R
session, and to retrieve the simulation outputs in an appropriate format
for post-processing treatments. Five sequential sampling schemes and three
coupled-to-MCMC schemes are implemented.

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
