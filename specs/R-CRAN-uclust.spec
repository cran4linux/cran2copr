%global __brp_check_rpaths %{nil}
%global packname  uclust
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering and Classification Inference with U-Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-robcor 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-robcor 

%description
Clustering and classification inference for high dimension low sample size
(HDLSS) data with U-statistics. The package contains implementations of
nonparametric statistical tests for sample homogeneity, group separation,
clustering, and classification of multivariate data. The methods have high
statistical power and are tailored for data in which the dimension L is
much larger than sample size n. See Gabriela B. Cybis, Marcio Valk and
Sílvia RC Lopes (2018) <doi:10.1080/00949655.2017.1374387>, Marcio Valk
and Gabriela B. Cybis (2020) <doi:10.1080/10618600.2020.1796398>, Debora
Z. Bello, Marcio Valk and Gabriela B. Cybis (2021) <arXiv:2106.09115>.

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
