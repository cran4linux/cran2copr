%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ardldml
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bounds Testing for Cointegration with Many Persistent Controls

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
An implementation of the DML-Bounds procedure of Villena (2026)
<doi:10.2139/ssrn.6472826> for testing cointegration in data-rich
time-series settings. The Autoregressive Distributed Lag (ARDL) bounds
test of Pesaran, Shin and Smith (2001) <doi:10.1002/jae.616> avoids
pretesting the integration order of the regressors but is not designed for
a high-dimensional conditioning set. Residualising the lagged levels
against persistent controls can absorb stochastic trends and thereby
change the finite-sample null distribution, so what governs the null is
the effective number of stochastic trends surviving residualisation rather
than the integration order of the original regressors. The procedure
combines h-block cross-fitting, a balanced nuisance projection in the
Double Machine Learning (DML) style of Chernozhukov and others (2018)
<doi:10.1111/ectj.12097>, adaptive weighting after Zou (2006)
<doi:10.1198/016214506000000735>, and a restricted system wild bootstrap
that regenerates the dependent variable and the focal regressor jointly.
No critical-value table is shipped: the classical bracket is regenerated
by simulation and the operational critical value is bootstrapped. A
trend-absorption diagnostic and a penalty-sensitivity sweep report whether
a verdict survives a change of conditioning set. Monthly United States
macroeconomic series from the 'FRED-MD' database of McCracken and Ng
(2016) <doi:10.1080/07350015.2015.1086655> are bundled so every example
runs offline.

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
