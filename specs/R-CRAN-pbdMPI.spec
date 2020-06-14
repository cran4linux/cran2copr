%global packname  pbdMPI
%global packver   0.3-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          2%{?dist}
Summary:          Programming with Big Data -- Interface to MPI

License:          Mozilla Public License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openmpi-devel >= 1.5.4
Requires:         openmpi
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlecuyer 
BuildRequires:    R-CRAN-float 
Requires:         R-methods 
Requires:         R-CRAN-rlecuyer 
Requires:         R-CRAN-float 

%description
An efficient interface to MPI by utilizing S4 classes and methods with a
focus on Single Program/Multiple Data ('SPMD') parallel programming style,
which is intended for batch parallel execution.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/c_combine_r
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%doc %{rlibdir}/%{packname}/etc
