%global packname  singcar
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Comparing Single Cases to Small Samples

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-CholWishart 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-withr 
Requires:         R-stats 
Requires:         R-CRAN-CholWishart 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-withr 

%description
When comparing single cases to control populations and no parameters are
known researchers and clinicians must estimate these with a control
sample. This is often done when testing a case's abnormality on some
variable or testing abnormality of the discrepancy between two variables.
Appropriate frequentist and Bayesian methods for doing this are here
implemented, including tests allowing for the inclusion of covariates.
These have been developed first and foremost by John Crawford and Paul
Garthwaite, e.g. in Crawford and Howell (1998)
<doi:10.1076/clin.12.4.482.7241>, Crawford and Garthwaite (2005)
<doi:10.1037/0894-4105.19.3.318>, Crawford and Garthwaite (2007)
<doi:10.1080/02643290701290146> and Crawford, Garthwaite and Ryan (2011)
<doi:10.1016/j.cortex.2011.02.017>. The package is also equipped with
power calculators for each method.

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
