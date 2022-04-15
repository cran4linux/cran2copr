%global __brp_check_rpaths %{nil}
%global packname  ks
%global packver   1.13.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.5
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Smoothing

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-KernSmooth >= 2.22
BuildRequires:    R-CRAN-FNN >= 1.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-multicool 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-KernSmooth >= 2.22
Requires:         R-CRAN-FNN >= 1.1
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-multicool 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-pracma 

%description
Kernel smoothers for univariate and multivariate data, including
densities, density derivatives, cumulative distributions, clustering,
classification, density ridges, significant modal regions, and two-sample
hypothesis tests. Chacon & Duong (2018) <doi:10.1201/9780429485572>.

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
