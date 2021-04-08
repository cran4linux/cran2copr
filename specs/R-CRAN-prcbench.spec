%global packname  prcbench
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Testing Workbench for Precision-Recall Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.1.1
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-PRROC >= 1.1
BuildRequires:    R-CRAN-ROCR >= 1.0.7
BuildRequires:    R-CRAN-memoise >= 1.0.0
BuildRequires:    R-CRAN-rJava >= 0.9.7
BuildRequires:    R-CRAN-precrec >= 0.1
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-CRAN-R6 >= 2.1.1
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-PRROC >= 1.1
Requires:         R-CRAN-ROCR >= 1.0.7
Requires:         R-CRAN-memoise >= 1.0.0
Requires:         R-CRAN-rJava >= 0.9.7
Requires:         R-CRAN-precrec >= 0.1
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-methods 

%description
A testing workbench for evaluating precision-recall curves under various
conditions.

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
