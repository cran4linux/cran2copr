%global __brp_check_rpaths %{nil}
%global packname  fergm
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation and Fit Assessment of Frailty Exponential RandomGraph Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm >= 3.9
BuildRequires:    R-stats >= 3.4.4
BuildRequires:    R-parallel >= 3.3.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rstan >= 2.16.2
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-network >= 1.13.0
BuildRequires:    R-CRAN-matrixStats >= 0.52.2
BuildRequires:    R-CRAN-extrafont >= 0.17
Requires:         R-CRAN-ergm >= 3.9
Requires:         R-stats >= 3.4.4
Requires:         R-parallel >= 3.3.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rstan >= 2.16.2
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-network >= 1.13.0
Requires:         R-CRAN-matrixStats >= 0.52.2
Requires:         R-CRAN-extrafont >= 0.17

%description
Frailty Exponential Random Graph Models estimated through pseudo
likelihood with frailty terms estimated using 'Stan' as per
Box-Steffensmeier et. al (2017) <doi:10.7910/DVN/K3D1M2>. Goodness of fit
for Frailty Exponential Random Graph Models is also available, with easy
visualizations for comparison to fit Exponential Random Graph Models.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
