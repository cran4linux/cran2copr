%global packname  refimpact
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          API Wrapper for the UK REF 2014 Impact Case Studies Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.1
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-curl >= 2.1
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-xml2 >= 1.0.0

%description
Provides wrapper functions around the UK Research Excellence Framework
2014 Impact Case Studies Database API <http://impact.ref.ac.uk/>. The
database contains relevant publication and research metadata about each
case study as well as several paragraphs of text from the case study
submissions. Case studies in the database are licenced under a CC-BY 4.0
licence <http://creativecommons.org/licenses/by/4.0/legalcode>.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
