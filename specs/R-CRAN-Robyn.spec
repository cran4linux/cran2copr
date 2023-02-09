%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Robyn
%global packver   3.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Automated Marketing Mix Modeling (MMM) from Meta Marketing Science

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lares 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-prophet 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rPref 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lares 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-prophet 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rPref 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Semi-Automated Marketing Mix Modeling (MMM) aiming to reduce human bias by
means of ridge regression and evolutionary algorithms, enables actionable
decision making providing a budget allocation and diminishing returns
curves and allows ground-truth calibration to account for causation.

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
