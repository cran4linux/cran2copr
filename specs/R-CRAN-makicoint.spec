%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  makicoint
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Maki Cointegration Test with Multiple Structural Breaks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements the Maki (2012) <doi:10.1016/j.econmod.2012.04.022>
residual-based test for cointegration allowing for an unknown number of
structural breaks. Breaks are located by a sequential procedure and the
cointegrating residual is tested for a unit root with an augmented
Dickey-Fuller (ADF) regression; the test statistic is the minimum ADF
t-statistic over all candidate breaks. Four model specifications are
supported (level shift, level shift with trend, regime shift, and regime
shift with trend) and one to four regressors. The default engine
reproduces the original 'GAUSS' / 'tspdlib' implementation, with an
optional break rule following Maki (2012, Steps 2 and 4). The test runs
for any feasible number of breaks; beyond the five tabulated by Maki,
critical values can be simulated by his Monte-Carlo design. A two-panel
diagnostic plot is provided via 'ggplot2'.

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
