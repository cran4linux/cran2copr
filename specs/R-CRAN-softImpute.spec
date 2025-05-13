%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  softImpute
%global packver   1.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Matrix Completion via Iterative Soft-Thresholded SVD

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
Iterative methods for matrix completion that use nuclear-norm
regularization. There are two main approaches.The one approach uses
iterative soft-thresholded svds to impute the missing values. The second
approach uses alternating least squares. Both have an 'EM' flavor, in that
at each iteration the matrix is completed with the current estimate. For
large matrices there is a special sparse-matrix class named "Incomplete"
that efficiently handles all computations. The package includes procedures
for centering and scaling rows, columns or both, and for computing
low-rank SVDs on large sparse centered matrices (i.e. principal
components).

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
