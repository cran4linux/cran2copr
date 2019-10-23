%global packname  sprm
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Sparse and Non-Sparse Partial Robust M Regression andClassification

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-cvTools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 

%description
Robust dimension reduction methods for regression and discriminant
analysis are implemented that yield estimates with a partial least squares
alike interpretability. Partial robust M regression (PRM) is robust to
both vertical outliers and leverage points. Sparse partial robust M
regression (SPRM) is a related robust method with sparse coefficient
estimate, and therefore with intrinsic variable selection. For binary
classification related discriminant methods are PRM-DA and SPRM-DA.

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
