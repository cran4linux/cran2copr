%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UMDA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate Marginal Distribution Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EEEA 
Requires:         R-CRAN-EEEA 

%description
Implements the Univariate Marginal Distribution Algorithm (UMDA), an
Estimation of Distribution Algorithm (EDA) for continuous optimization
problems. The method iteratively selects the best individuals from a
population, estimates an independent marginal probability distribution for
each decision variable, and generates new candidate solutions by sampling
from the estimated distributions. This process allows the probability
model to adapt toward promising regions of the search space. The
implementation supports normal, triangular, histogram-based, and uniform
probability distributions, together with an optional explicit exploration
strategy for the initialization of the population. The implemented
explicit exploration strategy in this package is described in Salinas
Gutierrez and Muñoz Zavala (2023) <doi:10.1016/j.asoc.2023.110230>.

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
