%global __brp_check_rpaths %{nil}
%global packname  editrules
%global packver   2.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.3
Release:          3%{?dist}%{?buildtag}
Summary:          Parsing, Applying, and Manipulating Data Cleaning Rules

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lpSolveAPI 

%description
Facilitates reading and manipulating (multivariate) data restrictions
(edit rules) on numerical and categorical data. Rules can be defined with
common R syntax and parsed to an internal (matrix-like format). Rules can
be manipulated with variable elimination and value substitution methods,
allowing for feasibility checks and more. Data can be tested against the
rules and erroneous fields can be found based on Fellegi and Holt's
generalized principle. Rules dependencies can be visualized with using the
'igraph' package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
