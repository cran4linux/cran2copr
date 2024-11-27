%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ehymet
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Methodologies for Functional Data Based on the Epigraph and Hypograph Indices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-clusterCrit 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tf 
Requires:         R-CRAN-clusterCrit 
Requires:         R-CRAN-kernlab 
Requires:         R-stats 
Requires:         R-CRAN-tf 

%description
Implements methods for functional data analysis based on the epigraph and
hypograph indices. These methods transform functional datasets, whether in
one or multiple dimensions, into multivariate datasets. The transformation
involves applying the epigraph, hypograph, and their modified versions to
both the original curves and their first and second derivatives. The
calculation of these indices is tailored to the dimensionality of the
functional dataset, with special considerations for dependencies between
dimensions in multidimensional cases. This approach extends traditional
multivariate data analysis techniques to the functional data setting. A
key application of this package is the EHyClus method, which enhances
clustering analysis for functional data across one or multiple dimensions
using the epigraph and hypograph indices. See Pulido et al. (2023)
<doi:10.1007/s11222-023-10213-7> and Pulido et al. (2024)
<doi:10.48550/arXiv.2307.16720>.

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
