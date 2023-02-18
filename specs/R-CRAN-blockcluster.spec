%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blockcluster
%global packver   4.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Co-Clustering Package for Binary, Categorical, Contingency and Continuous Data-Sets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-rtkore >= 1.5.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-rtkore >= 1.5.5
Requires:         R-methods 

%description
Simultaneous clustering of rows and columns, usually designated by
biclustering, co-clustering or block clustering, is an important technique
in two way data analysis. It consists of estimating a mixture model which
takes into account the block clustering problem on both the individual and
variables sets. The 'blockcluster' package provides a bridge between the
C++ core library build on top of the 'STK++' library, and the R
statistical computing environment. This package allows to co-cluster
binary <doi:10.1016/j.csda.2007.09.007>, contingency
<doi:10.1080/03610920903140197>, continuous
<doi:10.1007/s11634-013-0161-3> and categorical data-sets
<doi:10.1007/s11222-014-9472-2>. It also provides utility functions to
visualize the results. This package may be useful for various applications
in fields of Data mining, Information retrieval, Biology, computer vision
and many more. More information about the project and comprehensive
tutorial can be found on the link mentioned in URL.

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
