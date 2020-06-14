%global packname  plumber
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          2%{?dist}
Summary:          An API Generator for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.0.0
BuildRequires:    R-CRAN-httpuv >= 1.2.3
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
BuildRequires:    R-CRAN-stringi >= 0.3.0
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-R6 >= 2.0.0
Requires:         R-CRAN-httpuv >= 1.2.3
Requires:         R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-stringi >= 0.3.0
Requires:         R-CRAN-crayon 

%description
Gives the ability to automatically generate and serve an HTTP API from R
functions using the annotations in the R documentation around your
functions.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/hosted
%doc %{rlibdir}/%{packname}/hosted-new.R
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/server
%doc %{rlibdir}/%{packname}/swagger-ui
%{rlibdir}/%{packname}/INDEX
