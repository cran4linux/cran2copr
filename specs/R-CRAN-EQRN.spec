%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EQRN
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Quantile Regression Neural Networks for Risk Forecasting

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-utils 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-torch 
Requires:         R-utils 

%description
This framework enables forecasting and extrapolating measures of
conditional risk (e.g. of extreme or unprecedented events), including
quantiles and exceedance probabilities, using extreme value statistics and
flexible neural network architectures. It allows for capturing complex
multivariate dependencies, including dependencies between observations,
such as sequential dependence (time-series). The methodology was
introduced in Pasche and Engelke (2024) <doi:10.1214/24-AOAS1907> (also
available in preprint: Pasche and Engelke (2022)
<doi:10.48550/arXiv.2208.07590>).

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
