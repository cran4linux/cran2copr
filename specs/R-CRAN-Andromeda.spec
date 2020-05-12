%global packname  Andromeda
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Asynchronous Disk-Based Representation of Massive Data

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-zip 
Requires:         R-methods 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-Rcpp 

%description
Storing very large data objects on a local drive, while still making it
possible to manipulate the data in an efficient manner.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
