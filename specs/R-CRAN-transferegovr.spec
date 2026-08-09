%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  transferegovr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access the 'TransfereGov' Open Data APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a modern interface to the open data application programming
interfaces of the Brazilian federal government's 'TransfereGov' platform
(<https://www.gov.br/transferegov/pt-br/ferramentas-gestao/dados-abertos>).
Covers the special transfers, fund-to-fund transfers, and decentralized
credit ('TED') modules, which together publish forty-eight tables on
action plans, programs, budget commitments, financial execution,
management reports, and payment orders. The APIs are built on 'PostgREST',
so the package exposes its filtering, column selection, and ordering
operators directly, and returns tidy tibbles with types taken from the
published schema. Automatic pagination, request throttling, retries with
exponential backoff, and an optional response cache are included.

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
