%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  atRisk
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          At-Risk

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-dfoptim 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-dfoptim 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 

%description
The at-Risk (aR) approach is based on a two-step parametric estimation
procedure that allows to forecast the full conditional distribution of an
economic variable at a given horizon, as a function of a set of factors.
These density forecasts are then be used to produce coherent forecasts for
any downside risk measure, e.g., value-at-risk, expected shortfall,
downside entropy. Initially introduced by Adrian et al. (2019)
<doi:10.1257/aer.20161923> to reveal the vulnerability of economic growth
to financial conditions, the aR approach is currently extensively used by
international financial institutions to provide Value-at-Risk (VaR) type
forecasts for GDP growth (Growth-at-Risk) or inflation
(Inflation-at-Risk). This package provides methods for estimating these
models. Datasets for the US and the Eurozone are available to allow
testing of the Adrian et al. (2019) model. This package constitutes a
useful toolbox (data and functions) for private practitioners, scholars as
well as policymakers.

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
