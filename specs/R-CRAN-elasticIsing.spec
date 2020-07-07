%global packname  elasticIsing
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          2%{?dist}
Summary:          Ising Network Estimation using Elastic Net and k-FoldCross-Validation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-qgraph 
Requires:         R-methods 

%description
Description: Uses k-fold cross-validation and elastic-net regularization
to estimate the Ising model on binary data. Produces 3D plots of the cost
function as a function of the tuning parameter in addition to the optimal
network structure.

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

%files
%{rlibdir}/%{packname}
