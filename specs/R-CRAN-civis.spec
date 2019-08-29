%global packname  civis
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          R Client for the 'Civis data science API'

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.8.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-future >= 1.8.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-memoise 
Requires:         R-stats 
Requires:         R-utils 

%description
A convenient interface for making requests directly to the 'Civis data
science API' <https://www.civisanalytics.com/platform/>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/civis_ml_brandable.rds
%doc %{rlibdir}/%{packname}/civis_ml_err.rds
%doc %{rlibdir}/%{packname}/civis_ml_oos.rds
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
