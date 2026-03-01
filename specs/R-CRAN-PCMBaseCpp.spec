%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PCMBaseCpp
%global packver   0.1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.12
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Likelihood Calculation for Phylogenetic Comparative Models

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-PCMBase 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-PCMBase 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-abind 

%description
Provides a C++ backend for multivariate phylogenetic comparative models
implemented in the R-package 'PCMBase'. Can be used in combination with
'PCMBase' to enable fast and parallel likelihood calculation. Implements
the pruning likelihood calculation algorithm described in Mitov et al.
(2020) <doi:10.1016/j.tpb.2019.11.005>. Uses the 'SPLITT' C++ library for
parallel tree traversal described in Mitov and Stadler (2018)
<doi:10.1111/2041-210X.13136>.

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
