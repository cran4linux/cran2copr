%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cjbart
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Heterogeneous Effects Analysis of Conjoint Experiments

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForestSRC >= 3.2.2
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-randomForestSRC >= 3.2.2
Requires:         R-CRAN-BART 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 

%description
A tool for analyzing conjoint experiments using Bayesian Additive
Regression Trees ('BART'), a machine learning method developed by Chipman,
George and McCulloch (2010) <doi:10.1214/09-AOAS285>. This tool focuses
specifically on estimating, identifying, and visualizing the heterogeneity
within marginal component effects, at the observation- and
individual-level. It uses a variable importance measure ('VIMP') with
delete-d jackknife variance estimation, following Ishwaran and Lu (2019)
<doi:10.1002/sim.7803>, to obtain bias-corrected estimates of which
variables drive heterogeneity in the predicted individual-level effects.

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
