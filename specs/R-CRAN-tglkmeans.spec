%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tglkmeans
%global packver   0.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Implementation of K-Means++ Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-parallel >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-tgstat >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-purrr >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-parallel >= 3.3.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-tgstat >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-purrr >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-future 
Requires:         R-CRAN-magrittr 

%description
Efficient implementation of K-Means++ algorithm. For more information see
(1) "kmeans++ the advantages of the k-means++ algorithm" by David Arthur
and Sergei Vassilvitskii (2007), Proceedings of the eighteenth annual
ACM-SIAM symposium on Discrete algorithms, Society for Industrial and
Applied Mathematics, Philadelphia, PA, USA, pp. 1027-1035,
<http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf>, and (2) "The
Effectiveness of Lloyd-Type Methods for the k-Means Problem" by Rafail
Ostrovsky, Yuval Rabani, Leonard J. Schulman and Chaitanya Swamy
<doi:10.1145/2395116.2395117>.

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
