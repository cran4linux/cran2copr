%global packname  dexterMST
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          CML Calibration of Multi Stage Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RSQLite >= 2.0
BuildRequires:    R-CRAN-igraph >= 1.2.1
BuildRequires:    R-CRAN-dbplyr >= 1.2.0
BuildRequires:    R-CRAN-dexter >= 0.8.1
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-RSQLite >= 2.0
Requires:         R-CRAN-igraph >= 1.2.1
Requires:         R-CRAN-dbplyr >= 1.2.0
Requires:         R-CRAN-dexter >= 0.8.1
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-crayon 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Conditional Maximum Likelihood Calibration and data management of
multistage tests. Functions for calibration of the Extended Nominal
Response and the Interaction models, DIF and profile analysis. See Robert
J. Zwitser and Gunter Maris (2015)<doi:10.1007/s11336-013-9369-6>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
