%global packname  ggiraph
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          2%{?dist}
Summary:          Make 'ggplot2' Graphics Interactive

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-htmlwidgets >= 0.6
BuildRequires:    R-CRAN-gdtools >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-htmlwidgets >= 0.6
Requires:         R-CRAN-gdtools >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-uuid 

%description
Create interactive 'ggplot2' graphics using 'htmlwidgets'.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
