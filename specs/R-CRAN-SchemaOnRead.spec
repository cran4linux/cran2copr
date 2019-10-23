%global packname  SchemaOnRead
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Automated Schema on Read

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-readODS >= 1.4
BuildRequires:    R-CRAN-caTools >= 1.17.1
BuildRequires:    R-CRAN-ncdf4 >= 1.14
BuildRequires:    R-CRAN-network >= 1.12
BuildRequires:    R-foreign >= 0.8.66
BuildRequires:    R-CRAN-haven >= 0.2.0
BuildRequires:    R-CRAN-tiff >= 0.1.5
BuildRequires:    R-CRAN-readbitmap >= 0.1.4
BuildRequires:    R-CRAN-xml2 >= 0.1.2
BuildRequires:    R-CRAN-readxl >= 0.1.0
Requires:         R-CRAN-readODS >= 1.4
Requires:         R-CRAN-caTools >= 1.17.1
Requires:         R-CRAN-ncdf4 >= 1.14
Requires:         R-CRAN-network >= 1.12
Requires:         R-foreign >= 0.8.66
Requires:         R-CRAN-haven >= 0.2.0
Requires:         R-CRAN-tiff >= 0.1.5
Requires:         R-CRAN-readbitmap >= 0.1.4
Requires:         R-CRAN-xml2 >= 0.1.2
Requires:         R-CRAN-readxl >= 0.1.0

%description
Provides schema-on-read tools including a single function call (e.g.,
schemaOnRead('filename')) that reads text ('TXT'), comma separated value
('CSV'), raster image ('BMP', 'PNG', 'GIF', 'TIFF', and 'JPG'), R data
('RDS'), HDF5 ('H5'), NetCDF ('CS'), spreadsheet ('XLS', 'XLSX', 'ODS',
and 'DIF'), Weka Attribute-Relation File Format ('ARFF'), Epi Info
('REC'), SPSS ('SAV'), Systat ('SYS'), and Stata ('DTA') files. It also
recursively reads folders (e.g., schemaOnRead('folder')), returning a
nested list of the contained elements.

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
%doc %{rlibdir}/%{packname}/Data.xyz
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
