%global __brp_check_rpaths %{nil}
%global packname  oai
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          General Purpose 'Oai-PMH' Services Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-httr >= 1.2.0
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-httr >= 1.2.0
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-xml2 >= 1.0.0

%description
A general purpose client to work with any 'OAI-PMH' (Open Archives
Initiative Protocol for 'Metadata' Harvesting) service. The 'OAI-PMH'
protocol is described at
<http://www.openarchives.org/OAI/openarchivesprotocol.html>. Functions are
provided to work with the 'OAI-PMH' verbs: 'GetRecord', 'Identify',
'ListIdentifiers', 'ListMetadataFormats', 'ListRecords', and 'ListSets'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
