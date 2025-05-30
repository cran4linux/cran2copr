%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  morseDR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference of Binary, Count and Continuous Data in Toxicology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-rjags 
Requires:         R-stats 

%description
Advanced methods for a valuable quantitative environmental risk assessment
using Bayesian inference of several type of toxicological data. 'binary'
(e.g., survival, mobility), 'count' (e.g., reproduction) and 'continuous'
(e.g., growth as length, weight).  Estimation procedures can be used
without a deep knowledge of their underlying probabilistic model or
inference methods. Rather, they were designed to behave as well as
possible without requiring a user to provide values for some obscure
parameters. That said, models can also be used as a first step to tailor
new models for more specific situations.

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
