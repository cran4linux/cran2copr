%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stockAnalyst
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Equity Valuation using Methods of Fundamental Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Methods of Fundamental Analysis for Valuation of Equity included here
serve as a quick reference for undergraduate courses on Stock Valuation
and Chartered Financial Analyst Levels 1 and 2 Readings on Equity
Valuation. Jerald E. Pinto (“Equity Asset Valuation (4th Edition)”, 2020,
ISBN: 9781119628194). Chartered Financial Analyst Institute ("Chartered
Financial Analyst Program Curriculum 2020 Level I Volumes 1-6. (Vol. 4,
pp. 445-491)", 2019, ISBN: 9781119593577). Chartered Financial Analyst
Institute ("Chartered Financial Analyst Program Curriculum 2020 Level II
Volumes 1-6. (Vol. 4, pp. 197-447)", 2019, ISBN: 9781119593614).

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
