%global __brp_check_rpaths %{nil}
%global packname  prioritizr
%global packver   7.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Systematic Conservation Prioritization in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-withr >= 2.3.0
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-fasterize >= 1.0.2
BuildRequires:    R-CRAN-sf >= 0.8.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-exactextractr >= 0.2.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.1.0.0
BuildRequires:    R-CRAN-slam >= 0.1.48
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-proto 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-withr >= 2.3.0
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-fasterize >= 1.0.2
Requires:         R-CRAN-sf >= 0.8.0
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-exactextractr >= 0.2.0
Requires:         R-CRAN-slam >= 0.1.48
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-proto 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-plyr 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-magrittr 

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
Additionally, the 'rcbc' R package (available at
<https://github.com/dirkschumacher/rcbc>) can be used to generate
solutions using the CBC optimization software
(<https://projects.coin-or.org/Cbc>).

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
