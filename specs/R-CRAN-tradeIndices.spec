%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tradeIndices
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          International Trade Intensity, Openness and Diversification Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Calculates commonly used indicators for empirical international trade
analysis from user-supplied data. Measures include trade openness,
bilateral export and import intensity, the Herfindahl-Hirschman
concentration index, normalized and entropy-based diversification,
structural diversification relative to a benchmark, export similarity,
trade complementarity, revealed comparative advantage, and intra-industry
trade. Functions are vectorized where appropriate, validate economically
meaningful inputs, and require no external data service. The definition of
trade openness follows the World Bank indicator metadata
<https://data.worldbank.org/indicator/NE.TRD.GNFS.ZS>. Methodological
background for several trade indicators is provided by the World Bank's
World Integrated Trade Solution
<https://wits.worldbank.org/wits/wits/witshelp/Content/Utilities/e1.trade_indicators.htm>
and the World Trade Organization (2012, ISBN:9789287038128).

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
