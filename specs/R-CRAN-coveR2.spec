%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coveR2
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Process Digital Cover Photography Images of Tree Crowns

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-autothresholdr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mgc 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-autothresholdr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mgc 
Requires:         R-CRAN-terra 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Process Digital Cover Photography images of tree canopies to get canopy
attributes like Foliage Cover and Leaf Area Index. Detailed description of
the methods in Chianucci et al. (2022) <doi:10.1007/s00468-018-1666-3>.

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
