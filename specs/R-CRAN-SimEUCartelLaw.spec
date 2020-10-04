%global packname  SimEUCartelLaw
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Simulation of Legal Exemption System for European Cartel Law

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-plot3Drgl 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-stats 
Requires:         R-CRAN-plot3Drgl 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-rgl 
Requires:         R-stats 

%description
Monte Carlo simulations of a game-theoretic model for the legal exemption
system of the European cartel law are implemented in order to estimate the
(mean) deterrent effect of this system. The input and output parameters of
the simulated cartel opportunities can be visualized by three-dimensional
projections.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
