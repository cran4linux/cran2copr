%global __brp_check_rpaths %{nil}
%global packname  rbace
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          'Bielefeld' Academic Search Engine ('BASE') Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 

%description
Interface to the API for the 'Bielefeld' Academic Search Engine ('BASE')
(<https://www.base-search.net/>). 'BASE' is a search engine for more than
150 million scholarly documents from more than 7000 sources. Methods are
provided for searching for documents, as well as getting information on
higher level groupings of documents: collections and repositories within
collections. Search includes faceting, so you can get a high level
overview of number of documents across a given variable (e.g., year).
'BASE' asks users to respect a rate limit, but does not enforce it
themselves; we enforce that rate limit.

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
