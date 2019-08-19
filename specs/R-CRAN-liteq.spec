%global packname  liteq
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Lightweight Portable Message Queue Using 'SQLite'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-RSQLite 

%description
Temporary and permanent message queues for R. Built on top of 'SQLite'
databases. 'SQLite' provides locking, and makes it possible to detect
crashed consumers. Crashed jobs can be automatically marked as "failed",
or put in the queue again, potentially a limited number of times.

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
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/README.Rmd
%{rlibdir}/%{packname}/INDEX
