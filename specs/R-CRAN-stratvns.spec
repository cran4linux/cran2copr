%global packname  stratvns
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Optimal Stratification in Stratified Sampling OptimizationAlgorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-stratification 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-MultAlloc 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-stratification 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-MultAlloc 

%description
An Optimization Algorithm Applied to stratification Problem. It is aims to
delimit the population strata and defining the allocation of
sample,considering the following objective: minimize the sample size given
a fixed precision level. Exhaustive enumeration method is applied in small
problems, while in problems with greater complexity the algorithm is based
on metaheuristic Variable Neighborhood Decomposition Search with Path
Relink.

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
