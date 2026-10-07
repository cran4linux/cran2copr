%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMGCR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture Cure Rate Models with Flexible Link Functions via the EM Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-graphics 

%description
Fits mixture cure rate models by the Expectation-Maximization (EM)
algorithm. The incidence component (the probability of being uncured)
accepts the logit, probit, cauchit, power logit and reversed power logit
link functions, and the latency component accepts the exponential,
Rayleigh, Weibull, log-normal, log-logistic and inverse Gaussian
distributions. The package provides parameter estimates with standard
errors, simulation of data from the model, and diagnostic tools based on
residuals and simulated envelopes. The methods build on Berkson and Gage
(1952) <doi:10.2307/2281318>, Dempster, Laird and Rubin (1977)
<doi:10.1111/j.2517-6161.1977.tb01600.x> and Bazán, Torres-Avilés, Suzuki
and Louzada (2017) <doi:10.1002/asmb.2215>.

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
