%global __brp_check_rpaths %{nil}
%global packname  sourceR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fits a Non-Parametric Bayesian Source Attribution Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-cluster 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-SPIn 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-assertthat 
Requires:         R-methods 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-R6 
Requires:         R-cluster 
Requires:         R-stats 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-SPIn 
Requires:         R-grDevices 
Requires:         R-CRAN-reshape2 

%description
Implements a non-parametric source attribution model to attribute cases of
disease to sources in Bayesian framework with source and type effects.
Type effects are clustered using a Dirichlet Process. Multiple times and
locations are supported.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
