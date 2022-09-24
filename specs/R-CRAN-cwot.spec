%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cwot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cauchy Weighted Joint Test for Pharmacogenetics Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SPAtest 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-SPAtest 
Requires:         R-CRAN-mvtnorm 

%description
A flexible and robust joint test of the single nucleotide polymorphism
(SNP) main effect and genotype-by-treatment interaction effect for
continuous and binary endpoints. Two analytic procedures, Cauchy weighted
joint test (CWOT) and adaptively weighted joint test (AWOT), are proposed
to accurately calculate the joint test p-value. The proposed methods are
evaluated through extensive simulations under various scenarios. The
results show that the proposed AWOT and CWOT control type I error well and
outperform existing methods in detecting the most interesting signal
patterns in pharmacogenetics (PGx) association studies. For reference, see
Hong Zhang, Devan Mehrotra and Judong Shen (2022)
<doi:10.13140/RG.2.2.28323.53280>.

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
