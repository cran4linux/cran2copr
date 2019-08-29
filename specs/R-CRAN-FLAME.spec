%global packname  FLAME
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          A Fast Large-Scale Almost Matching Exactly Approach to CausalInference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.9
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-reticulate >= 1.9
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-gmp 
Requires:         R-lattice 
Requires:         R-CRAN-rlang 

%description
The 'FLAME' (Fast Large-scale Almost Matching Exactly) package implements
the matching algorithm in Roy, Rudin, Volfovsky, and Wang (2017)
<arXiv:1707.06315>. 'FLAME' performs matching of treatment and control
units in the potential outcomes framework for large categorical datasets.
'FLAME' creates matches that include as many covariates as possible, and
sequentially drops covariates that are less useful based on a match
quality measure. Match quality combines two important elements – it
considers predictive power from machine learning on a hold out training
set, and a balancing factor to ensure that it does not remove a covariate
that would ruin overlap between treatment and control groups. Currently
the 'FLAME' package applies to categorical data, and provides two
approaches for implementation - bit vectors and database management
systems (e.g., 'PostgreSQL', 'SQLite'). For data that has been adequately
processed and fits in memory, bit vectors should be applied. For extremely
large data that does not fit in memory, database systems should be
applied.

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
%doc %{rlibdir}/%{packname}/DecisionTree.py
%doc %{rlibdir}/%{packname}/Lasso.py
%doc %{rlibdir}/%{packname}/Linear.py
%doc %{rlibdir}/%{packname}/Ridge.py
%{rlibdir}/%{packname}/INDEX
