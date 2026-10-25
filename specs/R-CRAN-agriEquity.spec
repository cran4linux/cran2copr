%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agriEquity
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Equity and Sustainability Assessment of Agricultural Subsidies

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
An integrated framework for evaluating whether agricultural support
measures reach smallholders, women farmers and resource-poor regions, and
at what productivity and environmental cost. It provides survey-weighted
benefit incidence analysis by landholding class, gender, region or income
quantile; concentration, Kakwani and Reynolds-Smolensky progressivity
measures (Kakwani, 1977) <doi:10.2307/2230485> with bootstrap confidence
intervals; multi-dimensional equity scorecards with parity ratios and
Theil decomposition of benefit inequality; effects of subsidies on income
inequality and Foster-Greer-Thorbecke poverty (Foster, Greer and
Thorbecke, 1984) <doi:10.2307/1913475>; budget-neutral reallocation of a
subsidy budget under alternative allocation rules, including a
welfare-optimal allocation that combines diminishing productivity returns,
Atkinson (1970) <doi:10.1016/0022-0531(70)90039-6> inequality aversion and
environmental damage costs; and productivity-equity-sustainability
trade-off frontiers. Simulated farm-household data illustrate the
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
