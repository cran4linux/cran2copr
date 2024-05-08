%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ddecompose
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detailed Distributional Decomposition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rifreg 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-fastglm 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rifreg 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-Hmisc 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-fastglm 
Requires:         R-methods 

%description
Implements the Oaxaca-Blinder decomposition method and generalizations of
it that decompose differences in distributional statistics beyond the
mean. The function ob_decompose() decomposes differences in the mean
outcome between two groups into one part explained by different covariates
(composition effect) and into another part due to differences in the way
covariates are linked to the outcome variable (structure effect). The
function further divides the two effects into the contribution of each
covariate and allows for weighted doubly robust decompositions. For
distributional statistics beyond the mean, the function performs the
recentered influence function (RIF) decomposition proposed by Firpo,
Fortin, and Lemieux (2018). The function dfl_decompose() divides
differences in distributional statistics into an composition effect and a
structure effect using inverse probability weighting as introduced by
DiNardo, Fortin, and Lemieux (1996). The function also allows to
sequentially decompose the composition effect into the contribution of
single covariates. References: Firpo, Sergio, Nicole M. Fortin, and Thomas
Lemieux. (2018) <doi:10.3390/econometrics6020028>. "Decomposing Wage
Distributions Using Recentered Influence Function Regressions." Fortin,
Nicole M., Thomas Lemieux, and Sergio Firpo. (2011) <doi:10.3386/w16045>.
"Decomposition Methods in Economics." DiNardo, John, Nicole M. Fortin, and
Thomas Lemieux. (1996) <doi:10.2307/2171954>. "Labor Market Institutions
and the Distribution of Wages, 1973-1992: A Semiparametric Approach."
Oaxaca, Ronald. (1973) <doi:10.2307/2525981>. "Male-Female Wage
Differentials in Urban Labor Markets." Blinder, Alan S. (1973)
<doi:10.2307/144855>. "Wage Discrimination: Reduced Form and Structural
Estimates."

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
