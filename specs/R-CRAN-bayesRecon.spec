%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesRecon
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Reconciliation via Conditioning

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve >= 5.6.18
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lpSolve >= 5.6.18
Requires:         R-stats 
Requires:         R-utils 

%description
Provides methods for probabilistic reconciliation of hierarchical
forecasts of time series. The available methods include analytical
Gaussian reconciliation (Corani et al., 2021)
<doi:10.1007/978-3-030-67664-3_13>, MCMC reconciliation of count time
series (Corani et al., 2024) <doi:10.1016/j.ijforecast.2023.04.003>,
Bottom-Up Importance Sampling (Zambon et al., 2024)
<doi:10.1007/s11222-023-10343-y>, methods for the reconciliation of mixed
hierarchies (Mix-Cond and TD-cond) (Zambon et al., 2024)
<https://proceedings.mlr.press/v244/zambon24a.html>.

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
