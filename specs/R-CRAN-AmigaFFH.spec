%global packname  AmigaFFH
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Commodore Amiga File Format Handler

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tuneR >= 1.0
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-tuneR >= 1.0
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 

%description
Modern software often poorly support older file formats. This package
intends to handle many file formats that were native to the antiquated
Commodore Amiga machine. This package focuses on file types from the older
Amiga operating systems (<= 3.0). It will read and write specific file
formats and coerces them into more contemporary data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ilbm8lores.iff
%{rlibdir}/%{packname}/INDEX
