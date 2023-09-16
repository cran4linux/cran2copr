%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remotePARTS
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Spatiotemporal Autoregression Analyses for Large Data Sets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-geosphere >= 1.5.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-geosphere >= 1.5.10
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-stats 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-doParallel 

%description
These tools were created to test map-scale hypotheses about trends in
large remotely sensed data sets but any data with spatial and temporal
variation can be analyzed. Tests are conducted using the PARTS method for
analyzing spatially autocorrelated time series (Ives et al., 2021:
<doi:10.1016/j.rse.2021.112678>). The method's unique approach can handle
extremely large data sets that other spatiotemporal models cannot, while
still appropriately accounting for spatial and temporal autocorrelation.
This is done by partitioning the data into smaller chunks, analyzing
chunks separately and then combining the separate analyses into a single,
correlated test of the map-scale hypotheses.

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
