%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kutils
%global packver   1.73
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.73
Release:          1%{?dist}%{?buildtag}
Summary:          Project Management Tools

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-RUnit 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-RUnit 

%description
Tools for data importation, recoding, and inspection. There are functions
to create new project folders, R code templates, create uniquely named
output directories, and to quickly obtain a visual summary for each
variable in a data frame.  The main feature here is the systematic
implementation of the "variable key" framework for data importation and
recoding.  We are eager to have community feedback about the variable key
and the vignette about it. In version 1.7, the function 'semTable' is
removed. It was deprecated since 1.67. That is provided in a separate
package, 'semTable'.

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
