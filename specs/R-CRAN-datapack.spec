%global packname  datapack
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          A Flexible Container to Transport and Manipulate Data andAssociated Resources

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-redland 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-CRAN-redland 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-uuid 

%description
Provides a flexible container to transport and manipulate complex sets of
data. These data may consist of multiple data files and associated meta
data and ancillary files. Individual data objects have associated system
level meta data, and data files are linked together using the OAI-ORE
standard resource map which describes the relationships between the files.
The OAI- ORE standard is described at <https://www.openarchives.org/ore>.
Data packages can be serialized and transported as structured files that
have been created following the BagIt specification. The BagIt
specification is described at
<https://tools.ietf.org/html/draft-kunze-bagit-08>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/testfiles
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
