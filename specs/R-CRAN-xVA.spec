%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xVA
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Credit Risk Valuation Adjustments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SACCR 
BuildRequires:    R-CRAN-Trading 
BuildRequires:    R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-SACCR 
Requires:         R-CRAN-Trading 
Requires:         R-CRAN-data.table 

%description
Calculates a number of valuation adjustments including CVA, DVA, FBA, FCA,
MVA and KVA. A two-way margin agreement has been implemented. For the KVA
calculation four regulatory frameworks are supported: CEM, (simplified)
SA-CCR, OEM and IMM. The probability of default is implied through the
credit spreads curve. The package supports an exposure calculation based
on SA-CCR which includes several trade types and a simulated path which is
currently available only for Interest Rate Swaps. The latest regulatory
capital charge methodologies have been implementing including BA-CVA &
SA-CVA.

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
