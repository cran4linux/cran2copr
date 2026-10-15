%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Person Parameter Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-tinyplot >= 0.8.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-tinyplot >= 0.8.0
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimation of person parameters (abilities) for the 1, 2, 3 and 4
parameter logistic model, the (generalized) partial credit model and tests
that mix dichotomous and polytomous items, under the assumption that the
item parameters are known and fixed: maximum likelihood, weighted
likelihood (Warm, 1989 <doi:10.1007/BF02294627>), maximum and expected a
posteriori and robust estimation (Schuster and Yuan, 2011
<doi:10.3102/1076998610396890>). Further features are jackknife estimates
(Wainer and Wright, 1980 <doi:10.1007/BF02293910>), plausible values, the
person fit statistics lz, lz* (Snijders, 2001 <doi:10.1007/BF02294437>),
infit and outfit, and the simulation of response data. Models fitted with
the 'eRm' package can be passed on directly. The package is useful, e.g.,
when items of an item bank are given to a new sample of persons.

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
