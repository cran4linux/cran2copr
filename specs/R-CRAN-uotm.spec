%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  uotm
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Uncertainty of Time Series Model Selection Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hash 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hash 

%description
We propose a new procedure, called model uncertainty variance, which can
quantify the uncertainty of model selection on Autoregressive Moving
Average models. The model uncertainty variance not pay attention to the
accuracy of prediction, but focus on model selection uncertainty and
providing more information of the model selection results. And to estimate
the model measures, we propose an simplify and faster algorithm based on
bootstrap method, which is proven to be effective and feasible by
Monte-Carlo simulation. At the same time, we also made some optimizations
and adjustments to the Model Confidence Bounds algorithm, so that it can
be applied to the time series model selection method. The consistency of
the algorithm result is also verified by Monte-Carlo simulation. We
propose a new procedure, called model uncertainty variance, which can
quantify the uncertainty of model selection on Autoregressive Moving
Average models. The model uncertainty variance focuses on model selection
uncertainty and providing more information of the model selection results.
To estimate the model uncertainty variance, we propose an simplified and
faster algorithm based on bootstrap method, which is proven to be
effective and feasible by Monte-Carlo simulation. At the same time, we
also made some optimizations and adjustments to the Model Confidence
Bounds algorithm, so that it can be applied to the time series model
selection method. The consistency of the algorithm result is also verified
by Monte-Carlo simulation. Please see Li,Y., Luo,Y., Ferrari,D., Hu,X. and
Qin,Y. (2019) Model Confidence Bounds for Variable Selection. Biometrics,
75:392-403.<DOI:10.1111/biom.13024> for more information.

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
