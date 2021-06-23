%global __brp_check_rpaths %{nil}
%global packname  readxl
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Read Excel Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-tibble >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-tibble >= 1.3.1
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-cellranger 
Requires:         R-utils 

%description
Import excel files into R. Supports '.xls' via the embedded 'libxls' C
library <https://github.com/libxls/libxls> and '.xlsx' via the embedded
'RapidXML' C++ library <http://rapidxml.sourceforge.net>.  Works on
Windows, Mac and Linux without external dependencies.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
