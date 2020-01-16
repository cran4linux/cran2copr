%global packname  phylocomr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Interface to 'Phylocom'

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-sys >= 3.2
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-sys >= 3.2
Requires:         R-CRAN-tibble 

%description
Interface to 'Phylocom' (<http://phylodiversity.net/phylocom/>), a library
for analysis of 'phylogenetic' community structure and character
evolution. Includes low level methods for interacting with the three
executables, as well as higher level interfaces for methods like 'aot',
'ecovolve', 'bladj', 'phylomatic', and more.

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
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/COPYRIGHT
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%doc %{rlibdir}/%{packname}/bin
