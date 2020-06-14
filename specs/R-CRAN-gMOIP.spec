%global packname  gMOIP
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          2%{?dist}
Summary:          Tools for 2D and 3D Plots of Single and Multi-ObjectiveLinear/Integer Programming Models

License:          GPL (>= 3.3.2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgl 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 

%description
Make 2D and 3D plots of linear programming (LP), integer linear
programming (ILP), or mixed integer linear programming (MILP) models with
up to three objectives. Plots of both the solution and criterion space are
possible. For instance the non-dominated (Pareto) set for bi-objective
LP/ILP/MILP programming models (see vignettes for an overview).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
