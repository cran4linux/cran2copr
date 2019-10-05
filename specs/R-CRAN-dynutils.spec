%global packname  dynutils
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Common Functionality for the 'dynverse' Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-proxyC 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-proxyC 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
Provides common functionality for the 'dynverse' packages. 'dynverse' is
created to support the development, execution, and benchmarking of
trajectory inference methods. For more information, check out
<https://dynverse.org>.

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
%{rlibdir}/%{packname}/libs
