%global __brp_check_rpaths %{nil}
%global packname  upstartr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities Powering the Globe and Mail's Data Journalism Template

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-librarian 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-textclean 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tgamtheme 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-here 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-librarian 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-textclean 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tgamtheme 
Requires:         R-CRAN-crayon 

%description
Core functions necessary for using The Globe and Mail's R data journalism
template, 'startr', along with utilities for day-to-day data journalism
tasks, such as reading and writing files, producing graphics and cleaning
up datasets.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
