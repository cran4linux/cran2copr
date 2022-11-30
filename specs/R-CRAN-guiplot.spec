%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  guiplot
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          User-Friendly GUI Plotting Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-shiny >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-excelR 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-shiny >= 1.0.0
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-DT 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-excelR 

%description
Create a user-friendly plotting GUI for 'R'. In addition, one purpose of
creating the 'R' package is to facilitate third-party software to call 'R'
for drawing, for example, 'Phoenix WinNonlin' software calls 'R' to draw
the drug concentration versus time curve.

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
