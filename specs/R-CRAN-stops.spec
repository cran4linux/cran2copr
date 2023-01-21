%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stops
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Structure Optimized Proximity Scaling

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-cordillera 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-acepack 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-DiceOptim 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-CRAN-pomp 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-scagnostics 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-cmaes 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-cordillera 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-acepack 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-DiceOptim 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-tgp 
Requires:         R-CRAN-pomp 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-scagnostics 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-cmaes 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-nloptr 

%description
A collection of methods that fit nonlinear distance transformations in
multidimensional scaling (MDS) and trade-off the fit with structure
considerations to find optimal parameters also known as structure
optimized proximity scaling (STOPS) (Rusch, Mair & Hornik,
2023,<doi:10.1007/s11222-022-10197-w>). The package contains various
functions, wrappers, methods and classes for fitting, plotting and
displaying different MDS models in a STOPS framework like Torgerson
(classical) scaling, scaling by majorizing a complex function (SMACOF),
Sammon mapping, elastic scaling, symmetric SMACOF, spherical SMACOF,
s-stress, r-stress, power MDS, power elastic scaling, power Sammon
mapping, power stress MDS (POST-MDS), approximate power stress, Box-Cox
MDS, local MDS and Isomap. All of these models can also be fit
individually with given hyperparameters or by optimizing over
hyperparameters based on fit only (i.e., no structure considerations). The
package further contains functions for optimization, specifically the
adaptive Luus-Jaakola algorithm and a wrapper for Bayesian optimization
with treed Gaussian process with jumps to linear models, and functions for
various c-structuredness indices.

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
