%global packname  DSOpal
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          'DataSHIELD' Implementation for 'Opal'

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-opalr >= 1.4
BuildRequires:    R-CRAN-DSI >= 1.1
BuildRequires:    R-methods 
Requires:         R-CRAN-opalr >= 1.4
Requires:         R-CRAN-DSI >= 1.1
Requires:         R-methods 

%description
'DataSHIELD' is an infrastructure and series of R packages that enables
the remote and 'non-disclosive' analysis of sensitive research data. This
package is the 'DataSHIELD' interface implementation for 'Opal', which is
the data integration application for biobanks by 'OBiBa'. Participant
data, once collected from any data source, must be integrated and stored
in a central data repository under a uniform model. 'Opal' is such a
central repository. It can import, process, validate, query, analyze,
report, and export data. 'Opal' is the reference implementation of the
'DataSHIELD' infrastructure.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
