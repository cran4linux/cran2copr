%global __brp_check_rpaths %{nil}
%global packname  AlphaPart
%global packver   0.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          Partition/Decomposition of Breeding Values by Paths of Information

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gdata >= 2.6.0
BuildRequires:    R-CRAN-pedigree >= 1.3
BuildRequires:    R-CRAN-directlabels >= 1.1
BuildRequires:    R-CRAN-Rcpp >= 0.9.4
BuildRequires:    R-CRAN-ggplot2 >= 0.8.9
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-gdata >= 2.6.0
Requires:         R-CRAN-pedigree >= 1.3
Requires:         R-CRAN-directlabels >= 1.1
Requires:         R-CRAN-Rcpp >= 0.9.4
Requires:         R-CRAN-ggplot2 >= 0.8.9
Requires:         R-CRAN-reshape 

%description
A software that implements a method for partitioning genetic trends to
quantify the sources of genetic gain in breeding programmes. The
partitioning method is described in Garcia-Cortes et al. (2008)
<doi:10.1017/S175173110800205X>. The package includes the main function
AlphaPart for partitioning breeding values and auxiliary functions for
manipulating data and summarizing, visualizing, and saving results.

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
