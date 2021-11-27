%global __brp_check_rpaths %{nil}
%global packname  BFpack
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Bayes Factor Testing of Scientific Expectations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-bain 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-extraDistr 
Requires:         R-CRAN-bain 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-extraDistr 

%description
Implementation of various default Bayes factors for testing statistical
hypotheses. The package is intended for applied quantitative researchers
in the social and behavioral sciences, medical research, and related
fields. The Bayes factor tests can be executed for statistical models such
as univariate and multivariate normal linear models, generalized linear
models, special cases of linear mixed models, survival models, relational
event models. Parameters that can be tested are location parameters (e.g.,
group means, regression coefficients), variances (e.g., group variances),
and measures of association (e.g,. bivariate correlations), among others.
The statistical underpinnings are described in Mulder, Hoijtink, and Xin
(2019) <arXiv:1904.00679>, Mulder and Gelissen (2019) <arXiv:1807.05819>,
Mulder (2016) <DOI:10.1016/j.jmp.2014.09.004>, Mulder and Fox (2019)
<DOI:10.1214/18-BA1115>, Mulder and Fox (2013)
<DOI:10.1007/s11222-011-9295-3>, Boeing-Messing, van Assen, Hofman,
Hoijtink, and Mulder (2017) <DOI:10.1037/met0000116>, Hoijtink, Mulder,
van Lissa, and Gu, (2018) <DOI:10.31234/osf.io/v3shc>, Gu, Mulder, and
Hoijtink, (2018) <DOI:10.1111/bmsp.12110>, Hoijtink, Gu, and Mulder,
(2018) <DOI:10.1111/bmsp.12145>, and Hoijtink, Gu, Mulder, and Rosseel,
(2018) <DOI:10.1037/met0000187>. When using the packages, please refer to
Mulder et al. (2021) <DOI:10.18637/jss.v100.i18>.

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
