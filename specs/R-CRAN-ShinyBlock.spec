%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ShinyBlock
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Protocol Blockchain Simulator and Enterprise Ledger Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-jsonlite 

%description
An interactive framework for simulating blockchain protocols using a
hybrid 'R-Shiny' and 'Python' architecture. The package provides tools to
visualize peer-to-peer network maps, manage supply chain logistics
on-chain, and execute cross-border settlements via smart contract logic.
It leverages the 'reticulate' package to perform standardized
cryptographic operations, including 'SHA-256' hashing, 'Merkle' Tree
construction, and 'ECDSA' (Elliptic Curve Digital Signature Algorithm) key
generation. This tool is designed for pedagogical demonstration and rapid
prototyping of distributed ledger requirements.

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
