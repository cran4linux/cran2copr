%global packname  WikidataQueryServiceR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          API Client Library for 'Wikidata Query Service'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-WikipediR >= 1.5.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-rex >= 1.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ratelimitr >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-WikipediR >= 1.5.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-rex >= 1.2.0
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ratelimitr >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.4

%description
An API client for the 'Wikidata Query Service'
<https://query.wikidata.org/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
