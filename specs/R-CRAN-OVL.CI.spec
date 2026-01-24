%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OVL.CI
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Inference on the Overlap Coefficient

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-stats 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mixtools 
Requires:         R-stats 

%description
Provides functions to construct confidence intervals for the Overlap
Coefficient (OVL). OVL measures the similarity between two distributions
through the overlapping area of their distribution functions. Given its
intuitive description and ease of visual representation by the
straightforward depiction of the amount of overlap between the two
corresponding histograms based on samples of measurements from each one of
the two distributions, the development of accurate methods for confidence
interval construction can be useful for applied researchers. Implements
methods based on the work of Franco-Pereira, A.M., Nakas, C.T., Reiser,
B., and Pardo, M.C. (2021) <doi:10.1177/09622802211046386> as well as
extensions for multimodal distributions proposed by Alcaraz-Peñalba, A.,
Franco-Pereira, A., and Pardo, M.C. (2025)
<doi:10.1007/s10182-025-00545-2>.

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
