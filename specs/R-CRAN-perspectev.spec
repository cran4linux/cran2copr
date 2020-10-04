%global packname  perspectev
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Permutation of Species During Turnover Events

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-mapproj 
Requires:         R-boot 
Requires:         R-CRAN-sp 

%description
Provides a robust framework for analyzing the extent to which differential
survival with respect to higher level trait variation is reducible to
lower level variation. In addition to its primary test, it also provides
functions for simulation-based power analysis, reading in common data set
formats, and visualizing results. Temporarily contains an edited version
of function hr.mcp() from package 'wild1', written by Glen Sargeant. For
tutorial see: http://evolve.zoo.ox.ac.uk/Evolve/Perspectev.html.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
