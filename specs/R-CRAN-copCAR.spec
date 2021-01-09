%global packname  copCAR
%global packver   2.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting the copCAR Regression Model for Discrete Areal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spam 

%description
Provides tools for fitting the copCAR (Hughes, 2015)
<DOI:10.1080/10618600.2014.948178> regression model for discrete areal
data. Three types of estimation are supported (continuous extension,
composite marginal likelihood, and distributional transform), for three
types of outcomes (Bernoulli, negative binomial, and Poisson).

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
