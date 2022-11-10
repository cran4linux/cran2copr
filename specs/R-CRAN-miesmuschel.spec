%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  miesmuschel
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Integer Evolution Strategies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.9.0
BuildRequires:    R-CRAN-paradox >= 0.7.1
BuildRequires:    R-CRAN-mlr3misc >= 0.5.0
BuildRequires:    R-CRAN-bbotk >= 0.3.0.900
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-lgr 
Requires:         R-CRAN-checkmate >= 1.9.0
Requires:         R-CRAN-paradox >= 0.7.1
Requires:         R-CRAN-mlr3misc >= 0.5.0
Requires:         R-CRAN-bbotk >= 0.3.0.900
Requires:         R-CRAN-R6 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-lgr 

%description
Evolutionary black box optimization algorithms building on the 'bbotk'
package. 'miesmuschel' offers both ready-to-use optimization algorithms,
as well as their fundamental building blocks that can be used to manually
construct specialized optimization loops. The Mixed Integer Evolution
Strategies as described by Li et al. (2013) <doi:10.1162/EVCO_a_00059> can
be implemented, as well as the multi-objective optimization algorithms
NSGA-II by Deb, Pratap, Agarwal, and Meyarivan (2002)
<doi:10.1109/4235.996017>.

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
