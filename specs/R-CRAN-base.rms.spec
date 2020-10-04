%global packname  base.rms
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Regression Between Base Function and 'rms' Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-do 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-CRAN-rms 
Requires:         R-survival 
Requires:         R-CRAN-do 
Requires:         R-splines 
Requires:         R-stats 

%description
We perform linear, logistic, and cox regression using the base functions
lm(), glm(), and coxph() in the R software and the 'survival' package.
Likewise, we can use ols(), lrm() and cph() from the 'rms' package for the
same functionality. Each of these two sets of commands has a different
focus. In many cases, we need to use both sets of commands in the same
situation, e.g. we need to filter the full subset model using AIC, and we
need to build a visualization graph for the final model. 'base.rms'
package can help you to switch between the two sets of commands easily.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
