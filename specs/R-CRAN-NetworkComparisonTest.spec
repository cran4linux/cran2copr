%global packname  NetworkComparisonTest
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Statistical Comparison of Two Networks Based on Three InvarianceMeasures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-IsingFit 
BuildRequires:    R-CRAN-IsingSampler 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-IsingFit 
Requires:         R-CRAN-IsingSampler 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-methods 

%description
This permutation based hypothesis test, suited for Gaussian and binary
data, assesses the difference between two networks based on several
invariance measures (e.g., network structure invariance, global strength
invariance, edge invariance). Network structures are estimated with
l1-regularized partial correlations (Gaussian data) or with l1-regularized
logistic regression (eLasso, binary data). Suited for comparison of
independent and dependent samples. For dependent samples, only supported
for data of one group which is measured twice. See van Borkulo et al.
(2017) <doi:10.13140/RG.2.2.29455.38569>.

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
