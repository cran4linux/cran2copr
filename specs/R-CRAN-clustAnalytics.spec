%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustAnalytics
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Cluster Evaluation on Graphs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mcclust 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-fossil 
BuildRequires:    R-CRAN-aricode 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mcclust 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-fossil 
Requires:         R-CRAN-aricode 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rdpack 

%description
Evaluates the stability and significance of clusters on 'igraph' graphs.
Supports weighted and unweighted graphs. Implements the cluster evaluation
methods defined by Arratia A, Renedo M (2021) <doi:10.7717/peerj-cs.600>.
Also includes an implementation of the Reduced Mutual Information
introduced by Newman et al. (2020) <doi:10.1103/PhysRevE.101.042304>.

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
