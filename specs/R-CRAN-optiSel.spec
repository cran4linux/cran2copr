%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  optiSel
%global packver   2.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Optimum Contribution Selection and Population Genetics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-nadiv 
BuildRequires:    R-CRAN-pedigree 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ECOSolveR 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-optiSolve 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-nadiv 
Requires:         R-CRAN-pedigree 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-graphics 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magic 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ECOSolveR 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-optiSolve 

%description
A framework for the optimization of breeding programs via optimum
contribution selection and mate allocation. An easy to use set of function
for computation of optimum contributions of selection candidates, and of
the population genetic parameters to be optimized. These parameters can be
estimated using pedigree or genotype information, and include kinships,
kinships at native haplotype segments, and breed composition of crossbred
individuals. They are suitable for managing genetic diversity, removing
introgressed genetic material, and accelerating genetic gain.
Additionally, functions are provided for computing genetic contributions
from ancestors, inbreeding coefficients, the native effective size, the
native genome equivalent, pedigree completeness, and for preparing and
plotting pedigrees. The methods are described in:n Wellmann, R., and
Pfeiffer, I. (2009) <doi:10.1017/S0016672309000202>.n Wellmann, R., and
Bennewitz, J. (2011) <doi:10.2527/jas.2010-3709>.n Wellmann, R., Hartwig,
S., Bennewitz, J. (2012) <doi:10.1186/1297-9686-44-34>.n de Cara, M. A.
R., Villanueva, B., Toro, M. A., Fernandez, J. (2013)
<doi:10.1111/mec.12560>.n Wellmann, R., Bennewitz, J., Meuwissen, T.H.E.
(2014) <doi:10.1017/S0016672314000196>.n Wellmann, R. (2019)
<doi:10.1186/s12859-018-2450-5>.

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
