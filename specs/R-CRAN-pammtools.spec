%global packname  pammtools
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Piece-Wise Exponential Additive Mixed Modeling Tools forSurvival Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-survival >= 2.39.5
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pec 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-survival >= 2.39.5
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-mgcv 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pec 

%description
The Piece-wise exponential (Additive Mixed) Model (PAMM; Bender and
Scheipl (2018) <doi: 10.1177/1471082X17748083>) is a powerful model class
for the analysis of survival (or time-to-event) data, based on Generalized
Additive (Mixed) Models (GA(M)Ms). It offers intuitive specification and
robust estimation of complex survival models with stratified baseline
hazards, random effects, time-varying effects, time-dependent covariates
and cumulative effects (Bender and others (2018) <doi:
10.1093/biostatistics/kxy003>. pammtools provides tidy workflow for
survival analysis with PAMMs, including data simulation, transformation
and other functions for data preprocessing and model post-processing as
well as visualization.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
