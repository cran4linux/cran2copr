%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regclass
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for an Introductory Class in Regression and Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-bestglm 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-CRAN-bestglm 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart.plot 

%description
Contains basic tools for visualizing, interpreting, and building
regression models.  It has been designed for use with the book
Introduction to Regression and Modeling with R by Adam Petrie, Cognella
Publishers, ISBN: 978-1-63189-250-9.

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
