%global packname  HGNChelper
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Identify and Correct Invalid HGNC Human Gene Symbols and MGIMouse Gene Symbols

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-utils 

%description
Contains functions for identifying and correcting HGNC human gene symbols
and MGI mouse gene symbols which have been converted to date format by
Excel, withdrawn, or aliased. Also contains functions for reversibly
converting between HGNC symbols and valid R names.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
