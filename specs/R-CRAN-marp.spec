%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  marp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Averaged Renewal Process

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-stats 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-VGAM 

%description
To implement a model-averaging approach with different renewal models,
with a primary focus on forecasting large earthquakes. Based on six
renewal models (i.e., Poisson, Gamma, Log-Logistics, Weibull, Log-Normal
and BPT), model-averaged point estimates are calculated using AIC (or BIC)
weights. Additionally, both percentile and studentized bootstrapped
model-averaged confidence intervals are constructed. In comparison, point
and interval estimation from the individual or "best" model (determined
via model selection) can be retrieved.

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
