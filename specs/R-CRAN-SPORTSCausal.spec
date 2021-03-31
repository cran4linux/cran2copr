%global packname  SPORTSCausal
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spillover Time Series Causal Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CausalImpact 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-CausalImpact 
Requires:         R-CRAN-keras 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
A time series causal inference model for Randomized Controlled Trial (RCT)
under spillover effect. 'SPORTSCausal' (Spillover Time Series Causal
Inference) separates treatment effect and spillover effect from given
responses of experiment group and control group by predicting the response
without treatment. It reports both effects by fitting the Bayesian
Structural Time Series (BSTS) model based on 'CausalImpact', as described
in Brodersen et al. (2015) <doi:10.1214/14-AOAS788>.

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
