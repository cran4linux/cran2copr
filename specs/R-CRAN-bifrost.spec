%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bifrost
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Branch-Level Inference Framework for Recognizing Optimal Shifts in Traits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvMORPH 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-txtplot 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-phytools 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-mvMORPH 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-txtplot 

%description
Methods for detecting and visualizing cladogenic shifts in multivariate
trait data on phylogenies. Implements penalized-likelihood multivariate
generalized least squares models, enabling analyses of high-dimensional
trait datasets and large trees via searchOptimalConfiguration(). Includes
a greedy step-wise shift-search algorithm following approaches developed
in Smith et al. (2023) <doi:10.1111/nph.19099> and Berv et al. (2024)
<doi:10.1126/sciadv.adp0114>. Methods build on multivariate GLS approaches
described in Clavel et al. (2019) <doi:10.1093/sysbio/syy045> and
implemented in the mvgls() function from the 'mvMORPH' package.
Documentation and vignettes are available at
<https://jakeberv.com/bifrost/>, including the introductory vignette at
<https://jakeberv.com/bifrost/articles/jaw-shape-vignette.html>.

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
