%global __brp_check_rpaths %{nil}
%global packname  iheiddown
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          For Writing Geneva Graduate Institute Documents

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
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-gender 
BuildRequires:    R-CRAN-pagedown 
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
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-gender 
Requires:         R-CRAN-pagedown 

%description
A set of tools for writing documents according to Geneva Graduate
Institute conventions and regulations. The most common use is for writing
and compiling theses or thesis chapters, as drafts or for examination with
correct preamble formatting. However, the package also offers users to
create HTML presentation slides with 'xaringan', complete problem sets,
format posters, and, for course instructors, prepare a syllabus. The
package includes additional functions for institutional color palettes, an
institutional 'ggplot' theme, a function for counting manuscript words,
and a bibliographical analysis toolkit.

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
