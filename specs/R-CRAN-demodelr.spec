%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  demodelr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Differential Equations with Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-tibble 

%description
Designed to support the visualization, numerical computation, qualitative
analysis, model-data fusion, and stochastic simulation for autonomous
systems of differential equations. Euler and Runge-Kutta methods are
implemented, along with tools to visualize the two-dimensional phaseplane.
Likelihood surfaces and a simple Markov Chain Monte Carlo parameter
estimator can be used for model-data fusion of differential equations and
empirical models. The Euler-Maruyama method is provided for simulation of
stochastic differential equations. The package was originally written for
internal use to support teaching by Zobitz, and refined to support the
text "Exploring modeling with data and differential equations using R" by
John Zobitz (2021) <https://jmzobitz.github.io/ModelingWithR/index.html>.

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
