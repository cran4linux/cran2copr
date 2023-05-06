%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ContaminatedMixt
%global packver   1.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering and Classification with the Contaminated Normal

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-mixture 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-mixture 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-mvtnorm 
Requires:         R-grDevices 

%description
Fits mixtures of multivariate contaminated normal distributions (with
eigen-decomposed scale matrices) via the expectation conditional-
maximization algorithm under a clustering or classification paradigm
Methods are described in Antonio Punzo, Angelo Mazza, and Paul D
McNicholas (2018) <doi:10.18637/jss.v085.i10>.

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
