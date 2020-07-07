%global packname  dpa
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Dynamic Path Approach

License:          LGPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         tcl
Requires:         tk
Requires:         bwidget
BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-sem 
BuildRequires:    R-CRAN-igraph 
Requires:         R-tcltk 
Requires:         R-CRAN-sem 
Requires:         R-CRAN-igraph 

%description
A GUI or command-line operated data analysis tool, for analyzing
time-dependent simulation data in which multiple instantaneous or
time-lagged relations are assumed. This package uses Structural Equation
Modeling (the sem package). It is aimed to deal with time-dependent data
and estimate whether a causal diagram fits data from an (agent-based)
simulation model.

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
