%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fable.bayesRecon
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Reconciliation in the 'fable' Framework

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-fabletools >= 0.7.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bayesRecon 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-fabletools >= 0.7.0
Requires:         R-stats 
Requires:         R-CRAN-bayesRecon 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-distributional 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-rlang 

%description
Implements the 'bayesRecon' probabilistic reconciliation methods within
the 'fable' framework for hierarchical time series forecasting. Bayesian
reconciliation (bayesRecon) methods are accessed via the 'reconcile' verb,
following 'fable' conventions. For methodological background, see Corani
et al. (2021) <doi:10.1007/978-3-030-67664-3_13>, Zambon et al. (2024a)
<doi:10.1007/s11222-023-10343-y>, Zambon et al. (2024b)
<https://proceedings.mlr.press/v244/zambon24a.html>, and Carrara et al.
(2025) <doi:10.48550/arXiv.2506.19554>.

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
