%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flexrsurv
%global packver   2.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Relative Survival Analysis

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-orthogonalsplinebasis 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-survival 
Requires:         R-utils 
Requires:         R-CRAN-orthogonalsplinebasis 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Epi 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-formula.tools 
Requires:         R-splines 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-Matrix 

%description
Package for parametric relative survival analyses. It allows to model
non-linear and non-proportional effects and both non proportional and non
linear effects, using splines (B-spline and truncated power basis),
Weighted Cumulative Index of Exposure effect, with correction model for
the life table. Both non proportional and non linear effects are described
in Remontet, L. et al. (2007) <doi:10.1002/sim.2656> and Mahboubi, A. et
al. (2011) <doi:10.1002/sim.4208>.

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
