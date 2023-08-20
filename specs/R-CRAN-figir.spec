%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  figir
%global packver   0.1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Check Validity of FIGI, CUSIP, ISIN, SEDOL

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
With the functions in this package you can check the validity of the
following financial instrument identifiers: FIGI (Financial Instrument
Global Identifier <https://www.openfigi.com/about/figi>), CUSIP (Committee
on Uniform Security Identification Procedures
<https://www.cusip.com/identifiers.html#/CUSIP>), ISIN (International
Securities Identification Number
<https://www.cusip.com/identifiers.html#/ISIN>), SEDOL (Stock Exchange
Daily Official List
<https://www2.lseg.com/SEDOL-masterfile-service-tech-guide-v8.6>). You can
also calculate the FIGI checksum of 11-character strings, which can be
useful if you want to create your own FIGI identifiers.

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
