%global packname  Sim.DiffProc
%global packver   4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4
Release:          1%{?dist}
Summary:          Simulation of Diffusion Processes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-MASS >= 7.3.30
BuildRequires:    R-CRAN-Deriv >= 3.8.0
BuildRequires:    R-parallel 
Requires:         R-MASS >= 7.3.30
Requires:         R-CRAN-Deriv >= 3.8.0
Requires:         R-parallel 

%description
It provides users with a wide range of tools to simulate, estimate,
analyze, and visualize the dynamics of stochastic differential systems in
both forms Ito and Stratonovich. Statistical analysis with parallel Monte
Carlo and moment equations methods of SDE's. Enabled many searchers in
different domains to use these equations to modeling practical problems in
financial and actuarial modeling and other areas of application, e.g.,
modeling and simulate of first passage time problem in shallow water using
the attractive center (Boukhetala K, 1996) ISBN:1-56252-342-2.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
