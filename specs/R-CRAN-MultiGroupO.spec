%global __brp_check_rpaths %{nil}
%global packname  MultiGroupO
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          MultiGroup Method and Simulation Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-plsgenomics 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-mgm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-expm 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-plsgenomics 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-mgm 

%description
Two method new of multigroup and simulation of data. The first technique
called multigroup PCA (mgPCA) this multivariate exploration approach that
has the idea of considering the structure of groups and / or different
types of variables. On the other hand, the second multivariate technique
called Multigroup Dimensionality Reduction (MDR) it is another
multivariate exploration method that is based on projections. In addition,
a method called Single Dimension Exploration (SDE) was incorporated for to
analyze the exploration of the data. It could help us in a better way to
observe the behavior of the multigroup data with certain variables of
interest.

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
