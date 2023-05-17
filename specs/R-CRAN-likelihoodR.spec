%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  likelihoodR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood Analyses for Common Statistical Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-lme4 

%description
A collection of functions that calculate the log likelihood (support) for
a range of statistical tests. Where possible the likelihood function and
likelihood interval for the observed data are displayed. The evidential
approach used here is based on the book "Likelihood" by A.W.F. Edwards
(1992, ISBN-13 : 978-0801844430), "Statistical Evidence" by R. Royall
(1997, ISBN-13 : 978-0412044113), S.N. Goodman & R. Royall (2011)
<doi:10.2105/AJPH.78.12.1568>, "Understanding Psychology as a Science" by
Z. Dienes (2008, ISBN-13 : 978-0230542310), S. Glover & P. Dixon
<https://link.springer.com/article/10.3758/BF03196706> and others. This
package accompanies "Evidence-Based Statistics" by P. Cahusac (2020,
ISBN-13 : 978-1119549802).

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
