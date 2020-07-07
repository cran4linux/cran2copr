%global packname  xlsx
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          3%{?dist}
Summary:          Read, Write, Format Excel 2007 and Excel 97/2000/XP/2003 Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-xlsxjars 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-xlsxjars 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Provide R functions to read/write/format Excel 2007 and Excel
97/2000/XP/2003 file formats.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
