%global __brp_check_rpaths %{nil}
%global packname  htmlTable
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Tables for Markdown/HTML

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-rstudioapi >= 0.6
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-knitr >= 1.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-rstudioapi >= 0.6
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 

%description
Tables with state-of-the-art layout elements such as row spanners, column
spanners, table spanners, zebra striping, and more. While allowing
advanced layout, the underlying css-structure is simple in order to
maximize compatibility with common word processors.  The package also
contains a few text formatting functions that help outputting text
compatible with HTML/LaTeX.

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
