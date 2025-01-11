%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  describedata
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Descriptive Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-rlang 

%description
Helper functions for descriptive tasks such as making print-friendly
bivariate tables, sample size flow counts, and visualizing sample
distributions. Also contains 'R' approximations of some common 'SAS' and
'Stata' functions such as 'PROC MEANS' from 'SAS' and 'ladder', 'gladder',
and 'pwcorr' from 'Stata'.

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
