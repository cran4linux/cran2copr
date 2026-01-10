%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dipsaus
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Dipping Sauce for Data Analysis and Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-fastmap >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-rstudioapi >= 0.11
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-fastmap >= 1.1.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-rstudioapi >= 0.11
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-digest 

%description
Works as an "add-on" to packages like 'shiny', 'future', as well as
'rlang', and provides utility functions. Just like dipping sauce adding
flavors to potato chips or pita bread, 'dipsaus' for data analysis and
visualizations adds handy functions and enhancements to popular packages.
The goal is to provide simple solutions that are frequently asked for
online, such as how to synchronize 'shiny' inputs without freezing the
app, or how to get memory size on 'Linux' or 'MacOS' system. The
enhancements roughly fall into these four categories: 1. 'shiny' input
widgets; 2. high-performance computing using the 'future' package; 3.
modify R calls and convert among numbers, strings, and other objects. 4.
utility functions to get system information such like CPU chip-set, memory
limit, etc.

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
