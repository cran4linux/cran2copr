%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mstATA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Test Assembly for Multistage Tests Using Mixed-Integer Linear Programming

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 

%description
Provides a suite of mixed-integer linear programming (MILP) model builders
and solvers—including 'Gurobi', 'HiGHS', 'Symphony', 'GNU Linear
Programming Kit (GLPK)', and 'lpSolve'—for automated test assembly (ATA)
in multistage testing (MST). Offers filtering of decision variables
through item–module eligibility and the application of explicit bounds to
simplify the MILP model and accelerate the optimization process. Supports
bottom up, top down, and hybrid assembly strategies; enemy-item and
enemy-stimulus exclusions; stimulus all in/all out or partial selection;
anchor item/stimulus specification; and item exposure control.
Accommodates both single-objective and multi-objective optimization
('weighted sum', 'maximin', 'capped maximin', 'minimax', and 'goal
programming'). Enables simultaneous assembly of multiple panels with item
and stimulus content balancing and exposure control. Provides analytical
evaluation of assembled MST performance within seconds. Includes tools for
diagnosing infeasible optimization models by systematically identifying
sources of infeasibility and reformulating models with slack variables to
restore feasibility.Methods implemented in this package build on
established work in optimal test assembly (van der Linden, 2005
<doi:10.1007/0-387-29054-0>), item-set constrained test assembly (van der
Linden, 2000 <doi:10.1177/01466210022031697>), hybrid assembly (Xiong,
2018 <doi:10.1177/0146621618762739>), recursion-based analytic methods
(Lim et al., 2021 <doi:10.1111/jedm.12276>), and classification evaluation
(Rudner, 2000 <doi:10.7275/an9m-2035>; Rudner, 2005
<doi:10.7275/56a5-6b14>).

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
