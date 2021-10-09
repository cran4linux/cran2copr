%global __brp_check_rpaths %{nil}
%global packname  FADPclust
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Data Clustering Using Adaptive Density Peak Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MFPCA 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-funData 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-MFPCA 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-funData 
Requires:         R-stats 
Requires:         R-graphics 

%description
An implementation of a clustering algorithm for functional data based on
adaptive density peak detection technique, in which the density is
estimated by functional k-nearest neighbor density estimation based on a
proposed semi-metric between functions. The proposed functional data
clustering algorithm is computationally fast since it does not need
iterative process. (Alex Rodriguez and Alessandro Laio (2014)
<doi:10.1126/science.1242072>; Xiao-Feng Wang and Yifan Xu (2016)
<doi:10.1177/0962280215609948>).

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
