%global packname  rcrossref
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client for Various 'CrossRef' 'APIs'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-crul >= 0.7.4
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-stats 
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-crul >= 0.7.4
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-DT 
Requires:         R-stats 

%description
Client for various 'CrossRef' 'APIs', including 'metadata' search with
their old and newer search 'APIs', get 'citations' in various formats
(including 'bibtex', 'citeproc-json', 'rdf-xml', etc.), convert 'DOIs' to
'PMIDs', and 'vice versa', get citations for 'DOIs', and get links to full
text of articles when available.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
