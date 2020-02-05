%global packname  importinegi
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Download and Manage Open Data from INEGI

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-data.table 
Requires:         R-foreign 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-data.table 

%description
Download and manage data sets of statistical projects and geographic data
created by Instituto Nacional de Estadistica y Geografia (INEGI). See
<https://www.inegi.org.mx/>.

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
%{rlibdir}/%{packname}/INDEX
