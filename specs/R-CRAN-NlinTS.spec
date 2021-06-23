%global __brp_check_rpaths %{nil}
%global packname  NlinTS
%global packver   1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Models for Non Linear Causality Detection in Time Series

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-Rdpack 

%description
Models for non-linear time series analysis and causality detection. The
main functionalities of this package consist of an implementation of the
classical causality test (C.W.J.Granger 1980)
<doi:10.1016/0165-1889(80)90069-X>, and a non-linear version of it based
on feed-forward neural networks. This package contains also an
implementation of the Transfer Entropy <doi:10.1103/PhysRevLett.85.461>,
and the continuous Transfer Entropy using an approximation based on the
k-nearest neighbors <doi:10.1103/PhysRevE.69.066138>. There are also some
other useful tools, like the VARNN (Vector Auto-Regressive Neural Network)
prediction model, the Augmented test of stationarity, and the discrete and
continuous entropy and mutual information.

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
