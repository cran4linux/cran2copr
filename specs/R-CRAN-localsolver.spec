%global __brp_check_rpaths %{nil}
%global packname  localsolver
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}%{?buildtag}
Summary:          R API to LocalSolver

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch

%description
The package converts R data onto input and data for LocalSolver, executes
optimization and exposes optimization results as R data. LocalSolver
(http://www.localsolver.com/) is an optimization engine developed by
Innovation24 (http://www.innovation24.fr/). It is designed to solve
large-scale mixed-variable non-convex optimization problems.  The
localsolver package is developed and maintained by WLOG Solutions
(http://www.wlogsolutions.com/en/) in collaboration with Decision Support
and Analysis Division at Warsaw School of Economics
(http://www.sgh.waw.pl/en/).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
