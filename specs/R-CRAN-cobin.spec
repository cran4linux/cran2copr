%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cobin
%global packver   1.0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Cobin and Micobin Regression Models for Continuous Proportional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-spNNGP 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-spNNGP 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functions for cobin and micobin regression models, a new family
of generalized linear models for continuous proportional data (Y in the
closed unit interval [0, 1]). It also includes an exact, efficient sampler
for the Kolmogorov-Gamma random variable. For details, see Lee et al.
(2025+) <doi:10.48550/arXiv.2504.15269>.

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
