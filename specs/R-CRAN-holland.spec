%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  holland
%global packver   0.1.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistics for Holland's Theory of Vocational Choice

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-mvtnorm 

%description
Offers a convenient way to compute parameters in the framework of the
theory of vocational choice introduced by J.L. Holland, (1997). A
comprehensive summary to this theory of vocational choice is given in
Holland, J.L. (1997). Making vocational choices. A theory of vocational
personalities and work environments. Lutz, FL: Psychological Assessment.

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
