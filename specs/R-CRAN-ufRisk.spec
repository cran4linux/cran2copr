%global __brp_check_rpaths %{nil}
%global packname  ufRisk
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Risk Measure Calculation in Financial TS

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-esemifar 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-smoots 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-esemifar 
Requires:         R-CRAN-fracdiff 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-smoots 
Requires:         R-stats 
Requires:         R-utils 

%description
Enables the user to calculate Value at Risk (VaR) and Expected Shortfall
(ES) by means of various parametric and semiparametric GARCH-type models.
For the latter the estimation of the nonparametric scale function is
carried out by means of a data-driven smoothing approach. Model quality,
in terms of forecasting VaR and ES, can be assessed by means of various
backtesting methods such as the traffic light test for VaR and a newly
developed traffic light test for ES. The approaches implemented in this
package are described in e.g. Feng Y., Beran J., Letmathe S. and Ghosh S.
(2020) <https://ideas.repec.org/p/pdn/ciepap/137.html> as well as Letmathe
S., Feng Y. and Uhde A. (2021)
<https://ideas.repec.org/p/pdn/ciepap/141.html>.

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
