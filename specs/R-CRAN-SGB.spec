%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SGB
%global packver   1.0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simplicial Generalized Beta Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-alabama 
Requires:         R-CRAN-Formula 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-alabama 

%description
Main properties and regression procedures using a generalization of the
Dirichlet distribution called Simplicial Generalized Beta distribution. It
is a new distribution on the simplex (i.e. on the space of compositions or
positive vectors with sum of components equal to 1). The Dirichlet
distribution can be constructed from a random vector of independent Gamma
variables divided by their sum. The SGB follows the same construction with
generalized Gamma instead of Gamma variables. The Dirichlet exponents are
supplemented by an overall shape parameter and a vector of scales. The
scale vector is itself a composition and can be modeled with auxiliary
variables through a log-ratio transformation. Graf, M. (2017, ISBN:
978-84-947240-0-8). See also the vignette enclosed in the package.

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
