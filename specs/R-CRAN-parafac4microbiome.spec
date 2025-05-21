%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parafac4microbiome
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Factor Analysis Modelling of Longitudinal Microbiome Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mize 
BuildRequires:    R-CRAN-multiway 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-mize 
Requires:         R-CRAN-multiway 
Requires:         R-parallel 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rTensor 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Creation and selection of PARAllel FACtor Analysis (PARAFAC) models of
longitudinal microbiome data. You can import your own data with our import
functions or use one of the example datasets to create your own PARAFAC
models. Selection of the optimal number of components can be done using
assessModelQuality() and assessModelStability(). The selected model can
then be plotted using plotPARAFACmodel(). The Parallel Factor Analysis
method was originally described by Caroll and Chang (1970)
<doi:10.1007/BF02310791> and Harshman (1970)
<https://www.psychology.uwo.ca/faculty/harshman/wpppfac0.pdf>.

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
