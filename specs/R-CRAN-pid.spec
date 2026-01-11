%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pid
%global packver   0.65
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.65
Release:          1%{?dist}%{?buildtag}
Summary:          Process Improvement using Data

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-FrF2 
BuildRequires:    R-CRAN-DoE.base 
BuildRequires:    R-CRAN-FrF2.catlg128 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-png 
Requires:         R-CRAN-FrF2 
Requires:         R-CRAN-DoE.base 
Requires:         R-CRAN-FrF2.catlg128 

%description
A collection of scripts and data files for the statistics text: "Process
Improvement using Data" <https://learnche.org/pid/> and the online course
"Experimentation for Improvement" found on Coursera. The package contains
code for designed experiments, data sets and other convenience functions
used in the book.

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
