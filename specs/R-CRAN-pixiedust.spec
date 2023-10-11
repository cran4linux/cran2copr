%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pixiedust
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tables so Beautifully Fine-Tuned You Will Believe It's Magic

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.8.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-labelVector 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-checkmate >= 1.8.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-labelVector 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 

%description
The introduction of the 'broom' package has made converting model objects
into data frames as simple as a single function. While the 'broom' package
focuses on providing tidy data frames that can be used in advanced
analysis, it deliberately stops short of providing functionality for
reporting models in publication-ready tables. 'pixiedust' provides this
functionality with a programming interface intended to be similar to
'ggplot2's system of layers with fine tuned control over each cell of the
table. Options for output include printing to the console and to the
common markdown formats (markdown, HTML, and LaTeX). With a little
'pixiedust' (and happy thoughts) tables can really fly.

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
