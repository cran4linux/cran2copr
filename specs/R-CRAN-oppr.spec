%global packname  oppr
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          Optimal Project Prioritization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-lpSolveAPI >= 5.5.2.0.17
BuildRequires:    R-CRAN-ape >= 5.2
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-cli >= 1.0.1
BuildRequires:    R-CRAN-proto >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.100.5.0
BuildRequires:    R-CRAN-RcppProgress >= 0.4.1
BuildRequires:    R-CRAN-viridisLite >= 0.3.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-CRAN-tidytree >= 0.1.9
BuildRequires:    R-CRAN-uuid >= 0.1.2
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-lpSolveAPI >= 5.5.2.0.17
Requires:         R-CRAN-ape >= 5.2
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-cli >= 1.0.1
Requires:         R-CRAN-proto >= 1.0.0
Requires:         R-CRAN-viridisLite >= 0.3.0
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-tidytree >= 0.1.9
Requires:         R-CRAN-uuid >= 0.1.2
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-Matrix 

%description
A decision support tool for prioritizing conservation projects.
Prioritizations can be developed by maximizing expected feature richness,
expected phylogenetic diversity, the number of features that meet
persistence targets, or identifying a set of projects that meet
persistence targets for minimal cost. Constraints (e.g. lock in specific
actions) and feature weights can also be specified to further customize
prioritizations. After defining a project prioritization problem,
solutions can be obtained using exact algorithms, heuristic algorithms, or
random processes. In particular, it is recommended to install the 'Gurobi'
optimizer (available from <https://www.gurobi.com>) because it can
identify optimal solutions very quickly. Finally, methods are provided for
comparing different prioritizations and evaluating their benefits.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
