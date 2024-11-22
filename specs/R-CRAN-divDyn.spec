%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  divDyn
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Diversity Dynamics using Fossil Sampling Data

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Functions to describe sampling and diversity dynamics of fossil occurrence
datasets (e.g. from the Paleobiology Database). The package includes
methods to calculate range- and occurrence-based metrics of taxonomic
richness, extinction and origination rates, along with traditional
sampling measures. A powerful subsampling tool is also included that
implements frequently used sampling standardization methods in a multiple
bin-framework. The plotting of time series and the occurrence data can be
simplified by the functions incorporated in the package, as well as other
calculations, such as environmental affinities and extinction selectivity
testing. Details can be found in: Kocsis, A.T.; Reddin, C.J.; Alroy, J.
and Kiessling, W. (2019) <doi:10.1101/423780>.

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
