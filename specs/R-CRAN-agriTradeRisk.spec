%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agriTradeRisk
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Agricultural Export Competitiveness and Risk Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
An integrated and reproducible workflow for analysing the competitiveness
and risk of agricultural and horticultural exports. It measures
destination and product concentration (Herfindahl-Hirschman, entropy and
equivalent-number indices), revealed comparative advantage (Balassa, 1965)
<doi:10.1111/j.1467-9957.1965.tb00050.x> and its symmetric form, relative
unit values, and constant market share decomposition of export growth. It
tests vertical price transmission between export and domestic prices with
Engle-Granger cointegration (Engle and Granger, 1987)
<doi:10.2307/1913236> using MacKinnon (2010) critical values and symmetric
or asymmetric error correction models. It quantifies exchange-rate
exposure of a multi-currency export portfolio (volatility, diversification
ratio, risk contributions and value at risk), screens destination markets
with composite entry-risk scores, and identifies risk-efficient
destination mixes by mean-variance portfolio optimisation (Markowitz,
1952) <doi:10.2307/2975974>. Simulated example data for Indian mango,
grape, pomegranate and processed horticultural exports illustrate the
workflow.

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
