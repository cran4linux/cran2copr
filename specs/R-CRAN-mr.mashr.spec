%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mr.mashr
%global packver   0.3.44
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.44
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Regression with Multivariate Adaptive Shrinkage

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-RcppParallel >= 5.1.10
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-flashier >= 1.0.7
BuildRequires:    R-CRAN-mashr >= 0.2.73
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.4.0.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ebnm 
BuildRequires:    R-parallel 
Requires:         R-CRAN-RcppParallel >= 5.1.10
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-flashier >= 1.0.7
Requires:         R-CRAN-mashr >= 0.2.73
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ebnm 
Requires:         R-parallel 

%description
Provides an implementation of methods for multivariate multiple regression
with adaptive shrinkage priors as described in F. Morgante et al (2023)
<doi:10.1371/journal.pgen.1010539>.

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
