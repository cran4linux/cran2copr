%global packname  GUIgems
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Graphical User Interface for Generalized Multistate SimulationModel

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-rpanel 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-tools 
Requires:         R-CRAN-msm 
Requires:         R-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
A graphical user interface for the R package Gems. Apart from the
functionality of Gems package in the Graphical User interface, GUIgems
allows adding states to a defined model, merging states for the analysis
and plotting progression paths between states based on the simulated
cohort. There is also a module in the GUIgems which allows to compare
costs and QALYs between different cohorts.

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
%{rlibdir}/%{packname}/INDEX
