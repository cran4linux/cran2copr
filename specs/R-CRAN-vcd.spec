%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vcd
%global packver   1.4-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.13
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Categorical Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-lmtest 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-grDevices 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-lmtest 

%description
Visualization techniques, data sets, summary and inference procedures
aimed particularly at categorical data. Special emphasis is given to
highly extensible grid graphics. The package was package was originally
inspired by the book "Visualizing Categorical Data" by Michael Friendly
and is now the main support package for a new book, "Discrete Data
Analysis with R" by Michael Friendly and David Meyer (2015).

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
