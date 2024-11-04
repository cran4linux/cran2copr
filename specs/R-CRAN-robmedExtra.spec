%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robmedExtra
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Functionality for (Robust) Mediation Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-flextable >= 0.8.3
BuildRequires:    R-CRAN-robmed >= 0.10.0
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-flextable >= 0.8.3
Requires:         R-CRAN-robmed >= 0.10.0
Requires:         R-CRAN-DT 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-officer 
Requires:         R-stats 
Requires:         R-utils 

%description
This companion package extends the package 'robmed' (Alfons, Ates &
Groenen, 2022b; <doi:10.18637/jss.v103.i13>) in various ways.  Most
notably, it provides a graphical user interface for the robust bootstrap
test ROBMED (Alfons, Ates & Groenen, 2022a;
<doi:10.1177/1094428121999096>) to make the method more accessible to less
proficient 'R' users, as well as functions to export the results as a
table in a 'Microsoft Word' or 'Microsoft Powerpoint' document, or as a
'LaTeX' table. Furthermore, the package contains a 'shiny' app to compare
various bootstrap procedures for mediation analysis on simulated data.

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
