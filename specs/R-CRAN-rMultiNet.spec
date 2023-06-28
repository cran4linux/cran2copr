%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rMultiNet
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Layer Networks Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-stats 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rTensor 
Requires:         R-stats 

%description
Provides two general frameworks to generate a multi-layer network. This
also provides several methods to reveal the embedding of both nodes and
layers. The reference paper can be found from the URL mentioned below.
Ting Li, Zhongyuan Lyu, Chenyu Ren, Dong Xia (2023) <arXiv:2302.04437>.

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
