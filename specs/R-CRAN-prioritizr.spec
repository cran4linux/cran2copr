%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prioritizr
%global packver   8.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Systematic Conservation Prioritization in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ape >= 5.6
BuildRequires:    R-CRAN-raster >= 3.6.11
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-withr >= 2.3.0
BuildRequires:    R-CRAN-igraph >= 2.0.3
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.75.0.0
BuildRequires:    R-CRAN-terra >= 1.6.53
BuildRequires:    R-CRAN-Matrix >= 1.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-sf >= 1.0.12
BuildRequires:    R-CRAN-exactextractr >= 0.8.1
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.7.3.0
BuildRequires:    R-CRAN-slam >= 0.1.48
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ape >= 5.6
Requires:         R-CRAN-raster >= 3.6.11
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-withr >= 2.3.0
Requires:         R-CRAN-igraph >= 2.0.3
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-terra >= 1.6.53
Requires:         R-CRAN-Matrix >= 1.3.0
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-sf >= 1.0.12
Requires:         R-CRAN-exactextractr >= 0.8.1
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-slam >= 0.1.48
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-parallel 

%description
Systematic conservation prioritization using mixed integer linear
programming (MILP). It provides a flexible interface for building and
solving conservation planning problems. Once built, conservation planning
problems can be solved using a variety of commercial and open-source exact
algorithm solvers. By using exact algorithm solvers, solutions can be
generated that are guaranteed to be optimal (or within a pre-specified
optimality gap). Furthermore, conservation problems can be constructed to
optimize the spatial allocation of different management actions or zones,
meaning that conservation practitioners can identify solutions that
benefit multiple stakeholders. To solve large-scale or complex
conservation planning problems, users should install the Gurobi
optimization software (available from <https://www.gurobi.com/>) and the
'gurobi' R package (see Gurobi Installation Guide vignette for details).
Users can also install the IBM CPLEX software
(<https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer>)
and the 'cplexAPI' R package (available at
<https://github.com/cran/cplexAPI>). Additionally, the 'rcbc' R package
(available at <https://github.com/dirkschumacher/rcbc>) can be used to
generate solutions using the CBC optimization software
(<https://github.com/coin-or/Cbc>).

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
