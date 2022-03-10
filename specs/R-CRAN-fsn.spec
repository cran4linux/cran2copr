%global __brp_check_rpaths %{nil}
%global packname  fsn
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Rosenthal's Fail Safe Number and Related Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 

%description
Estimation of Rosenthal's fail safe number including confidence intervals.
The relevant papers are the following. Konstantinos C. Fragkos, Michail
Tsagris and Christos C. Frangos (2014). "Publication Bias in
Meta-Analysis: Confidence Intervals for Rosenthal's Fail-Safe Number".
International Scholarly Research Notices, Volume 2014.
<doi:10.1155/2014/825383>. Konstantinos C. Fragkos, Michail Tsagris and
Christos C. Frangos (2017). "Exploring the distribution for the estimator
of Rosenthal's fail-safe number of unpublished studies in meta-analysis".
Communications in Statistics-Theory and Methods, 46(11):5672--5684.
<doi:10.1080/03610926.2015.1109664>.

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
