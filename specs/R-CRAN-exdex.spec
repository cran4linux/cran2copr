%global __brp_check_rpaths %{nil}
%global packname  exdex
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the Extremal Index

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-chandwich 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-chandwich 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppRoll 
Requires:         R-stats 

%description
Performs frequentist inference for the extremal index of a stationary time
series.  Two types of methodology are used.  One type is based on a model
that relates the distribution of block maxima to the marginal distribution
of series and leads to the semiparametric maxima estimators described in
Northrop (2015) <doi:10.1007/s10687-015-0221-5> and Berghaus and Bucher
(2018) <doi:10.1214/17-AOS1621>.  Sliding block maxima are used to
increase precision of estimation. A graphical block size diagnostic is
provided.  The other type of methodology uses a model for the distribution
of threshold inter-exceedance times (Ferro and Segers (2003)
<doi:10.1111/1467-9868.00401>). Three versions of this type of approach
are provided: the iterated weight least squares approach of Suveges (2007)
<doi:10.1007/s10687-007-0034-2>, the K-gaps model of Suveges and Davison
(2010) <doi:10.1214/09-AOAS292> and a similar approach of Holesovsky, J.
and Fusek, M. (2020) <doi:10.1007/s10687-020-00374-3> that we refer to as
D-gaps. For the K-gaps and D-gaps models this package allows missing
values in the data, can accommodate independent subsets of data, such as
monthly or seasonal time series from different years, and can incorporate
information from right-censored inter-exceedance times. Graphical
diagnostics for the threshold level and the respective tuning parameters K
and D are provided.

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
