%global packname  MonteCarlo
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          2%{?dist}
Summary:          Automatic Parallelized Monte Carlo Simulations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 3.0.2
BuildRequires:    R-utils >= 3.0.2
BuildRequires:    R-CRAN-snowfall >= 1.84.4
BuildRequires:    R-CRAN-abind >= 1.4.0
BuildRequires:    R-CRAN-reshape >= 0.8.6
BuildRequires:    R-CRAN-snow >= 0.4.1
BuildRequires:    R-CRAN-rlecuyer >= 0.3.4
BuildRequires:    R-codetools >= 0.2.8
Requires:         R-stats >= 3.0.2
Requires:         R-utils >= 3.0.2
Requires:         R-CRAN-snowfall >= 1.84.4
Requires:         R-CRAN-abind >= 1.4.0
Requires:         R-CRAN-reshape >= 0.8.6
Requires:         R-CRAN-snow >= 0.4.1
Requires:         R-CRAN-rlecuyer >= 0.3.4
Requires:         R-codetools >= 0.2.8

%description
Simplifies Monte Carlo simulation studies by automatically setting up
loops to run over parameter grids and parallelising the Monte Carlo
repetitions. It also generates LaTeX tables.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
