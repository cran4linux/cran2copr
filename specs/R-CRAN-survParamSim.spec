%global packname  survParamSim
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Survival Simulation with Parameter Uncertainty

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 2.43
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tidyr >= 1.1
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-survival >= 2.43
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tidyr >= 1.1
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Perform survival simulation with parametric survival model generated from
'survreg' function in 'survival' package. In each simulation coefficients
are resampled from variance-covariance matrix of parameter estimates to
capture uncertainty in model parameters. Prediction intervals of
Kaplan-Meier estimates and hazard ratio of treatment effect can be further
calculated using simulated survival data.

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
