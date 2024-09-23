%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cops
%global packver   1.12-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Optimized Proximity Scaling

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cordillera >= 0.7.2
BuildRequires:    R-CRAN-smacofx 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-analogue 
BuildRequires:    R-CRAN-cmaes 
BuildRequires:    R-CRAN-crs 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-NlcOptim 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-subplex 
Requires:         R-CRAN-cordillera >= 0.7.2
Requires:         R-CRAN-smacofx 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-analogue 
Requires:         R-CRAN-cmaes 
Requires:         R-CRAN-crs 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-NlcOptim 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-subplex 

%description
Multidimensional scaling (MDS) methods that aim at pronouncing the
clustered appearance of the configuration (Rusch, Mair & Hornik, 2021,
<doi:10.1080/10618600.2020.1869027>). They achieve this by transforming
proximities/distances with explicit power functions and penalizing the
fitting criterion with a clusteredness index, the OPTICS Cordillera
(Rusch, Hornik & Mair, 2018, <doi:10.1080/10618600.2017.1349664>). There
are two variants: One for finding the configuration directly (COPS-C) with
given explicit power transformations and implicit ratio, interval and
non-metric optimal scaling transformations (Borg & Groenen, 2005,
ISBN:978-0-387-28981-6), and one for using the augmented fitting criterion
to find optimal hyperparameters for the explicit transformations (P-COPS).
The package contains various functions, wrappers, methods and classes for
fitting, plotting and displaying a large number of different MDS models
(most of the functionality in smacofx) in the COPS framework. The package
further contains a function for pattern search optimization, the
``Adaptive Luus-Jaakola Algorithm'' (Rusch, Mair & Hornik,
2021,<doi:10.1080/10618600.2020.1869027>) and a functions to calculate the
phi-distances for count data or histograms.

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
