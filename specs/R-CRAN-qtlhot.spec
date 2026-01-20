%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qtlhot
%global packver   1.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Inference for QTL Hotspots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-broman 
Requires:         R-stats 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-mnormt 
Requires:         R-utils 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-broman 

%description
Functions to infer co-mapping trait hotspots and causal models. Chaibub
Neto E, Keller MP, Broman AF, Attie AD, Jansen RC, Broman KW, Yandell BS
(2012) Quantile-based permutation thresholds for QTL hotspots. Genetics
191 : 1355-1365. <doi:10.1534/genetics.112.139451>. Chaibub Neto E, Broman
AT, Keller MP, Attie AD, Zhang B, Zhu J, Yandell BS (2013) Modeling
causality for pairs of phenotypes in system genetics. Genetics 193 :
1003-1013. <doi:10.1534/genetics.112.147124>.

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
