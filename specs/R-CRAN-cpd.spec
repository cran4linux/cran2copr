%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cpd
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Complex Pearson Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-dgof 
BuildRequires:    R-graphics 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-dgof 
Requires:         R-graphics 

%description
Probability mass function, distribution function, quantile function and
random generation for the Complex Triparametric Pearson (CTP) and Complex
Biparametric Pearson (CBP) distributions developed by Rodriguez-Avi et al
(2003) <doi:10.1007/s00362-002-0134-7>, Rodriguez-Avi et al (2004)
<doi:10.1007/BF02778271> and Olmo-Jimenez et al (2018)
<doi:10.1080/00949655.2018.1482897>. The package also contains
maximum-likelihood fitting functions for these models.

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
