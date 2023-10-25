%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetSimR
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Actuarial Functions for Non-Life Insurance Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-future 
Requires:         R-methods 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-RODBC 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-shinyWidgets 

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
Gamma distribution for reporting delay. Includes three shiny tools, one to
simulate insurance claims applying reinsurance structures, fit generalised
linear models and fit claims frequency or severity distributions. Methods
used in the package refer to Free for All by Yiannis Parizas (2023)
<https://www.theactuary.com/2023/03/02/free-all>; Escaping the triangle by
Yiannis Parizas (2019)
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
