%global packname  nlmeU
%global packver   0.70-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.70.3
Release:          2%{?dist}
Summary:          Datasets and utility functions enhancing functionality of nlmepackage.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.2
Requires:         R-core >= 2.14.2
BuildArch:        noarch
BuildRequires:    R-nlme 
Requires:         R-nlme 

%description
nlmeU: Datasets and utility functions enhancing functionality of nlme
package. Datasets, functions and scripts are described in book titled
'Linear Mixed-Effects Models: A Step-by-Step Approach' by Galecki and
Burzykowski (2013). Package is under development.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/csvData
%doc %{rlibdir}/%{packname}/scriptsR2.15.0
%doc %{rlibdir}/%{packname}/testsR2.15.0
%{rlibdir}/%{packname}/INDEX
