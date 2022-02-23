%global __brp_check_rpaths %{nil}
%global packname  clusterCons
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Consensus Clustering using Multiple Algorithms and Parameters

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-apcluster 
Requires:         R-methods 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grid 
Requires:         R-CRAN-apcluster 

%description
Functions for calculation of robustness measures for clusters and cluster
membership based on generating consensus matrices from bootstrapped
clustering experiments in which a random proportion of rows of the data
set are used in each individual clustering. This allows the user to
prioritise clusters and the members of clusters based on their consistency
in this regime. The functions allow the user to select several algorithms
to use in the re-sampling scheme and with any of the parameters that the
algorithm would normally take. See Simpson, T. I., Armstrong, J. D. &
Jarman, A. P. (2010) <doi:10.1186/1471-2105-11-590> and Monti, S., Tamayo,
P., Mesirov, J. & Golub, T. (2003) <doi:10.1023/a:1023949509487>.

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
