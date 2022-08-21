%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KODAMA
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Knowledge Discovery by Accuracy Maximization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-stats 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-Rtsne 

%description
An unsupervised and semi-supervised learning algorithm that performs
feature extraction from noisy and high-dimensional data. It facilitates
identification of patterns representing underlying groups on all samples
in a data set. Based on Cacciatore S, Tenori L, Luchinat C, Bennett PR,
MacIntyre DA. (2017) Bioinformatics <doi:10.1093/bioinformatics/btw705>
and Cacciatore S, Luchinat C, Tenori L. (2014) Proc Natl Acad Sci USA
<doi:10.1073/pnas.1220873111>.

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
