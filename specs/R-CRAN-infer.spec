%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  infer
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Statistical Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-vctrs >= 0.6.5
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-vctrs >= 0.6.5
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-grDevices 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
The objective of this package is to perform inference using an expressive
statistical grammar that coheres with the tidy design framework.

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
