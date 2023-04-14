%global __brp_check_rpaths %{nil}
%global packname  freqparcoord
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Novel Methods for Parallel Coordinates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-mvtnorm 

%description
New approaches to parallel coordinates plots for multivariate data
visualization, including applications to clustering, outlier hunting and
regression diagnostics.  Includes general functions for multivariate
nonparametric density and regression estimation, using parallel
computation.

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
