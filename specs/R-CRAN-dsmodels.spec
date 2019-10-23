%global packname  dsmodels
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          A Language to Facilitate Simulation and Visualization ofTwo-Dimensional Dynamical Systems

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-pryr 
Requires:         R-CRAN-shape 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-pryr 

%description
An expressive language to facilitate simulation and visualization of
two-dimensional dynamical systems. The basic elements of the language are
a model wrapping around a function(x,y) which outputs a list(x = xprime, y
= yprime), and a range. The language supports three types of visual
objects: visualizations, features, and backgrounds. Visualizations,
including dots and arrows, depict the behavior of the dynamical system
over the entire range. Features display user-defined curves and points,
and their images under the system. Backgrounds define and color regions of
interest, such as basins of attraction. The language can also approximate
attractors and their basins through simulation.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/staticdocs
%{rlibdir}/%{packname}/INDEX
