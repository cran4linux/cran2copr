%global packname  LogConcDEAD
%global packver   1.6-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Log-Concave Density Estimation in Arbitrary Dimensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mvtnorm 

%description
Software for computing a log-concave (maximum likelihood) estimator for
i.i.d. data in any number of dimensions. For a detailed description of the
method see Cule, Samworth and Stewart (2010, Journal of Royal Statistical
Society Series B, <doi:10.1111/j.1467-9868.2010.00753.x>).

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
