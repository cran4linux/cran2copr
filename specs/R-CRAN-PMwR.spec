%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PMwR
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Portfolio Management with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-NMOF 
BuildRequires:    R-CRAN-datetimeutils 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-orgutils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-textutils 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-NMOF 
Requires:         R-CRAN-datetimeutils 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-orgutils 
Requires:         R-parallel 
Requires:         R-CRAN-textutils 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Tools for the practical management of financial portfolios: backtesting
investment and trading strategies, computing profit/loss and returns,
analysing trades, handling lists of transactions, reporting, and more.
The package provides a small set of reliable, efficient and convenient
tools for processing and analysing trade/portfolio data.  The manual
provides all the details; it is available from
<https://enricoschumann.net/R/packages/PMwR/manual/PMwR.html>. Examples
and descriptions of new features are provided at
<https://enricoschumann.net/notes/PMwR/>.

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
