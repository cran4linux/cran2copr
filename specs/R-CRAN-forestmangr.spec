%global __brp_check_rpaths %{nil}
%global packname  forestmangr
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Mensuration and Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-systemfit 
BuildRequires:    R-CRAN-ggpmisc 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-FinCal 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-ggplot2 >= 2.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-systemfit 
Requires:         R-CRAN-ggpmisc 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-car 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-FinCal 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 

%description
Processing forest inventory data with methods such as simple random
sampling, stratified random sampling and systematic sampling. There are
also functions for yield and growth predictions and model fitting, linear
and nonlinear grouped data fitting, and statistical tests. References:
Kershaw Jr., Ducey, Beers and Husch (2016). <doi:10.1002/9781118902028>.

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
