%global __brp_check_rpaths %{nil}
%global packname  KFPCA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kendall Functional Principal Component Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-kader 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-fdapace 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-kader 
Requires:         R-utils 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-fdapace 
Requires:         R-CRAN-fda 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implementation for Kendall functional principal component analysis.
Kendall functional principal component analysis is a robust functional
principal component analysis technique for non-Gaussian
functional/longitudinal data. The crucial function of this package is
KFPCA(). Moreover, least square estimates of functional principal
component scores are also provided. Refer to <arXiv:2102.00911>.

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
