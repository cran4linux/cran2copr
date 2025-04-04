%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  braQCA
%global packver   1.4.11.27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.11.27
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrapped Robustness Assessment for Qualitative Comparative Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-QCA 
BuildRequires:    R-CRAN-bootstrap 
Requires:         R-CRAN-QCA 
Requires:         R-CRAN-bootstrap 

%description
Test the robustness of a user's Qualitative Comparative Analysis solutions
to randomness, using the bootstrapped assessment: baQCA(). This package
also includes a function that provides recommendations for improving
solutions to reach typical significance levels: brQCA(). Data included
come from McVeigh et al. (2014) <doi:10.1177/0003122414534065>.

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
