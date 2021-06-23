%global __brp_check_rpaths %{nil}
%global packname  RH2
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          DBI/RJDBC Interface to H2 Database

License:          Mozilla Public License 1.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RJDBC 
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-chron 
Requires:         R-methods 
Requires:         R-CRAN-RJDBC 
Requires:         R-CRAN-rJava 

%description
DBI/RJDBC interface to h2 database. h2 version 1.3.175 is included.

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
%doc %{rlibdir}/%{packname}/INSTALL
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/NOTE
%doc %{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/INDEX
