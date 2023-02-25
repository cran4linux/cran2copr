%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frequencyConnectedness
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Spectral Decomposition of Connectedness Measures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-methods 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-pbapply 
Requires:         R-methods 

%description
Accompanies a paper (Barunik, Krehlik (2018) <doi:10.1093/jjfinec/nby001>)
dedicated to spectral decomposition of connectedness measures and their
interpretation. We implement all the developed estimators as well as the
historical counterparts. For more information, see the help or GitHub page
(<https://github.com/tomaskrehlik/frequencyConnectedness>) for relevant
information.

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
