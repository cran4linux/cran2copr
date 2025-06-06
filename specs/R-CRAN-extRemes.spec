%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  extRemes
%global packver   2.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Value Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-distillery >= 1.0.4
BuildRequires:    R-CRAN-Lmoments 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-distillery >= 1.0.4
Requires:         R-CRAN-Lmoments 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
General functions for performing extreme value analysis.  In particular,
allows for inclusion of covariates into the parameters of the
extreme-value distributions, as well as estimation through MLE, L-moments,
generalized (penalized) MLE (GMLE), as well as Bayes.  Inference methods
include parametric normal approximation, profile-likelihood, Bayes, and
bootstrapping.  Some bivariate functionality and dependence checking
(e.g., auto-tail dependence function plot, extremal index estimation) is
also included.  For a tutorial, see Gilleland and Katz (2016) <doi:
10.18637/jss.v072.i08> and for bootstrapping, please see Gilleland (2020)
<doi: 10.1175/JTECH-D-20-0070.1>.

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
