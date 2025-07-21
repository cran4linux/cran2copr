%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  upset.hp
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Generate UpSet Plots of VP and HP Based on the ASV Concept

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-glmm.hp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-glmm.hp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-grDevices 

%description
Using matrix layout to visualize the unique, common, or individual
contribution of each predictor (or matrix of predictors) towards explained
variation on different models. These contributions were derived from
variation partitioning (VP) and hierarchical partitioning (HP), applying
the algorithm of "Lai et al. (2022) Generalizing hierarchical and
variation partitioning in multiple regression and canonical analyses using
the rdacca.hp R package.Methods in Ecology and Evolution, 13: 782-788
<doi:10.1111/2041-210X.13800>".

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
