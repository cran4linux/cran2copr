%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  steadyICA
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          ICA and Tests of Independence via Multivariate Distance Covariance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.9.13
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-combinat 
Requires:         R-CRAN-Rcpp >= 0.9.13
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-combinat 

%description
Functions related to multivariate measures of independence and ICA:
-estimate independent components by minimizing distance covariance;
-conduct a test of mutual independence based on distance covariance;
-estimate independent components via infomax (a popular method but
generally performs poorer than mdcovica, ProDenICA, and/or fastICA, but is
useful for comparisons); -order indepedent components by skewness; -match
independent components from multiple estimates; -other functions useful in
ICA.

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
