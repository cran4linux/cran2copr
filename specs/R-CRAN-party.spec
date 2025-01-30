%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  party
%global packver   1.3-18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.18
Release:          1%{?dist}%{?buildtag}
Summary:          A Laboratory for Recursive Partytioning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-survival >= 2.37.7
BuildRequires:    R-CRAN-sandwich >= 1.1.1
BuildRequires:    R-CRAN-coin >= 1.1.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.2
BuildRequires:    R-CRAN-modeltools >= 0.2.21
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-survival >= 2.37.7
Requires:         R-CRAN-sandwich >= 1.1.1
Requires:         R-CRAN-coin >= 1.1.0
Requires:         R-CRAN-mvtnorm >= 1.0.2
Requires:         R-CRAN-modeltools >= 0.2.21
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-zoo 

%description
A computational toolbox for recursive partitioning. The core of the
package is ctree(), an implementation of conditional inference trees which
embed tree-structured regression models into a well defined theory of
conditional inference procedures. This non-parametric class of regression
trees is applicable to all kinds of regression problems, including
nominal, ordinal, numeric, censored as well as multivariate response
variables and arbitrary measurement scales of the covariates. Based on
conditional inference trees, cforest() provides an implementation of
Breiman's random forests. The function mob() implements an algorithm for
recursive partitioning based on parametric models (e.g. linear models,
GLMs or survival regression) employing parameter instability tests for
split selection. Extensible functionality for visualizing tree-structured
regression models is available. The methods are described in Hothorn et
al. (2006) <doi:10.1198/106186006X133933>, Zeileis et al. (2008)
<doi:10.1198/106186008X319331> and Strobl et al. (2007)
<doi:10.1186/1471-2105-8-25>.

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
