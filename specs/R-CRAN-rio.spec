%global packname  rio
%global packver   0.5.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.16
Release:          2%{?dist}
Summary:          A Swiss-Army Knife for Data I/O

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-haven >= 1.1.0
BuildRequires:    R-CRAN-curl >= 0.6
BuildRequires:    R-CRAN-readxl >= 0.1.1
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-haven >= 1.1.0
Requires:         R-CRAN-curl >= 0.6
Requires:         R-CRAN-readxl >= 0.1.1
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-foreign 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-tibble 

%description
Streamlined data import and export by making assumptions that the user is
probably willing to make: 'import()' and 'export()' determine the data
structure from the file extension, reasonable defaults are used for data
import and export (e.g., 'stringsAsFactors=FALSE'), web-based import is
natively supported (including from SSL/HTTPS), compressed files can be
read directly without explicit decompression, and fast import packages are
used where appropriate. An additional convenience function, 'convert()',
provides a simple method for converting between file types.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
