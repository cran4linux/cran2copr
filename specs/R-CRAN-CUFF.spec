%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CUFF
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Charles's Utility Function using Formula

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-clipr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-clipr 

%description
Utility functions that provides wrapper to descriptive base functions like
cor, mean and table.  It makes use of the formula interface to pass
variables to functions.  It also provides operators to concatenate (%%+%%),
to repeat (%%n%%) and manage character vectors for nice display.

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
