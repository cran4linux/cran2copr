%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  unmarked
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Models for Data from Unmarked Animals

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildRequires:    R-CRAN-TMB >= 1.7.18
BuildRequires:    R-CRAN-Rcpp >= 0.8.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.7.18
Requires:         R-CRAN-Rcpp >= 0.8.0
Requires:         R-graphics 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits hierarchical models of animal abundance and occurrence to data
collected using survey methods such as point counts, site occupancy
sampling, distance sampling, removal sampling, and double observer
sampling. Parameters governing the state and observation processes can be
modeled as functions of covariates. References: Kellner et al. (2023)
<doi:10.1111/2041-210X.14123>, Fiske and Chandler (2011)
<doi:10.18637/jss.v043.i10>.

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
