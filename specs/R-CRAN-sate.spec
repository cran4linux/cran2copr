%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sate
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Scientific Analysis of Trial Errors (SATE)

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-ellipse 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 

%description
Bundles functions used to analyze the harmfulness of trial errors in
criminal trials. Functions in the Scientific Analysis of Trial Errors
('SATE') package help users estimate the probability that a jury will find
a defendant guilty given jurors' preferences for a guilty verdict and the
uncertainty of that estimate. Users can also compare actual and
hypothetical trial conditions to conduct harmful error analysis. The
relationship between individual jurors' verdict preferences and the
probability that a jury returns a guilty verdict has been studied by Davis
(1973) <doi:10.1037/h0033951>; MacCoun & Kerr (1988)
<doi:10.1037/0022-3514.54.1.21>, and Devine et el. (2001)
<doi:10.1037/1076-8971.7.3.622>, among others.

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
