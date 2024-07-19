%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scellpam
%global packver   1.4.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Applying Partitioning Around Medoids to Single Cell Data with High Number of Cells

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-memuse >= 4.2.1
BuildRequires:    R-CRAN-cluster >= 2.1.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-memuse >= 4.2.1
Requires:         R-CRAN-cluster >= 2.1.4
Requires:         R-CRAN-Rcpp >= 1.0.8

%description
PAM (Partitioning Around Medoids) algorithm application to samples of
single cell sequencing techniques with a high number of cells (as many as
the computer memory allows). The package uses a binary format to store
matrices (either full, sparse or symmetric) in files written in the disk
that can contain any data type (not just double) which allows its
manipulation when memory is sufficient to load them as int or float, but
not as double. The PAM implementation is done in parallel, using
several/all the cores of the machine, if it has them. This package shares
a great part of its code with packages 'jmatrix' and 'parallelpam' but
their functionality is included here so there is no need to install them.

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
