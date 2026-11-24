%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easyCODA
%global packver   0.50
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.50
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Data Analysis in Practice

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan >= 2.3
BuildRequires:    R-CRAN-ca >= 0.7
BuildRequires:    R-CRAN-ellipse >= 0.4.1
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-vegan >= 2.3
Requires:         R-CRAN-ca >= 0.7
Requires:         R-CRAN-ellipse >= 0.4.1
Requires:         R-CRAN-boot 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Univariate and multivariate methods for compositional data analysis, based
on logratios. The package implements the approach in the book
Compositional Data Analysis in Practice by Michael Greenacre (2018, 2026),
where accent is given to simple pairwise logratios. Selection can be made
of logratios that account for a maximum percentage of logratio variance or
maximize prediction accuracy of a response variable. Various multivariate
analyses of logratios are included in the package.

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
