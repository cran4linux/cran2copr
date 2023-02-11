%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustering.sc.dp
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Distance-Based Clustering for Multidimensional Data with Sequential Constraint

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0

%description
A dynamic programming algorithm for optimal clustering multidimensional
data with sequential constraint. The algorithm minimizes the sum of
squares of within-cluster distances. The sequential constraint allows only
subsequent items of the input data to form a cluster. The sequential
constraint is typically required in clustering data streams or items with
time stamps such as video frames, GPS signals of a vehicle, movement data
of a person, e-pen data, etc. The algorithm represents an extension of
'Ckmeans.1d.dp' to multiple dimensional spaces. Similarly to the
one-dimensional case, the algorithm guarantees optimality and
repeatability of clustering. Method clustering.sc.dp() can find the
optimal clustering if the number of clusters is known. Otherwise, methods
findwithinss.sc.dp() and backtracking.sc.dp() can be used. See Szkaliczki,
T. (2016) "clustering.sc.dp: Optimal Clustering with Sequential Constraint
by Using Dynamic Programming" <doi: 10.32614/RJ-2016-022> for more
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
