%global packname  openCR
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}
Summary:          Open Population Capture-Recapture

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-secr >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-secr >= 3.2.0
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-CRAN-RcppParallel 

%description
Functions for non-spatial and spatial open-population capture-recapture
analysis.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
