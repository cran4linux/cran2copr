%global __brp_check_rpaths %{nil}
%global packname  BayesCACE
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Model for CACE Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Rdpack 
Requires:         R-grDevices 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-lme4 

%description
Performs CACE (Complier Average Causal Effect analysis) on either a single
study or meta-analysis of datasets with binary outcomes, using either
complete or incomplete noncompliance information. Our package implements
the Bayesian methods proposed in Zhou et al. (2019)
<doi:10.1111/biom.13028>, which introduces a Bayesian hierarchical model
for estimating CACE in meta-analysis of clinical trials with
noncompliance, and Zhou et al. (2021) <doi:10.1080/01621459.2021.1900859>,
with an application example on Epidural Analgesia.

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
