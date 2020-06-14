%global packname  rapport
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          A Report Templating System

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rapportools 
BuildRequires:    R-CRAN-pander 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rapportools 
Requires:         R-CRAN-pander 

%description
Facilitating the creation of reproducible statistical report templates.
Once created, rapport templates can be exported to various external
formats (HTML, LaTeX, PDF, ODT etc.) with pandoc as the converter backend.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/includes
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
