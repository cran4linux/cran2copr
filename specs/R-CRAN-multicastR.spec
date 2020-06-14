%global packname  multicastR
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          2%{?dist}
Summary:          A Companion to the Multi-CAST Collection

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.0
BuildRequires:    R-CRAN-curl >= 3.3
BuildRequires:    R-CRAN-xtable >= 1.8.0
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-stringi >= 1.1.0
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-gsubfn >= 0.7
Requires:         R-CRAN-XML >= 3.98.0
Requires:         R-CRAN-curl >= 3.3
Requires:         R-CRAN-xtable >= 1.8.0
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-stringi >= 1.1.0
Requires:         R-CRAN-xml2 >= 1.1.0
Requires:         R-CRAN-gsubfn >= 0.7

%description
Provides a basic interface for accessing annotation data from the
Multi-CAST collection, a database of spoken natural language texts edited
by Geoffrey Haig and Stefan Schnell. The collection draws from a diverse
set of languages and has been annotated across multiple levels. Annotation
data is downloaded on request from the servers of the University of
Bamberg. See the Multi-CAST website
<https://multicast.aspra.uni-bamberg.de/> for more information and a list
of related publications.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
