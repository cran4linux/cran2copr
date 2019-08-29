%global packname  fitur
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}
Summary:          Fit Univariate Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-stats 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-DT 

%description
Wrapper for computing parameters for univariate distributions using MLE.
It creates an object that stores d, p, q, r functions as well as
parameters and statistics for diagnostics. Currently supports automated
fitting from base and actuar packages. A manually fitting distribution
fitting function is included to support directly specifying parameters for
any distribution from ancillary packages.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
