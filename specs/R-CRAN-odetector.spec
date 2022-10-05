%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  odetector
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Outlier Detection Using Partitioning Clustering Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ppclust 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ppclust 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
An object is called "outlier" if it remarkably deviates from the other
objects in a data set. Outlier detection is the process to find outliers
by using the methods that are based on distance measures, clustering and
spatial methods (Ben-Gal, 2005 <ISBN 0-387-24435-2>). It is one of the
intensively studied research topics for identification of novelties,
frauds, anomalies, deviations or exceptions in addition to its use for
outlier removing in data processing. This package provides the
implementations of some novel approaches to detect the outliers based on
typicality degrees that are obtained with the soft partitioning clustering
algorithms such as Fuzzy C-means and its variants.

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
