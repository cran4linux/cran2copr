%global packname  stpm
%global packver   1.7.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.10
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Process Model for Analysis of Longitudinal and Time-to-Event Outcomes

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-sas7bdat 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-sas7bdat 
Requires:         R-stats 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-survival 
Requires:         R-tools 
Requires:         R-CRAN-MASS 

%description
Utilities to estimate parameters of the models with survival functions
induced by stochastic covariates. Miscellaneous functions for data
preparation and simulation are also provided. For more information, see:
(i)"Stochastic model for analysis of longitudinal data on aging and
mortality" by Yashin A. et al. (2007), Mathematical Biosciences, 208(2),
538-551, <DOI:10.1016/j.mbs.2006.11.006>; (ii) "Health decline, aging and
mortality: how are they related?" by Yashin A. et al. (2007),
Biogerontology 8(3), 291(302), <DOI:10.1007/s10522-006-9073-3>.

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
