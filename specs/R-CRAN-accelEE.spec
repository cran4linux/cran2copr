%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  accelEE
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Energy Expenditure from Accelerometer Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-PAutilities >= 1.3.0
BuildRequires:    R-CRAN-Sojourn >= 1.1.0
BuildRequires:    R-CRAN-TwoRegression >= 1.0.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-utils 
Requires:         R-CRAN-PAutilities >= 1.3.0
Requires:         R-CRAN-Sojourn >= 1.1.0
Requires:         R-CRAN-TwoRegression >= 1.0.0
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tree 
Requires:         R-utils 

%description
Simplifies the application of various energy expenditure models. The
package is intended as a hub that brings together methods from a variety
of other, themed packages such as 'Sojourn' and 'TwoRegression'. Several
methods are supported locally as well, including the linear methods of
Hildebrand et al. (2014) <doi:10.1249/MSS.0000000000000289> and the
non-linear adaptation by Ellingson et al. (2017)
<doi:10.1088/1361-6579/aa6d00>. The package can combine output from
different methods and produce standardized output in a range of units.

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
