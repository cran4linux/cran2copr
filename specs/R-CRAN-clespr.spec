%global __brp_check_rpaths %{nil}
%global packname  clespr
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Composite Likelihood Estimation for Spatial Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-survival >= 2.37.5
BuildRequires:    R-CRAN-magic >= 1.5.6
BuildRequires:    R-CRAN-AER >= 1.2.5
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-CRAN-clordr >= 1.0.2
BuildRequires:    R-CRAN-doParallel >= 1.0.11
BuildRequires:    R-CRAN-pbivnorm >= 0.6.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-MASS >= 7.3.45
Requires:         R-survival >= 2.37.5
Requires:         R-CRAN-magic >= 1.5.6
Requires:         R-CRAN-AER >= 1.2.5
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-CRAN-clordr >= 1.0.2
Requires:         R-CRAN-doParallel >= 1.0.11
Requires:         R-CRAN-pbivnorm >= 0.6.0
Requires:         R-utils 
Requires:         R-stats 

%description
Composite likelihood approach is implemented to estimating statistical
models for spatial ordinal and proportional data based on Feng et al.
(2014) <doi:10.1002/env.2306>. Parameter estimates are identified by
maximizing composite log-likelihood functions using the limited memory
BFGS optimization algorithm with bounding constraints, while standard
errors are obtained by estimating the Godambe information matrix.

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
