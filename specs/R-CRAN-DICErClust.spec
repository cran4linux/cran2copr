%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DICErClust
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Deep Significance Clustering for Clinical Risk Stratification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-argparser 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-argparser 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-pROC 

%description
We provide an R implementation of Deep Significance Clustering (DICE), a
self-supervised learning framework designed to identify clinically
meaningful and risk-stratified patient subgroups from electronic health
record (EHR) data. DICE jointly optimizes deep representation learning,
clustering, and outcome prediction while enforcing statistical
significance between predicted outcomes and cluster membership. This
integrated optimization produces subgroups that are both clinically
coherent and predictive, addressing a gap where traditional unsupervised
clustering methods and supervised risk prediction models alone may fail to
generate actionable clinical groupings. See Huang et al. (2021)
<doi:10.1093/jamia/ocab203>.

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
