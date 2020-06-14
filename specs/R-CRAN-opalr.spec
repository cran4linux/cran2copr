%global packname  opalr
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          2%{?dist}
Summary:          'Opal' Data Repository Client and 'DataSHIELD' Utils

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-progress 

%description
Data integration Web application for biobanks by 'OBiBa'. 'Opal' is the
core database application for biobanks. Participant data, once collected
from any data source, must be integrated and stored in a central data
repository under a uniform model. 'Opal' is such a central repository. It
can import, process, validate, query, analyze, report, and export data.
'Opal' is typically used in a research center to analyze the data acquired
at assessment centres. Its ultimate purpose is to achieve seamless
data-sharing among biobanks. This 'Opal' client allows to interact with
'Opal' web services and to perform operations on the R server side.
'DataSHIELD' administration tools are also provided.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/reports
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
