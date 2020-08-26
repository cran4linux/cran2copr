%global packname  rflexscan
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Flexible Spatial Scan Statistic

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rgdal 
Requires:         R-grDevices 
Requires:         R-CRAN-sp 

%description
Functions for the detection of spatial clusters using the flexible spatial
scan statistic developed by Tango and Takahashi (2005)
<doi:10.1186/1476-072X-4-11>. This package implements a wrapper for the C
routine used in the FleXScan 3.1.2
<https://sites.google.com/site/flexscansoftware/home> developed by
Takahashi, Yokoyama, and Tango.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
