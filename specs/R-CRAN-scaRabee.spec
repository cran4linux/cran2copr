%global packname  scaRabee
%global packver   1.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Optimization Toolkit for Pharmacokinetic-Pharmacodynamic Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-neldermead >= 1.0.8
BuildRequires:    R-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-utils 
Requires:         R-CRAN-neldermead >= 1.0.8
Requires:         R-lattice 
Requires:         R-grid 
Requires:         R-CRAN-deSolve 
Requires:         R-utils 

%description
scaRabee is a port of the Scarabee toolkit originally written as a
Matlab-based application. It provides a framework for simulation and
optimization of pharmacokinetic-pharmacodynamic models at the individual
and population level. It is built on top of the neldermead package, which
provides the direct search algorithm proposed by Nelder and Mead for model
optimization.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
