%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pikchr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Wrapper for 'pikchr' (PIC) Diagram Language

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rsvg 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-brio 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rsvg 

%description
An 'R' interface to 'pikchr' (<https://pikchr.org>, pronounced “picture”),
a 'PIC'-like markup language for creating diagrams within technical
documentation. Originally developed by Brian Kernighan, 'PIC' has been
adapted into 'pikchr' by D. Richard Hipp, the creator of 'SQLite'.
'pikchr' is designed to be embedded in fenced code blocks of Markdown or
other documentation markup languages, making it ideal for generating
diagrams in text-based formats. This package allows R users to seamlessly
integrate the descriptive syntax of 'pikchr' for diagram creation directly
within the 'R' environment.

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
