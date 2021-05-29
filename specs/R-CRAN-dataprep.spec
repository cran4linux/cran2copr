%global packname  dataprep
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient and Flexible Data Preprocessing Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-zoo 

%description
Efficiently and flexibly preprocess data using a set of data filtering,
deletion, and interpolation tools. These data preprocessing methods are
developed based on the principles of completeness, accuracy, threshold
method, and linear interpolation and through the setting of constraint
conditions, time completion & recovery, and fast & efficient calculation
and grouping. Key preprocessing steps include deletions of variables and
observations, outlier removal, and missing values (NA) interpolation,
which are dependent on the incomplete and dispersed degrees of raw data.
They clean data more accurately, keep more samples, and add no outliers
after interpolation, compared with ordinary methods. Auto-identification
of consecutive NA via run-length based grouping is used in observation
deletion, outlier removal, and NA interpolation; thus, new outliers are
not generated in interpolation. Conditional extremum is proposed to
realize point-by-point weighed outlier removal that saves non-outliers
from being removed. Plus, time series interpolation with values to refer
to within short periods further ensures reliable interpolation. These
methods are based on and improved from the reference: Liang, C.-S., Wu,
H., Li, H.-Y., Zhang, Q., Li, Z. & He, K.-B. (2020)
<doi:10.1016/j.scitotenv.2020.140923>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
