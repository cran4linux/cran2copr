%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autoFlagR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          AI-Driven Anomaly Detection for Data Quality

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.0
BuildRequires:    R-CRAN-isotree 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-rmarkdown >= 2.0
Requires:         R-CRAN-isotree 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-PRROC 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-scales 

%description
Automated data quality auditing using unsupervised machine learning.
Provides AI-driven anomaly detection for data quality assessment,
primarily designed for Electronic Health Records (EHR) data, with
benchmarking capabilities for validation and publication. Methods based
on: Liu et al. (2008) <doi:10.1109/ICDM.2008.17>, Breunig et al. (2000)
<doi:10.1145/342009.335388>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
