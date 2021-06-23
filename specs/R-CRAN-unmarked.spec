%global __brp_check_rpaths %{nil}
%global packname  unmarked
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Models for Data from Unmarked Animals

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildRequires:    R-CRAN-TMB >= 1.7.18
BuildRequires:    R-CRAN-Rcpp >= 0.8.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-TMB >= 1.7.18
Requires:         R-CRAN-Rcpp >= 0.8.0
Requires:         R-methods 
Requires:         R-CRAN-lattice 
Requires:         R-graphics 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-raster 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits hierarchical models of animal abundance and occurrence to data
collected using survey methods such as point counts, site occupancy
sampling, distance sampling, removal sampling, and double observer
sampling. Parameters governing the state and observation processes can be
modeled as functions of covariates.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
