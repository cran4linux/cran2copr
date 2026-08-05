%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FinancialInstrument
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Financial Instrument Modeling Infrastructure

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.5
BuildRequires:    R-CRAN-quantmod >= 0.4.3
BuildRequires:    R-CRAN-xts >= 0.10.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-TTR 
Requires:         R-CRAN-zoo >= 1.7.5
Requires:         R-CRAN-quantmod >= 0.4.3
Requires:         R-CRAN-xts >= 0.10.0
Requires:         R-methods 
Requires:         R-CRAN-TTR 

%description
Provides infrastructure for defining, storing, and managing financial
instrument metadata independently of market data sources. Models
instrument identities, contract specifications, identifiers, and
relationships among financial instruments, including currencies, equities,
funds, bonds, futures, options, spreads, exchange rates, and synthetic
instruments. Supports reusable instrument definitions for research,
portfolio management, trading, and quantitative finance applications.

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
