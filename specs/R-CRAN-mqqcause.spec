%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mqqcause
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Quantile-on-Quantile Granger Causality

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.0
BuildRequires:    R-CRAN-plotly >= 4.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-quantreg >= 5.0
Requires:         R-CRAN-plotly >= 4.0.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Implements bivariate and Multivariate Quantile-on-Quantile Granger
causality tests building on the Quantile-on-Quantile regression framework
of Sim and Zhou (2015) <doi:10.1016/j.jbankfin.2015.01.013> and the
quantile Granger causality test of Troster (2018)
<doi:10.1080/07474938.2016.1172400>. The bivariate test estimates the
local-linear slope in the quantile regression of y_t on lagged x_t with
lagged y_t as control, using Gaussian kernel weights, and tests it against
zero by paired bootstrap. The multivariate (conditional) test additionally
conditions on a set of moderators Z and optional x times Z interaction
terms, in the spirit of Sinha, Ghosh, Hussain, Nguyen and Das (2023)
<doi:10.1016/j.eneco.2023.107021>. A Sup-Wald summary across the quantile
grid is also provided. Heatmaps and 3D surfaces default to the 'MATLAB'
'Parula' colour map.

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
