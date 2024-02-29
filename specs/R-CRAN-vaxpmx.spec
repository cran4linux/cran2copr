%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vaxpmx
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Vaccines Pharmacometrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.6
BuildRequires:    R-methods >= 3.5.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.51.6
Requires:         R-methods >= 3.5.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-stats 

%description
Estimate vaccine efficacy (VE) using immunogenicity data. The inclusion of
immunogenicity data in regression models can increase precision in VE. The
methods are described in the publication "Elucidating vaccine efficacy
using a correlate of protection, demographics, and logistic regression" by
Julie Dudasova, Zdenek Valenta, and Jeffrey R. Sachs (2024).

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
