%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smartsnp
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Multivariate Analyses of Big Genomic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-bootSVD 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-bootSVD 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-Rcpp 

%description
Fast computation of multivariate analyses of small (10s to 100s markers)
to big (1000s to 100000s) genotype data. Runs Principal Component Analysis
allowing for centering, z-score standardization and scaling for genetic
drift, projection of ancient samples to modern genetic space and
multivariate tests for differences in group location (Permutation-Based
Multivariate Analysis of Variance) and dispersion (Permutation-Based
Multivariate Analysis of Dispersion).

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
