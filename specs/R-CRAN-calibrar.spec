%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  calibrar
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Parameter Estimation for Complex Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-cmaes 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-soma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-cmaes 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-GenSA 
Requires:         R-graphics 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-parallel 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-soma 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
General optimisation and specific tools for the parameter estimation (i.e.
calibration) of complex models, including stochastic ones. It implements
generic functions that can be used for fitting any type of models,
especially those with non-differentiable objective functions, with the
same syntax as base::optim. It supports multiple phases estimation
(sequential parameter masking), constrained optimization (bounding box
restrictions) and automatic parallel computation of numerical gradients.
Some common maximum likelihood estimation methods and automated
construction of the objective function from simulated model outputs is
provided. See <https://roliveros-ramos.github.io/calibrar/> for more
details.

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
