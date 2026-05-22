%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scindex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Strategic Convergence Index for Inter-Rater Reliability

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Inter-rater reliability analysis for binary classification tasks involving
two or more raters within a signal detection-theoretic framework.
User-supplied rating data are standardised into a common long-format
structure. The package automatically computes Cohen's kappa for two raters
and Fleiss' kappa for multiple raters. When ground-truth labels are
available, rater-specific hit rates, false-alarm rates, sensitivity,
specificity, and decision thresholds are estimated from observed
classification responses using standard signal detection-theoretic
transformations (DeCarlo, 1998) <doi:10.1037/1082-989X.3.2.186>. The
package implements the Strategic Convergence Index (SCI; Gianeselli, 2026)
<doi:10.1177/00131644261417643>, defined as SCI = 1 - [Var(t_i) /
Var_max], where Var(t_i) denotes the variance of rater-specific decision
thresholds and Var_max denotes the reference variance under maximal
threshold dispersion. SCI quantifies convergence in rater decision
criteria beyond observed agreement alone and complements classical
agreement coefficients by distinguishing agreement in observed categorical
outcomes from convergence in latent decision thresholds under an explicit
signal detection-theoretic model of categorical judgment. The package
provides structured summaries and threshold-based diagnostics for
applications in which similar agreement coefficients may reflect
substantively different underlying decision criteria across raters.

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
