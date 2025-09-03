%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  piecewiseSEM
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Piecewise Structural Equation Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-performance 
Requires:         R-CRAN-car 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-performance 

%description
Implements piecewise structural equation modeling from a single list of
structural equations, with new methods for non-linear, latent, and
composite variables, standardized coefficients, query-based prediction and
indirect effects. See <http://jslefche.github.io/piecewiseSEM/> for more.

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
