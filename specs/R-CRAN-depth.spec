%global packname  depth
%global packver   2.1-1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1.1
Release:          3%{?dist}
Summary:          Nonparametric Depth Functions for Multivariate Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-abind 
Requires:         R-grDevices 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-rgl 

%description
Tools for depth functions methodology applied to multivariate analysis.
Besides allowing calculation of depth values and depth-based location
estimators, the package includes functions or drawing contour plots and
perspective plots of depth functions. Euclidian and spherical depths are
supported.

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
%{rlibdir}/%{packname}/libs
