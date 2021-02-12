%global packname  HeteroGGM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Graphical Model-Based Heterogeneity Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 

%description
The goal of this package is to user-friendly realizing Gaussian graphical
model-based heterogeneity analysis. Recently, several Gaussian graphical
model-based heterogeneity analysis techniques have been developed. A
common methodological limitation is that the number of subgroups is
assumed to be known a priori, which is not realistic. In a very recent
study (Ren et al., 2021), a novel approach based on the penalized fusion
technique is developed to fully data-dependently determine the number and
structure of subgroups in Gaussian graphical model-based heterogeneity
analysis. It opens the door for utilizing the Gaussian graphical model
technique in more practical settings. Beyond Ren et al. (2021), more
estimations and functions are added, so that the package is self-contained
and more comprehensive and can provide "more direct" insights to
practitioners (with the visualization function). Reference: Ren, M., Zhang
S., Zhang Q. and Ma S. (2021). Gaussian Graphical Model-based
Heterogeneity Analysis via Penalized Fusion. Biometrics,
<doi:10.1111/biom.13426>.

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
