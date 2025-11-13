%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deepspat
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Deep Compositional Spatial Models

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-tfprobability 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-SpatialExtremes 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-tfprobability 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-SpatialExtremes 
Requires:         R-CRAN-fields 

%description
Deep compositional spatial models are standard spatial covariance models
coupled with an injective warping function of the spatial domain. The
warping function is constructed through a composition of multiple
elemental injective functions in a deep-learning framework. The package
implements two cases for the univariate setting; first, when these warping
functions are known up to some weights that need to be estimated, and,
second, when the weights in each layer are random. In the multivariate
setting only the former case is available. Estimation and inference is
done using 'tensorflow', which makes use of graphics processing units. For
more details see Zammit-Mangion et al. (2022)
<doi:10.1080/01621459.2021.1887741>, Vu et al. (2022)
<doi:10.5705/ss.202020.0156>, and Vu et al. (2023)
<doi:10.1016/j.spasta.2023.100742>.

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
