%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitPS
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Zeta Distributions to Forensic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ks 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-VGAM 

%description
Fits Zeta distributions (discrete power laws) to data that arises from
forensic surveys of clothing on the presence of glass and paint in various
populations. The general method is described to some extent in Coulson,
S.A., Buckleton, J.S., Gummer, A.B., and Triggs, C.M. (2001)
<doi:10.1016/S1355-0306(01)71847-3>, although the implementation differs.

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
