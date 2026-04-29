%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiscape
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Objective Spatial Planning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.1.0.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-proto 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-proto 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-sf 
Requires:         R-methods 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-ggrepel 

%description
Provides a modular framework for exact multi-objective spatial planning
using mixed-integer programming. The package supports the definition of
planning problems through planning units, features, management actions,
action effects, spatial relations, targets, constraints, and objective
functions. It enables the optimisation of spatial planning portfolios
under considerations such as boundary structure, connectivity, and
fragmentation. Supported multi-objective methods include weighted-sum
aggregation, epsilon-constraint, and the augmented epsilon-constraint
method. Problems can be solved with several commercial and open-source
optimisation solvers. Optional solver backends include the 'gurobi' R
package, which is distributed with the Gurobi Optimizer installation
<https://docs.gurobi.com/projects/optimizer/en/13.0/reference/r/setup.html>,
and the 'rcbc' R package, available from GitHub at
<https://github.com/dirkschumacher/rcbc>. For background on
multi-objective optimisation methods, see Halffmann et al. (2022)
<doi:10.1002/mcda.1780>; for the augmented epsilon-constraint method, see
Mavrotas (2009) <doi:10.1016/j.amc.2009.03.037>.

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
