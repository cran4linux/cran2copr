%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixAK
%global packver   5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Normal Mixture Models and Mixtures of Generalized Linear Mixed Models Including Model Based Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-CRAN-colorspace 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-splines 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-mnormt 
Requires:         R-parallel 
Requires:         R-CRAN-coda 

%description
Contains a mixture of statistical methods including the MCMC methods to
analyze normal mixtures. Additionally, model based clustering methods are
implemented to perform classification based on (multivariate) longitudinal
(or otherwise correlated) data. The basis for such clustering is a mixture
of multivariate generalized linear mixed models. The package is primarily
related to the publications Komárek (2009, Comp. Stat. and Data Anal.)
<doi:10.1016/j.csda.2009.05.006> and Komárek and Komárková (2014, J. of
Stat. Soft.) <doi:10.18637/jss.v059.i12>. It also implements methods
published in Komárek and Komárková (2013, Ann. of Appl. Stat.)
<doi:10.1214/12-AOAS580>, Hughes, Komárek, Bonnett, Czanner, García-Fiñana
(2017, Stat. in Med.) <doi:10.1002/sim.7397>, Jaspers, Komárek, Aerts
(2018, Biom. J.) <doi:10.1002/bimj.201600253> and Hughes, Komárek,
Czanner, García-Fiñana (2018, Stat. Meth. in Med. Res)
<doi:10.1177/0962280216674496>.

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
