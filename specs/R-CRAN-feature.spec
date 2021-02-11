%global packname  feature
%global packver   1.2.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.15
Release:          1%{?dist}%{?buildtag}
Summary:          Local Inferential Feature Significance for Multivariate Kernel Density Estimation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.4.0
Requires:         R-core >= 1.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ks >= 1.12.0
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-ks >= 1.12.0
Requires:         R-CRAN-plot3D 
Requires:         R-tcltk 

%description
Local inferential feature significance for multivariate kernel density
estimation.

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
