%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tip
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Clustering Using the Table Invitation Prior (TIP)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mniw 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-network 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-changepoint 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-mniw 

%description
Cluster data without specifying the number of clusters using the Table
Invitation Prior (TIP) introduced in the paper "Clustering Gene Expression
Using the Table Invitation Prior" by Charles W. Harrison, Qing He, and
Hsin-Hsiung Huang (2022) <doi:10.3390/genes13112036>. TIP is a Bayesian
prior that uses pairwise distance and similarity information to cluster
vectors, matrices, or tensors.

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
