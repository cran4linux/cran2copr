%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nQuack
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Predicting Ploidal Level from Sequence Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppArmadillo >= 14.0.2.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-RcppArmadillo >= 14.0.2.1
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-magrittr 

%description
Predicts ploidal level from sequence data using site-based heterozygosity
and a mixture models approach. See Gaynor et al. (2024)
<doi:10.1002/aps3.11606>.

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
