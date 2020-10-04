%global packname  pxweb
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          3%{?dist}%{?buildtag}
Summary:          R Interface to PXWEB APIs

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr >= 1.1
Requires:         R-methods 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-jsonlite 

%description
Generic interface for the PX-Web/PC-Axis API. The PX-Web/PC-Axis API is
used by organizations such as Statistics Sweden and Statistics Finland to
disseminate data. The R package can interact with all PX-Web/PC-Axis APIs
to fetch information about the data hierarchy, extract metadata and
extract and parse statistics to R data.frame format. PX-Web is a solution
to disseminate PC-Axis data files in dynamic tables on the web. Since 2013
PX-Web contains an API to disseminate PC-Axis files.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/extras
%{rlibdir}/%{packname}/INDEX
