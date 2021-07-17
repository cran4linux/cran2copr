%global __brp_check_rpaths %{nil}
%global packname  modelObj
%global packver   4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Model Object Framework for Regression Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
A utility library to facilitate the generalization of statistical methods
built on a regression framework. Package developers can use 'modelObj'
methods to initiate a regression analysis without concern for the details
of the regression model and the method to be used to obtain parameter
estimates. The specifics of the regression step are left to the user to
define when calling the function. The user of a function developed within
the 'modelObj' framework creates as input a 'modelObj' that contains the
model and the R methods to be used to obtain parameter estimates and to
obtain predictions.  In this way, a user can easily go from linear to
non-linear models within the same package.

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
