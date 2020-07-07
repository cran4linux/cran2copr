%global packname  bioinactivation
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          3%{?dist}
Summary:          Mathematical Modelling of (Dynamic) Microbial Inactivation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.39
BuildRequires:    R-graphics >= 3.1.3
BuildRequires:    R-stats >= 3.1.3
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-FME >= 1.3.2
BuildRequires:    R-CRAN-deSolve >= 1.11
BuildRequires:    R-CRAN-dplyr >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
Requires:         R-MASS >= 7.3.39
Requires:         R-graphics >= 3.1.3
Requires:         R-stats >= 3.1.3
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-FME >= 1.3.2
Requires:         R-CRAN-deSolve >= 1.11
Requires:         R-CRAN-dplyr >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-lazyeval >= 0.1.10

%description
Functions for modelling microbial inactivation under isothermal or dynamic
conditions. The calculations are based on several mathematical models
broadly used by the scientific community and industry. Functions enable to
make predictions for cases where the kinetic parameters are known. It also
implements functions for parameter estimation for isothermal and dynamic
conditions. The model fitting capabilities include an Adaptive Monte Carlo
method for a Bayesian approach to parameter estimation.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
