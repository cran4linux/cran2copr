%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npsm
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Statistical Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfit 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-Rfit 
Requires:         R-methods 
Requires:         R-CRAN-class 
Requires:         R-CRAN-plyr 

%description
Accompanies the book "Nonparametric Statistical Methods Using R, 2nd
Edition" by Kloke and McKean (2024, ISBN:9780367651350).  Includes
methods, datasets, and random number generation useful for the study of
robust and/or nonparametric statistics.  Emphasizes classical
nonparametric methods for a variety of designs --- especially one-sample
and two-sample problems.  Includes methods for general scores, including
estimation and testing for the two-sample location problem as well as
Hogg's adaptive method.

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
