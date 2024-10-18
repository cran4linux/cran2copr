%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mbbefd
%global packver   0.8.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.12
Release:          1%{?dist}%{?buildtag}
Summary:          Maxwell Boltzmann Bose Einstein Fermi Dirac Distribution and Destruction Rate Modelling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-fitdistrplus >= 1.1.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-fitdistrplus >= 1.1.4
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-alabama 
Requires:         R-utils 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-MASS 

%description
Distributions that are typically used for exposure rating in general
insurance, in particular to price reinsurance contracts. The vignette
shows code snippets to fit the distribution to empirical data. See, e.g.,
Bernegger (1997) <doi:10.2143/AST.27.1.563208> freely available on-line.

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
