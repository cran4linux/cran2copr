%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastFGEE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Functional Generalized Estimating Equations via a One-Step Estimator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-refund 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-SuperGauss 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-refund 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-SuperGauss 

%description
Fits functional generalized estimating equations for longitudinal
functional outcomes and covariates using a one-step estimator that is fast
even for large cluster sizes or large numbers of clusters. The package
supports quasi-likelihoods derived from a range of families, common link
functions, and several working correlation structures. Uncertainty
quantification is based on sandwich variance estimators and bootstrap
procedures that remain valid even when the working correlation is
incorrectly specified. The package provides an implementation of the
method described in Loewinger et al. (2025)
<https://pmc.ncbi.nlm.nih.gov/articles/PMC12306803/>. For irregularly
spaced AR(1) precision matrices, the package can optionally use the
archived package 'irregulAR1'; if needed, it can be obtained from the CRAN
Archive at <https://cran.r-project.org/src/contrib/Archive/irregulAR1/>.

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
