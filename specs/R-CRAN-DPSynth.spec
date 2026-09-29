%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DPSynth
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Differentially Private Synthetic Data with Guaranteed Utility

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 

%description
Differentially private (DP) synthetic data generation for tabular data.
Provides DP Gaussian mixture models, DP Gaussian copulas, DP histogram
marginals and a Private Aggregation of Teacher Ensembles (PATE)
synthesizer for mixed-type data, together with a standardized utility
evaluation framework (univariate fidelity, propensity score MSE,
multivariate dependence, downstream task performance), empirical
disclosure risk auditing (membership inference, attribute disclosure,
record linkage) and privacy budget accounting (basic, advanced and Renyi
DP composition). The implementation follows Dwork and Roth (2014)
<doi:10.1561/0400000042> and Dwork et al. (2006) <doi:10.1007/11681878_14>
for the DP mechanisms, Papernot et al. (2017)
<doi:10.1145/3133956.3133982> for the PATE synthesizer, and Woo et al.
(2009) <doi:10.2202/1557-4679.1203> for the disclosure risk evaluation
framework.

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
