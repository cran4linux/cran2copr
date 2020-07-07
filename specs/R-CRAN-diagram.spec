%global packname  diagram
%global packver   1.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.4
Release:          3%{?dist}
Summary:          Functions for Visualising Simple Graphs (Networks), PlottingFlow Diagrams

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.01
Requires:         R-core >= 2.01
BuildArch:        noarch
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-shape 
Requires:         R-stats 
Requires:         R-graphics 

%description
Visualises simple graphs (networks) based on a transition matrix,
utilities to plot flow diagrams, visualising webs, electrical networks,
etc. Support for the book "A practical guide to ecological modelling -
using R as a simulation platform" by Karline Soetaert and Peter M.J.
Herman (2009), Springer. and the book "Solving Differential Equations in
R" by Karline Soetaert, Jeff Cash and Francesca Mazzia (2012), Springer.
Includes demo(flowchart), demo(plotmat), demo(plotweb).

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
