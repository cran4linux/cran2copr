%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Deducer
%global packver   0.9-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Data Analysis GUI for R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-JGR >= 1.7.10
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-effects 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-JGR >= 1.7.10
Requires:         R-CRAN-car 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-effects 

%description
An intuitive, cross-platform graphical data analysis system. It uses menus
and dialogs to guide the user efficiently through the data manipulation
and analysis process, and has an excel like spreadsheet for easy data
frame visualization and editing. Deducer works best when used with the
Java based R GUI JGR, but the dialogs can be called from the command line.
Dialogs have also been integrated into the Windows Rgui.

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
