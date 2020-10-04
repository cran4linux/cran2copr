%global packname  dataone
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          R Interface to the DataONE REST API

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.95.0.1
BuildRequires:    R-CRAN-datapack >= 1.3.0
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-XML >= 3.95.0.1
Requires:         R-CRAN-datapack >= 1.3.0
Requires:         R-CRAN-hash 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 

%description
Provides read and write access to data and metadata from the DataONE
network <https://www.dataone.org> of data repositories. Each DataONE
repository implements a consistent repository application programming
interface. Users call methods in R to access these remote repository
functions, such as methods to query the metadata catalog, get access to
metadata for particular data packages, and read the data objects from the
data repository. Users can also insert and update data objects on
repositories that support these methods.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/testfiles
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
