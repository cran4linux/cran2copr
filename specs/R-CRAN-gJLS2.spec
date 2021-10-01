%global __brp_check_rpaths %{nil}
%global packname  gJLS2
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Generalized Joint Location and Scale Framework for Association Testing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-moments 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-moments 

%description
An update to the Joint Location-Scale (JLS) testing framework that
identifies associated SNPs, gene-sets and pathways with main and/or
interaction effects on quantitative traits (Soave et al., 2015;
<doi:10.1016/j.ajhg.2015.05.015>). The JLS method simultaneously tests the
null hypothesis of equal mean and equal variance across genotypes, by
aggregating association evidence from the individual location/mean-only
and scale/variance-only tests using Fisher's method. The generalized joint
location-scale (gJLS) framework has been developed to deal specifically
with sample correlation and group uncertainty (Soave and Sun, 2017;
<doi:10.1111/biom.12651>). The current release: gJLS2, include additional
functionalities that enable analyses of X-chromosome genotype data through
novel methods for location (Chen et al., 2021; <doi:10.1002/gepi.22422>)
and scale (Deng et al., 2019; <doi:10.1002/gepi.22247>).

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
