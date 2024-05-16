%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdmed
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Mediation Analysis with High-Dimensional Mediators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mediation >= 4.5.0
BuildRequires:    R-CRAN-ncvreg >= 3.13.0
BuildRequires:    R-CRAN-genlasso >= 1.6.1
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-bama >= 1.3.0
BuildRequires:    R-CRAN-gcdnet >= 1.0.6
BuildRequires:    R-CRAN-iterators >= 1.0.14
BuildRequires:    R-CRAN-freebird >= 1.0
BuildRequires:    R-CRAN-hdi >= 0.1.9
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-mediation >= 4.5.0
Requires:         R-CRAN-ncvreg >= 3.13.0
Requires:         R-CRAN-genlasso >= 1.6.1
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-bama >= 1.3.0
Requires:         R-CRAN-gcdnet >= 1.0.6
Requires:         R-CRAN-iterators >= 1.0.14
Requires:         R-CRAN-freebird >= 1.0
Requires:         R-CRAN-hdi >= 0.1.9
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 

%description
A suite of functions for performing mediation analysis with
high-dimensional mediators. In addition to centralizing code from several
existing packages for high-dimensional mediation analysis, we provide
organized, well-documented functions for a handle of methods which, though
programmed their original authors, have not previously been formalized
into R packages or been made presentable for public use. The methods we
include cover a broad array of approaches and objectives, and are
described in detail by both our companion manuscript---"Methods for
Mediation Analysis with High-Dimensional DNA Methylation Data: Possible
Choices and Comparison"---and the original publications that proposed
them. The specific methods offered by our package include the Bayesian
sparse linear mixed model (BSLMM) by Song et al. (2019); high-dimensional
mediation analysis (HDMA) by Gao et al. (2019); high-dimensional
multivariate mediation (HDMM) by Chén et al. (2018); high-dimensional
linear mediation analysis (HILMA) by Zhou et al. (2020); high-dimensional
mediation analysis (HIMA) by Zhang et al. (2016); latent variable
mediation analysis (LVMA) by Derkach et al. (2019); mediation by
fixed-effect model (MedFix) by Zhang (2021); pathway LASSO by Zhao & Luo
(2022); principal component mediation analysis (PCMA) by Huang & Pan
(2016); and sparse principal component mediation analysis (SPCMA) by Zhao
et al. (2020). Citations for the corresponding papers can be found in
their respective functions.

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
