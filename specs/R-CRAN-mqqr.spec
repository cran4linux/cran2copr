%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mqqr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Quantile-on-Quantile Regression

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
Implements Multivariate Quantile-on-Quantile Regression (m-QQR) of Sinha,
Ghosh, Hussain, Nguyen and Das (2023) <doi:10.1016/j.eneco.2023.107021>,
extending the bivariate Quantile-on-Quantile regression of Sim and Zhou
(2015) <doi:10.1016/j.jbankfin.2015.01.013> to include exogenous
moderators and controls with optional interaction terms. For each pair of
quantile levels (theta of the response and tau of the regressor) the
package fits a locally-weighted quantile regression of y on the principal
regressor x, a lagged dependent variable, moderators Z and the x*Z
interaction terms, using Gaussian kernel weights on the empirical
cumulative distribution function (CDF) distance. Bootstrap standard errors
and Koenker-Machado pseudo R-squared are reported. Visualisations include
'MATLAB'-style 'Parula' and 'Jet' 3D surfaces, heatmaps and contour plots
through 'plotly'.

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
