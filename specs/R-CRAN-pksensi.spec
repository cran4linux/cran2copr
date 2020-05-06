%global packname  pksensi
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Global Sensitivity Analysis in Physiologically Based KineticModeling

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reshape 

%description
Applying the global sensitivity analysis workflow to investigate the
parameter uncertainty and sensitivity in physiologically based kinetic
(PK) models, especially the physiologically based
pharmacokinetic/toxicokinetic model with multivariate outputs. The package
also provides some functions to check the convergence and sensitivity of
model parameters.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
