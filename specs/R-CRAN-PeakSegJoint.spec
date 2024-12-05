%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PeakSegJoint
%global packver   2024.12.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.12.4
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Peak Detection in Several ChIP-Seq Samples

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-PeakError 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-penaltyLearning 
Requires:         R-CRAN-PeakError 
Requires:         R-parallel 
Requires:         R-CRAN-penaltyLearning 

%description
Jointly segment several ChIP-seq samples to find the peaks which are the
same and different across samples. The fast approximate maximum Poisson
likelihood algorithm is described in "PeakSegJoint: fast supervised peak
detection via joint segmentation of multiple count data samples"
<doi:10.48550/arXiv.1506.01286> by TD Hocking and G Bourque.

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
