%global packname  Rmpi
%global packver   0.6-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.9
Release:          2%{?dist}
Summary:          Interface (Wrapper) to MPI (Message-Passing Interface)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    openmpi-devel
Requires:         openmpi
BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-parallel 
Requires:         R-parallel 

%description
An interface (wrapper) to MPI. It also provides interactive R manager and
worker environment.

%prep
%setup -q -c -n %{packname}


%build

%install
%{_openmpi_load}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/cslavePI.c
%doc %{rlibdir}/%{packname}/MacR64slaves.sh
%doc %{rlibdir}/%{packname}/Rprofile
%doc %{rlibdir}/%{packname}/Rslaves.sh
%doc %{rlibdir}/%{packname}/Rslaves32.cmd
%doc %{rlibdir}/%{packname}/Rslaves64.cmd
%doc %{rlibdir}/%{packname}/slavedaemon.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
