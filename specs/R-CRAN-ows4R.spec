%global packname  ows4R
%global packver   0.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Interface to OGC Web-Services (OWS)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.96.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-geometa 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-XML >= 3.96.1.1
Requires:         R-methods 
Requires:         R-CRAN-geometa 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rgdal 

%description
Provides an Interface to Web-Services defined as standards by the Open
Geospatial Consortium (OGC), including Web Feature Service (WFS) for
vector data, Catalogue Service (CSW) for ISO/OGC metadata and associated
standards such as the common web-service specification (OWS) and OGC
Filter Encoding. The long-term purpose is to add support for additional
OGC service standards such as Web Coverage Service (WCS) and Web
Processing Service (WPS).

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
