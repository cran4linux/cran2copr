%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rMOST
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimates Pareto-Optimal Solution for Hiring with 3 Objectives

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-nloptr 
Requires:         R-stats 

%description
Estimates Pareto-optimal solution for personnel selection with 3
objectives using Normal Boundary Intersection (NBI) algorithm introduced
by Das and Dennis (1998) <doi:10.1137/S1052623496307510>. Takes predictor
intercorrelations and predictor-objective relations as input and generates
a series of solutions containing predictor weights as output. Accepts
between 3 and 10 selection predictors. Maximum 2 objectives could be
adverse impact objectives. Partially modeled after De Corte (2006) TROFSS
Fortran program <https://users.ugent.be/~wdecorte/trofss.pdf> and updated
from 'ParetoR' package described in Song et al. (2017)
<doi:10.1037/apl0000240>. For details, see Song et al. (in press).

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
