%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xpose.xtras
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Functionality for the 'xpose' Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-readr >= 2.1.4
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-purrr >= 1.0.1
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-conflicted 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pmxcv 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-xpose 
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-readr >= 2.1.4
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-purrr >= 1.0.1
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-conflicted 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pmxcv 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-xpose 

%description
Adding some at-present missing functionality, or functions unlikely to be
added to the base 'xpose' package.  This includes some diagnostic plots
that have been missing in translation from 'xpose4', but also some useful
features that truly extend the capabilities of what can be done with
'xpose'. These extensions include the concept of a set of 'xpose' objects,
and diagnostics for likelihood-based models.

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
