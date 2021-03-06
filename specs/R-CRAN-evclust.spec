%global packname  evclust
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evidential Clustering

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-MASS 

%description
Various clustering algorithms that produce a credal partition, i.e., a set
of Dempster-Shafer mass functions representing the membership of objects
to clusters. The mass functions quantify the cluster-membership
uncertainty of the objects. The algorithms are: Evidential c-Means,
Relational Evidential c-Means, Constrained Evidential c-Means, Evidential
Clustering, Constrained Evidential Clustering, Evidential
K-nearest-neighbor-based Clustering, Bootstrap Model-Based Evidential
Clustering, Belief Peak Evidential Clustering, Neural-Network-based
Evidential Clustering.

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
