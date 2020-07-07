%global packname  muRL
%global packver   0.1-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.12
Release:          3%{?dist}
Summary:          Mailmerge using R, LaTeX, and the Web

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-stringr 
Requires:         R-graphics 

%description
Provides mailmerge methods for reading spreadsheets of addresses and other
relevant information to create standardized but customizable letters.
Provides a method for mapping US ZIP codes, including those of letter
recipients.  Provides a method for parsing and processing html code from
online job postings of the American Political Science Association.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
