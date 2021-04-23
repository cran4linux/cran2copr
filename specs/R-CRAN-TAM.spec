%global packname  TAM
%global packver   3.6-45
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.45
Release:          1%{?dist}%{?buildtag}
Summary:          Test Analysis Modules

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-CDM >= 6.4.19
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CDM >= 6.4.19
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Includes marginal maximum likelihood estimation and joint maximum
likelihood estimation for unidimensional and multidimensional item
response models. The package functionality covers the Rasch model, 2PL
model, 3PL model, generalized partial credit model, multi-faceted Rasch
model, nominal item response model, structured latent class model, mixture
distribution IRT models, and located latent class models. Latent
regression models and plausible value imputation are also supported. For
details see Adams, Wilson and Wang, 1997 <doi:10.1177/0146621697211001>,
Adams, Wilson and Wu, 1997 <doi:10.3102/10769986022001047>, Formann, 1982
<doi:10.1002/bimj.4710240209>, Formann, 1992
<doi:10.1080/01621459.1992.10475229>.

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
