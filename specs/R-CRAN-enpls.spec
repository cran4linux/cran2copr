%global __brp_check_rpaths %{nil}
%global packname  enpls
%global packver   6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Ensemble Partial Least Squares Regression

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-spls 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-spls 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plotly 

%description
An algorithmic framework for measuring feature importance, outlier
detection, model applicability domain evaluation, and ensemble predictive
modeling with (sparse) partial least squares regressions.

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
