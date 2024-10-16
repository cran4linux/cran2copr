%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FDX
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          False Discovery Exceedance Controlling Multiple Testing Procedures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildRequires:    R-CRAN-DiscreteFDR >= 2.0.0
BuildRequires:    R-CRAN-PoissonBinomial >= 1.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-DiscreteFDR >= 2.0.0
Requires:         R-CRAN-PoissonBinomial >= 1.2.0
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 

%description
Multiple testing procedures for heterogeneous and discrete tests as
described in Döhler and Roquain (2020) <doi:10.1214/20-EJS1771>. The main
algorithms of the paper are available as continuous, discrete and weighted
versions. They take as input the results of a test procedure from package
'DiscreteTests', or a set of observed p-values and their discrete support
under their nulls. A shortcut function to obtain such p-values and
supports is also provided, along with wrappers allowing to apply discrete
procedures directly to data.

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
