%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stops
%global packver   1.8-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Structure Optimized Proximity Scaling

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-smacofx 
BuildRequires:    R-CRAN-acepack 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-cmaes 
BuildRequires:    R-CRAN-cordillera 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-DiceOptim 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-pomp 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-CRAN-scagnostics 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-smacofx 
Requires:         R-CRAN-acepack 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-cmaes 
Requires:         R-CRAN-cordillera 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-DiceOptim 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-pomp 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-registry 
Requires:         R-CRAN-scagnostics 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-tgp 
Requires:         R-CRAN-vegan 

%description
Methods that use flexible variants of multidimensional scaling (MDS) which
incorporate parametric nonlinear distance transformations and trade-off
the goodness-of-fit fit with structure considerations to find optimal
hyperparameters, also known as structure optimized proximity scaling
(STOPS) (Rusch, Mair & Hornik, 2023,<doi:10.1007/s11222-022-10197-w>). The
package contains various functions, wrappers, methods and classes for
fitting, plotting and displaying different 1-way MDS models with ratio,
interval, ordinal optimal scaling in a STOPS framework. These cover
essentially the functionality of the package smacofx, including Torgerson
(classical) scaling with power transformations of dissimilarities, SMACOF
MDS with powers of dissimilarities, Sammon mapping with powers of
dissimilarities, elastic scaling with powers of dissimilarities, spherical
SMACOF with powers of dissimilarities, (ALSCAL) s-stress MDS with powers
of dissimilarities, r-stress MDS, MDS with powers of dissimilarities and
configuration distances, elastic scaling powers of dissimilarities and
configuration distances, Sammon mapping powers of dissimilarities and
configuration distances, power stress MDS (POST-MDS), approximate power
stress, Box-Cox MDS, local MDS, Isomap, curvilinear component analysis
(CLCA), curvilinear distance analysis (CLDA) and sparsified (power)
multidimensional scaling and (power) multidimensional distance analysis
(experimental models from smacofx influenced by CLCA). All of these models
can also be fit by optimizing over hyperparameters based on
goodness-of-fit fit only (i.e., no structure considerations). The package
further contains functions for optimization, specifically the adaptive
Luus-Jaakola algorithm and a wrapper for Bayesian optimization with treed
Gaussian process with jumps to linear models, and functions for various
c-structuredness indices.

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
