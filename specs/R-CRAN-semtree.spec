%global packname  semtree
%global packver   0.9.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.14
Release:          1%{?dist}
Summary:          Recursive Partitioning for Structural Equation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart.plot >= 3.0.6
BuildRequires:    R-CRAN-OpenMx >= 2.6.9
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-rpart 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-rpart.plot >= 3.0.6
Requires:         R-CRAN-OpenMx >= 2.6.9
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-digest 
Requires:         R-rpart 
Requires:         R-parallel 
Requires:         R-CRAN-plotrix 
Requires:         R-cluster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 

%description
SEM Trees and SEM Forests -- an extension of model-based decision trees
and forests to Structural Equation Models (SEM). SEM trees hierarchically
split empirical data into homogeneous groups sharing similar data patterns
with respect to a SEM by recursively selecting optimal predictors of these
differences. SEM forests are an extension of SEM trees. They are ensembles
of SEM trees each built on a random sample of the original data. By
aggregating over a forest, we obtain measures of variable importance that
are more robust than measures from single trees.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
