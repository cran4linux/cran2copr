%global __brp_check_rpaths %{nil}
%global packname  cops
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Optimized Proximity Scaling

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-smacof >= 1.10.4
BuildRequires:    R-CRAN-cordillera >= 0.7.2
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-NlcOptim 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-CRAN-cmaes 
BuildRequires:    R-CRAN-crs 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-GenSA 
Requires:         R-CRAN-smacof >= 1.10.4
Requires:         R-CRAN-cordillera >= 0.7.2
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-NlcOptim 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-subplex 
Requires:         R-CRAN-cmaes 
Requires:         R-CRAN-crs 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-GenSA 

%description
Cluster optimized proximity scaling (COPS) refers to multidimensional
scaling (MDS) methods that aim at pronouncing the clustered appearance of
the configuration (Rusch, Mair & Hornik, 2021,
<doi:10.1080/10618600.2020.1869027> ). They achieve this by transforming
proximities/distances with power functions and augment the fitting
criterion with a clusteredness index, the OPTICS Cordillera (Rusch, Hornik
& Mair, 2018, <doi:10.1080/10618600.2017.1349664> ). There are two
variants: One for finding the configuration directly (COPS-C) for ratio,
power, interval and non-metric MDS (Borg & Groenen, 2005,
ISBN:978-0-387-28981-6), and one for using the augmented fitting criterion
to find optimal parameters (P-COPS). The package contains various
functions, wrappers, methods and classes for fitting, plotting and
displaying different MDS models in a COPS framework like ratio, interval
and non-metric MDS for COPS-C and P-COPS with Torgerson scaling
(Torgerson, 1958, ISBN:978-0471879459), scaling by majorizing a complex
function (SMACOF; de Leeuw, 1977,
<https://escholarship.org/uc/item/4ps3b5mj> ), Sammon mapping (Sammon,
1969, <doi:10.1109/T-C.1969.222678> ), elastic scaling (McGee, 1966,
<doi:10.1111/j.2044-8317.1966.tb00367.x> ), s-stress (Takane, Young & de
Leeuw, 1977, <doi:10.1007/BF02293745> ), r-stress (de Leeuw, Groenen &
Mair, 2016, <https://rpubs.com/deleeuw/142619>), power-stress (Buja &
Swayne, 2002 <doi:10.1007/s00357-001-0031-0>), restricted power stress,
approximated power stress, power elastic scaling, power Sammon mapping
(Rusch, Mair & Hornik, 2021, <doi:10.1080/10618600.2020.1869027> ). All of
these models can also solely be fit as MDS with power transformations. The
package further contains a function for pattern search optimization, the
``Adaptive Luus-Jakola Algorithm'' (Rusch, Mair & Hornik, 2021,
<doi:10.1080/10618600.2020.1869027> ).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
