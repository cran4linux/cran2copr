%global packname  simPH
%global packver   1.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.11
Release:          3%{?dist}
Summary:          Tools for Simulating and Plotting Quantities of InterestEstimated from Cox Proportional Hazards Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-dplyr >= 0.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-dplyr >= 0.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lazyeval 
Requires:         R-MASS 
Requires:         R-mgcv 
Requires:         R-CRAN-stringr 
Requires:         R-survival 
Requires:         R-CRAN-quadprog 

%description
Simulates and plots quantities of interest (relative hazards, first
differences, and hazard ratios) for linear coefficients, multiplicative
interactions, polynomials, penalised splines, and non-proportional
hazards, as well as stratified survival curves from Cox Proportional
Hazard models. It also simulates and plots marginal effects for
multiplicative interactions.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
