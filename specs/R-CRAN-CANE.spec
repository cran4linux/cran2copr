%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CANE
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Groups of Experiments Analysis for Numerous Environments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-stats 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-stats 

%description
In many cases, experiments must be repeated across multiple seasons or
locations to ensure applicability of findings. A single experiment
conducted in one location and season may yield limited conclusions, as
results can vary under different environmental conditions. In agricultural
research, treatment × location and treatment × season interactions play a
crucial role. Analyzing a series of experiments across diverse conditions
allows for more generalized and reliable recommendations. The 'CANE'
package facilitates the pooled analysis of experiments conducted over
multiple years, seasons, or locations. It is designed to assess treatment
interactions with environmental factors (such as location and season)
using various experimental designs. The package supports pooled analysis
of variance (ANOVA) for the following designs: (1) 'PooledCRD()':
completely randomized design; (2) 'PooledRBD()': randomized block design;
(3) 'PooledLSD()': Latin square design; (4) 'PooledSPD()': split plot
design; and (5) 'PooledStPD()': strip plot design. Each function provides
the following outputs: (i) Individual ANOVA tables based on independent
analysis for each location or year; (ii) Testing of homogeneity of error
variances among distinct locations using Bartlett’s Chi-Square test; (iii)
If Bartlett’s test is significant, 'Aitken’s' transformation, defined as
the ratio of the response to the square root of the error mean square, is
applied to the response variable; otherwise, the data is used as is; (iv)
Combined analysis to obtain a pooled ANOVA table; (v) Multiple comparison
tests, including Tukey's honestly significant difference (Tukey's HSD)
test, Duncan’s multiple range test (DMRT), and the least significant
difference (LSD) test, for treatment comparisons. The statistical theory
and steps of analysis of these designs are available in Dean et al.
(2017)<doi:10.1007/978-3-319-52250-0> and Ruíz et al.
(2024)<doi:10.1007/978-3-031-65575-3>. By broadening the scope of
experimental conclusions, 'CANE' enables researchers to derive robust,
widely applicable recommendations. This package is particularly valuable
in agricultural research, where accounting for treatment × location and
treatment × season interactions is essential for ensuring the validity of
findings across multiple settings.

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
