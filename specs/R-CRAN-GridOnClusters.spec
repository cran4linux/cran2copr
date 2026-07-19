%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GridOnClusters
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster-Preserving Multivariate Joint Grid Discretization

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Ckmeans.1d.dp 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fossil 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Ckmeans.1d.dp 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fossil 
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-plotrix 

%description
Discretize multivariate continuous data using a grid to capture the joint
distribution that preserves clusters in original data (Wang et al 2020)
<doi:10.1145/3388440.3412415>. It can handle both labeled or unlabeled
data. Joint grid discretization can prepare data for model-free inference
of association, function, or causality.

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
