%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hydroMOPSO
%global packver   0.1-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.14
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Objective Optimisation with Focus on Environmental Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-hydroTSM 
BuildRequires:    R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-parallel 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-hydroTSM 
Requires:         R-methods 

%description
State-of-the-art Multi-Objective Particle Swarm Optimiser (MOPSO), based
on the algorithm developed by Lin et al. (2018)
<doi:10.1109/TEVC.2016.2631279> with improvements described by
Marinao-Rivas & Zambrano-Bigiarini (2020)
<doi:10.1109/LA-CCI48322.2021.9769844>. This package is inspired by and
closely follows the philosophy of the single objective 'hydroPSO' R
package ((Zambrano-Bigiarini & Rojas, 2013)
<doi:10.1016/j.envsoft.2013.01.004>), and can be used for global
optimisation of non-smooth and non-linear R functions and R-base models
(e.g., 'TUWmodel', 'GR4J', 'GR6J'). However, the main focus of
'hydroMOPSO' is optimising environmental and other real-world models that
need to be run from the system console (e.g., 'SWAT+'). 'hydroMOPSO'
communicates with the model to be optimised through its input and output
files, without requiring modifying its source code. Thanks to its flexible
design and the availability of several fine-tuning options, 'hydroMOPSO'
can tackle a wide range of multi-objective optimisation problems (e.g.,
multi-objective functions, multiple model variables, multiple periods).
Finally, 'hydroMOPSO' is designed to run on multi-core machines or network
clusters, to alleviate the computational burden of complex models with
long execution time.

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
