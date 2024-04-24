%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  collpcm
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Collapsed Latent Position Cluster Model for Social Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-latentnet 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-network 
Requires:         R-CRAN-latentnet 
Requires:         R-CRAN-gtools 

%description
Markov chain Monte Carlo based inference routines for collapsed latent
position cluster models or social networks, which includes searches over
the model space (number of clusters in the latent position cluster model).
The label switching algorithm used is that of Nobile and Fearnside (2007)
<doi:10.1007/s11222-006-9014-7> which relies on the algorithm of Carpaneto
and Toth (1980) <doi:10.1145/355873.355883>.

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
