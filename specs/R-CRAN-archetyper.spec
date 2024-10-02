%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  archetyper
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Archetype for Data Mining and Data Science Projects

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-log4r 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-skimr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-bannerCommenter 
BuildRequires:    R-CRAN-feather 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ps 
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-CRAN-here 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-log4r 
Requires:         R-CRAN-config 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-skimr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-bannerCommenter 
Requires:         R-CRAN-feather 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ps 

%description
A project template to support the data science workflow.

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
