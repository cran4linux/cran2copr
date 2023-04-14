%global __brp_check_rpaths %{nil}
%global packname  multiway
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Component Models for Multi-Way Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CMLS 
BuildRequires:    R-parallel 
Requires:         R-CRAN-CMLS 
Requires:         R-parallel 

%description
Fits multi-way component models via alternating least squares algorithms
with optional constraints. Fit models include N-way Canonical Polyadic
Decomposition, Individual Differences Scaling, Multiway Covariates
Regression, Parallel Factor Analysis (1 and 2), Simultaneous Component
Analysis, and Tucker Factor Analysis.

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
