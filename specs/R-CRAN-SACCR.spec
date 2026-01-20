%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SACCR
%global packver   3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4
Release:          1%{?dist}%{?buildtag}
Summary:          SA Counterparty Credit Risk under CRR2

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Trading 
Requires:         R-methods 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-Trading 

%description
Computes the Exposure-At-Default based on the standardized approach of
CRR2 (SA-CCR). The simplified version of SA-CCR has been included, as well
as the OEM methodology. Multiple trade types of all the five major asset
classes are being supported including the Other Exposure and, given the
inheritance- based structure of the application, the addition of further
trade types is straightforward. The application returns a list of trees
per Counterparty and CSA after automatically separating the trades based
on the Counterparty, the CSAs, the hedging sets, the netting sets and the
risk factors. The basis and volatility transactions are also identified
and treated in specific hedging sets whereby the corresponding penalty
factors are applied. All the examples appearing on the regulatory papers
(both for the margined and the unmargined workflow) have been implemented
including the latest CRR2 developments.

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
