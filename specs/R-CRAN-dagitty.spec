%global packname  dagitty
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Graphical Analysis of Structural Causal Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-jsonlite 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
A port of the web-based software 'DAGitty', available at
<http://dagitty.net>, for analyzing structural causal models (also known
as directed acyclic graphs or DAGs). This package computes covariate
adjustment sets for estimating causal effects, enumerates instrumental
variables, derives testable implications (d-separation and vanishing
tetrads), generates equivalent models, and includes a simple facility for
data simulation.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/js
%{rlibdir}/%{packname}/INDEX
