%global __brp_check_rpaths %{nil}
%global packname  mem
%global packver   2.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.17
Release:          1%{?dist}%{?buildtag}
Summary:          The Moving Epidemic Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-methods 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-EnvStats 
Requires:         R-methods 

%description
The Moving Epidemic Method, created by T Vega and JE Lozano (2012, 2015)
<doi:10.1111/j.1750-2659.2012.00422.x>, <doi:10.1111/irv.12330>, allows
the weekly assessment of the epidemic and intensity status to help in
routine respiratory infections surveillance in health systems. Allows the
comparison of different epidemic indicators, timing and shape with past
epidemics and across different regions or countries with different
surveillance systems. Also, it gives a measure of the performance of the
method in terms of sensitivity and specificity of the alert week.

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
