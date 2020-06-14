%global packname  finch
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Parse Darwin Core Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EML >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-hoardr >= 0.2.0
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-EML >= 2.0.0
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-hoardr >= 0.2.0
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-digest 

%description
Parse and create Darwin Core (<http://rs.tdwg.org/dwc/>) Simple and
Archives. Functionality includes reading and parsing all the files in a
Darwin Core Archive, including the datasets and metadata; read and parse
simple Darwin Core files; and validation of Darwin Core Archives.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/schemas
%{rlibdir}/%{packname}/INDEX
