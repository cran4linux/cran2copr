%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tamd
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Transcendental Algorithm for Mixtures of Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Implements the Transcendental Algorithm for Mixtures of Distributions
(TAMD), a penalized likelihood framework for fitting finite Gaussian
mixture models. TAMD augments the Expectation-Maximization (EM) algorithm
with analytic barrier terms built from the Hellinger affinity that diverge
on the singular locus, actively preventing component coalescence and
weight degeneracy. Provides the core TAMD fitting function, closed-form
Hellinger affinity and gradient computations, the Transcendental Affinity
Criterion (TAC) for geometry-aware model selection, the regularity index
rho (a scalar diagnostic for mixture fit quality), and reproduction
scripts for all simulation studies. Methods are described in Fokoue (2024)
<doi:10.48550/arXiv.2602.03889>. See also Titterington, Smith and Makov
(1985, ISBN:0-471-90510-4) and Watanabe (2009, ISBN:978-0-521-86408-7).

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
