%global packname  JOPS
%global packver   0.1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.15
Release:          1%{?dist}%{?buildtag}
Summary:          Practical Smoothing with P-Splines

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SpATS >= 1.0.13
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-fds 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-SemiPar 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-SpATS >= 1.0.13
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-fds 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-SemiPar 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Functions and data to reproduce all plots in the book "Practical
Smoothing. The Joys of P-splines" by Paul H.C. Eilers and Brian D. Marx
(2021, ISBN:978-1108482950).

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
