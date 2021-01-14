%global packname  JointAI
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Analysis and Imputation of Incomplete Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-future 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MASS 

%description
Joint analysis and imputation of incomplete data in the Bayesian
framework, using (generalized) linear (mixed) models and extensions there
of, survival models, or joint models for longitudinal and survival data.
Incomplete covariates, if present, are automatically imputed. The package
performs some preprocessing of the data and creates a 'JAGS' model, which
will then automatically be passed to 'JAGS'
<http://mcmc-jags.sourceforge.net/> with the help of the package 'rjags'.

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
