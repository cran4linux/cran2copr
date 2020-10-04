%global packname  DoseFinding
%global packver   0.9-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.17
Release:          3%{?dist}%{?buildtag}
Summary:          Planning and Analyzing Dose Finding Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-lattice 
Requires:         R-CRAN-mvtnorm 

%description
The DoseFinding package provides functions for the design and analysis of
dose-finding experiments (with focus on pharmaceutical Phase II clinical
trials). It provides functions for: multiple contrast tests, fitting
non-linear dose-response models (using Bayesian and non-Bayesian
estimation), calculating optimal designs and an implementation of the
MCPMod methodology (Pinheiro et al. (2014) <doi:10.1002/sim.6052>).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
