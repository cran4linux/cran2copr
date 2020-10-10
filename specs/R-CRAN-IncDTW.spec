%global packname  IncDTW
%global packver   1.1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Incremental Calculation of Dynamic Time Warping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-data.table 

%description
The Dynamic Time Warping (DTW) distance measure for time series allows
non-linear alignments of time series to match similar patterns in time
series of different lengths and or different speeds. IncDTW is
characterized by (1) the incremental calculation of DTW (reduces runtime
complexity to a linear level for updating the DTW distance) - especially
for life data streams or subsequence matching, (2) the vector based
implementation of DTW which is faster because no matrices are allocated
(reduces the space complexity from a quadratic to a linear level in the
number of observations) - for all runtime intensive DTW computations, (3)
the subsequence matching algorithm runDTW, that efficiently finds the k-NN
to a query pattern in a long time series, and (4) C++ in the heart. For
details about DTW see the original paper "Dynamic programming algorithm
optimization for spoken word recognition" by Sakoe and Chiba (1978)
<DOI:10.1109/TASSP.1978.1163055>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
