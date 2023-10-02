%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gofedf
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness of Fit Tests Based on Empirical Distribution Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-glm2 
BuildRequires:    R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-glm2 
Requires:         R-CRAN-statmod 

%description
Routines that allow the user to run goodness of fit tests based on
empirical distribution functions for formal model evaluation in a general
likelihood model. In addition, functions are provided to test a sample
against Normal or Gamma distributions, validate the normality assumptions
in a linear model, and examine the appropriateness of a Gamma distribution
in generalized linear models with various link functions. Michael Arthur
Stephens (1976) <http://www.jstor.org/stable/2958206>.

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
