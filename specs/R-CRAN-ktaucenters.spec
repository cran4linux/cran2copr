%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ktaucenters
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Clustering Procedures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-GSE 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-GSE 

%description
A clustering algorithm similar to K-Means is implemented, it has two main
advantages, namely (a) The estimator is resistant to outliers, that means
that results of estimator are still correct when there are atypical values
in the sample and (b) The estimator is efficient, roughly speaking, if
there are no outliers in the sample, results will be similar to those
obtained by a classic algorithm (K-Means). Clustering procedure is carried
out by minimizing the overall robust scale so-called tau scale. (see
Gonzalez, Yohai and Zamar (2019) <arxiv:1906.08198>).

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
