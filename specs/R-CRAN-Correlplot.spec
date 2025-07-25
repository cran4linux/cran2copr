%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Correlplot
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Functions for Graphing Correlation Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-calibrate 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lsei 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-calibrate 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lsei 
Requires:         R-CRAN-ggplot2 

%description
Routines for the graphical representation of correlation matrices by means
of correlograms, MDS maps and biplots obtained by PCA, PFA or WALS
(weighted alternating least squares); See Graffelman & De Leeuw (2023)
<doi: 10.1080/00031305.2023.2186952>.

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
