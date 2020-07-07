%global packname  originr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          Fetch Species Origin Data from the Web

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-taxize >= 0.9.0
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-taxize >= 0.9.0
Requires:         R-CRAN-crul 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xml2 

%description
Get species origin data (whether species is native/invasive) from the
following sources on the web: Encyclopedia of Life (<http://eol.org>),
Flora 'Europaea' (<http://rbg-web2.rbge.org.uk/FE/fe.html>), Global
Invasive Species Database (<http://www.iucngisd.org/gisd>), the Native
Species Resolver (<https://bien.nceas.ucsb.edu/bien/tools/nsr/>),
Integrated Taxonomic Information Service (<https://www.itis.gov/>), and
Global Register of Introduced and Invasive Species
(<http://www.griis.org/>).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
