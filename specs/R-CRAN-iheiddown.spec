%global __brp_check_rpaths %{nil}
%global packname  iheiddown
%global packver   0.8.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.6
Release:          1%{?dist}%{?buildtag}
Summary:          For Writing Graduate Institute Geneva Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-xaringan 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-bib2df 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-gender 
BuildRequires:    R-CRAN-remotes 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-xaringan 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-bib2df 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-gender 
Requires:         R-CRAN-remotes 

%description
A set of tools to support writing various documents according to the
Graduate Institute of International and Development Studies conventions
and regulations. The most common use will be for writing and compiling
theses or thesis chapters, as drafts or for examination with all the
correct preamble content. However, the package also offers the creation of
html presentation slides via 'xaringan', the capacity to write problem
sets and, for course instructors, the ability to create syllabi. The
package includes additional functions for institutional color palettes and
an institutional 'ggplot' theme, as well as a function for word counts and
a bibliographical analysis toolkit.

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
