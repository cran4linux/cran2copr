%global __brp_check_rpaths %{nil}
%global packname  spldv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Models for Limited Dependent Variables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sphet 
BuildRequires:    R-CRAN-memisc 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-maxLik 
Requires:         R-stats 
Requires:         R-CRAN-sphet 
Requires:         R-CRAN-memisc 
Requires:         R-CRAN-car 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 

%description
The current version of this package estimates spatial autoregressive
models for binary dependent variables using GMM estimators. It supports
one-step (Pinkse and Slade, 1998) <doi:10.1016/S0304-4076(97)00097-3> and
two-step GMM estimator along with the linearized GMM estimator proposed by
Klier and McMillen (2008) <doi:10.1198/073500107000000188>. It also allows
for either Probit or Logit model and compute the average marginal effects.

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
