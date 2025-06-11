%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayou
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Fitting of Ornstein-Uhlenbeck Models to Phylogenies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-ape >= 3.0.6
BuildRequires:    R-CRAN-geiger >= 2.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-denstrip 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape >= 3.0.6
Requires:         R-CRAN-geiger >= 2.0
Requires:         R-CRAN-Rcpp >= 0.10.3
Requires:         R-CRAN-coda 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-denstrip 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mnormt 
Requires:         R-stats 

%description
Fits and simulates multi-optima Ornstein-Uhlenbeck models to phylogenetic
comparative data using Bayesian reversible-jump methods. See Uyeda and
Harmon (2014) <DOI:10.1093/sysbio/syu057>.

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
