%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetSimR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Actuarial Functions for Non-Life Insurance Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-future >= 1.17.0
BuildRequires:    R-CRAN-bslib >= 0.9.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-future >= 1.17.0
Requires:         R-CRAN-bslib >= 0.9.0
Requires:         R-CRAN-base64enc 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Assists actuaries and other insurance modellers in pricing, reserving and
capital modelling for non-life insurance and reinsurance modelling.
Provides functions that help model excess levels, capping and pure
Incurred but not reported claims (pure IBNR). Includes capped mean,
exposure curves and increased limit factor curves (ILFs) for LogNormal,
Gamma, Pareto, Sliced LogNormal-Pareto and Sliced Gamma-Pareto
distributions. Includes mean, probability density function (pdf),
cumulative probability function (cdf) and inverse cumulative probability
function for Sliced LogNormal-Pareto and Sliced Gamma-Pareto
distributions. Includes calculating pure IBNR exposure with LogNormal and
Gamma distribution for reporting delay. Includes three 'shiny' tools, one
to simulate insurance claims applying reinsurance structures, fit
generalised linear models and fit claims frequency or severity
distributions. Methods used in the package refer to Free for All by
Yiannis Parizas (2023) <https://www.theactuary.com/2023/03/02/free-all>;
Escaping the triangle by Yiannis Parizas (2019)
<https://www.theactuary.com/features/2019/06/2019/06/05/escaping-triangle>;
Take to excess by Yiannis Parizas (2019)
<https://www.theactuary.com/features/2019/03/2019/03/06/taken-excess>.

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
