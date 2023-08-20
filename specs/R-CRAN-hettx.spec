%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hettx
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fisherian and Neymanian Methods for Detecting and Measuring Treatment Effect Variation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 

%description
Implements methods developed by Ding, Feller, and Miratrix (2016)
<doi:10.1111/rssb.12124> <arXiv:1412.5000>, and Ding, Feller, and Miratrix
(2018) <doi:10.1080/01621459.2017.1407322> <arXiv:1605.06566> for testing
whether there is unexplained variation in treatment effects across
observations, and for characterizing the extent of the explained and
unexplained variation in treatment effects. The package includes wrapper
functions implementing the proposed methods, as well as helper functions
for analyzing and visualizing the results of the test.

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
