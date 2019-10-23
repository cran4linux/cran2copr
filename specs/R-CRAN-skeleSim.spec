%global packname  skeleSim
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}
Summary:          Genetic Simulation Engine

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmetasim >= 3.0.0
BuildRequires:    R-CRAN-swfscMisc >= 1.1
BuildRequires:    R-CRAN-strataG >= 1.0
BuildRequires:    R-CRAN-shiny >= 0.13.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-hierfstat 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-rmetasim >= 3.0.0
Requires:         R-CRAN-swfscMisc >= 1.1
Requires:         R-CRAN-strataG >= 1.0
Requires:         R-CRAN-shiny >= 0.13.0
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-hierfstat 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-markdown 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 

%description
A shiny interface and supporting tools to guide users in choosing
appropriate simulations, setting parameters, calculating summary genetic
statistics, and organizing data output, all within the R environment. In
addition to supporting existing forward and reverse-time simulators, new
simulators can be integrated into the environment relatively easily.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/tableinput
%{rlibdir}/%{packname}/INDEX
