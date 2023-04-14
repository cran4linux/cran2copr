%global __brp_check_rpaths %{nil}
%global packname  NPflow
%global packver   0.13.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.3
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Nonparametrics for Automatic Gating of Flow-CytometryData

License:          LGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-truncnorm 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-reshape2 

%description
Dirichlet process mixture of multivariate normal, skew normal or skew
t-distributions modeling oriented towards flow-cytometry data
preprocessing applications. Method is detailed in: Hejblum, Alkhassimn,
Gottardo, Caron & Thiebaut (2019) <doi: 10.1214/18-AOAS1209>.

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
