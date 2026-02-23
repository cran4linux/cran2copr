%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimCop
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate from Arbitrary Copulae

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-rgl 
Requires:         R-stats 

%description
Provides a framework to generating random variates from arbitrary
multivariate copulae, while concentrating on (bivariate) extreme value
copulae.  Particularly useful if the multivariate copulae are not
available in closed form.  Detailed discussion of the methodologies used
can be found in Tajvidi and Turlach (2018) <doi:10.1111/anzs.12209>.

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
