%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kpcaIG
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variables Interpretability with Kernel PCA

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-WallomicsData 
Requires:         R-grDevices 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-WallomicsData 

%description
The kernelized version of principal component analysis (KPCA) has proven
to be a valid nonlinear alternative for tackling the nonlinearity of
biological sample spaces. However, it poses new challenges in terms of the
interpretability of the original variables. 'kpcaIG' aims to provide a
tool to select the most relevant variables based on the kernel PCA
representation of the data as in Briscik et al. (2023)
<doi:10.1186/s12859-023-05404-y>. It also includes functions for 2D and 3D
visualization of the original variables (as arrows) into the kernel
principal components axes, highlighting the contribution of the most
important ones.

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
