%global packname  easySdcTable
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Easy Interface to the Statistical Disclosure Control Package'sdcTable'

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sdcTable 
BuildRequires:    R-CRAN-SSBtools 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-sdcTable 
Requires:         R-CRAN-SSBtools 
Requires:         R-CRAN-shiny 

%description
The main function, ProtectTable(), performs table suppression according to
a frequency rule with a data set as the only required input. Within this
function, protectTable(), protectLinkedTables() or runArgusBatchFile() in
package 'sdcTable' is called. Lists of level-hierarchy (parameter
'dimList') and other required input to these functions are created
automatically. The function, PTgui(), starts a graphical user interface
based on the shiny package.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
