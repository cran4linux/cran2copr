%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ifit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Fitting of Parametric Models with Minimum Prior Information

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-parallel 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lpSolve 
Requires:         R-parallel 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements an algorithm for fitting a generative model with an intractable
likelihood using only box constraints on the parameters.  The implemented
algorithm consists of two phases. The first phase (global search) aims to
identify the region containing the best solution, while the second phase
(local search) refines this solution using a trust-region version of the
Fisher scoring method to solve a quasi-likelihood equation. See Guido
Masarotto (2025) <doi:10.48550/arXiv.2511.08180> for the details of the
algorithm and supporting results.

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
