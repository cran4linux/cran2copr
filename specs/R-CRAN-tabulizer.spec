%global packname  tabulizer
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          Bindings for 'Tabula' PDF Table Extractor Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-tabulizerjars 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-png 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-tabulizerjars 
Requires:         R-tools 
Requires:         R-utils 

%description
Bindings for the 'Tabula' <http://tabula.technology/> 'Java' library,
which can extract tables from PDF documents. The 'tabulizerjars' package
<https://github.com/ropensci/tabulizerjars> provides versioned 'Java' .jar
files, including all dependencies, aligned to releases of 'Tabula'.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
