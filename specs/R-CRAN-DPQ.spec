%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DPQ
%global packver   0.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Density, Probability, Quantile ('DPQ') Computations

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-sfsmisc >= 1.1.14
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-sfsmisc >= 1.1.14
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 

%description
Computations for approximations and alternatives for the 'DPQ' (Density
(pdf), Probability (cdf) and Quantile) functions for probability
distributions in R. Primary focus is on (central and non-central) beta,
gamma and related distributions such as the chi-squared, F, and t. -- For
several distribution functions, provide functions implementing formulas
from Johnson, Kotz, and Kemp (1992) <doi:10.1002/bimj.4710360207> and
Johnson, Kotz, and Balakrishnan (1995) for discrete or continuous
distributions respectively. This is for the use of researchers in these
numerical approximation implementations, notably for my own use in order
to improve standard R pbeta(), qgamma(), ..., etc: {'"dpq"'-functions}.

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
