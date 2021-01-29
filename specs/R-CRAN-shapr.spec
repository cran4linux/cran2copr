%global packname  shapr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction Explanation with Dependence-Aware Shapley Values

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-condMVNorm 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-condMVNorm 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-Matrix 

%description
Complex machine learning models are often hard to interpret. However, in
many situations it is crucial to understand and explain why a model made a
specific prediction. Shapley values is the only method for such prediction
explanation framework with a solid theoretical foundation. Previously
known methods for estimating the Shapley values do, however, assume
feature independence. This package implements the method described in Aas,
Jullum and Løland (2019) <arXiv:1903.10464>, which accounts for any
feature dependence, and thereby produces more accurate estimates of the
true Shapley values.

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
