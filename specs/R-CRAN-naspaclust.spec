%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  naspaclust
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nature-Inspired Spatial Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rdist 
BuildRequires:    R-CRAN-stabledist 
BuildRequires:    R-CRAN-beepr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rdist 
Requires:         R-CRAN-stabledist 
Requires:         R-CRAN-beepr 

%description
Implement and enhance the performance of spatial fuzzy clustering using
Fuzzy Geographically Weighted Clustering with various optimization
algorithms, mainly from Xin She Yang (2014) <ISBN:9780124167438> with book
entitled Nature-Inspired Optimization Algorithms. The optimization
algorithm is useful to tackle the disadvantages of clustering
inconsistency when using the traditional approach. The distance
measurements option is also provided in order to increase the quality of
clustering results. The Fuzzy Geographically Weighted Clustering with
nature inspired optimisation algorithm was firstly developed by Arie Wahyu
Wijayanto and Ayu Purwarianti (2014) <doi:10.1109/CITSM.2014.7042178>
using Artificial Bee Colony algorithm.

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
