%global packname  stpp
%global packver   2.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}
Summary:          Space-Time Point Pattern Simulation, Visualisation and Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rpanel 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-rpanel 
Requires:         R-CRAN-splancs 
Requires:         R-KernSmooth 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-spatstat 
Requires:         R-stats 

%description
Many of the models encountered in applications of point process methods to
the study of spatio-temporal phenomena are covered in 'stpp'. This package
provides statistical tools for analyzing the global and local second-order
properties of spatio-temporal point processes, including estimators of the
space-time inhomogeneous K-function and pair correlation function. It also
includes tools to get static and dynamic display of spatio-temporal point
patterns. See Gabriel et al (2013) <doi:10.18637/jss.v053.i02>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
