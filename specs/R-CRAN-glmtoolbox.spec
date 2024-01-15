%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmtoolbox
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Set of Tools to Data Analysis using Generalized Linear Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-SuppDists 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rfast 
Requires:         R-splines 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-SuppDists 

%description
Set of tools for the statistical analysis of data using: (1) normal linear
models; (2) generalized linear models; (3) negative binomial regression
models as alternative to the Poisson regression models under the presence
of overdispersion; (4) beta-binomial and random-clumped binomial
regression models as alternative to the binomial regression models under
the presence of overdispersion; (5) Zero-inflated and zero-altered
regression models to deal with zero-excess in count data; (6) generalized
nonlinear models; (7) generalized estimating equations for cluster
correlated data.

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
