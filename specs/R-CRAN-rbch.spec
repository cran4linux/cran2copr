%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbch
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Extraction and Analysis of Data from the Bitcoin Cash (BCH) Blockchain

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-rjson 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-rjson 

%description
Issues RPC-JSON calls to 'bitcoind', the daemon of Bitcoin Cash (BCH), to
extract transaction data from the blockchain. BCH is a fork of Bitcoin
that permits a greater number of transactions per second. A BCH daemon is
available under an MIT license from the Bitcoin Unlimited website
<https://www.bitcoinunlimited.info>.

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
