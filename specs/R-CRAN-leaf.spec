%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  leaf
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Learning Equations for Automated Function Discovery

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.30
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-reticulate >= 1.30
Requires:         R-CRAN-R6 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rstudioapi 

%description
A unified framework for symbolic regression (SR) and multi-view symbolic
regression (MvSR) designed for complex, nonlinear systems, with particular
applicability to ecological datasets. The package implements a four-stage
workflow: data subset generation, functional form discovery, numerical
parameter optimization, and multi-objective evaluation. It provides a
high-level formula-style interface that abstracts and extends multiple
discovery engines: genetic programming (via PySR), Reinforcement Learning
with Monte Carlo Tree Search (via RSRM), and exhaustive generalized linear
model search. 'leaf' extends these methods by enabling multi-view
discovery, where functional structures are shared across groups while
parameters are fitted locally, and by supporting the enforcement of
domain-specific constraints, such as sign consistency across groups. The
framework automatically handles data normalization, link functions, and
back-transformation, ensuring that discovered symbolic equations remain
interpretable and valid on the original data scale. Implements methods
following ongoing work by the authors (2026, in preparation).

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
