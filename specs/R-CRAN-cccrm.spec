%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cccrm
%global packver   3.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Concordance Correlation Coefficient for Repeated (and Non-Repeated) Measures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-nlmeU 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-nlmeU 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-future 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 

%description
Estimates the Concordance Correlation Coefficient to assess agreement. The
scenarios considered are non-repeated measures, non-longitudinal repeated
measures (replicates) and longitudinal repeated measures. It also includes
the estimation of the one-way intraclass correlation coefficient also
known as reliability index. The estimation approaches implemented are
variance components and U-statistics approaches. Description of methods
can be found in Fleiss (1986) <doi:10.1002/9781118032923> and Carrasco et
al. (2013) <doi:10.1016/j.cmpb.2012.09.002>.

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
