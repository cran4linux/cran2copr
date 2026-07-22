%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  grassr
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Context-Conditioned Reporting for Binary Rater Reliability

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Generates a Report Card for rater reliability on binary outcomes from an N
x k subject-by-rater rating matrix, on both the inter-rater and
intra-rater axes. Each panel coefficient is positioned on a
data-generating-process-calibrated reference surface conditioned on the
study's rater count, sample size, and prevalence, yielding a pooled
percentile (the coefficient's position within the design's achievable
agreement range) together with a consistency band on panel quality: the
quality levels whose sampling distributions are consistent with the
observed value at that design. The panel coefficients are the
prevalence-adjusted bias-adjusted kappa (PABAK) of Byrt, Bishop, and
Carlin (1993) <doi:10.1016/0895-4356(93)90018-V>, the first-order
agreement coefficient (AC1) of Gwet (2008) <doi:10.1348/000711006X126600>,
the multi-rater kappa of Fleiss (1971) <doi:10.1037/h0031619>, and the
observed intraclass correlation. A cross-coefficient discordance
diagnostic (delta-hat) reports the spread of the coefficients' implied
panel qualities and flags panels for which no single coefficient is a
stable summary by the spread's percentile on a matched null distribution;
for such divergent panels the report routes to a pairwise PABAK matrix and
per-rater sensitivity and specificity recovered from the latent-class
model of Dawid and Skene (1979) <doi:10.2307/2346806>, with the two-rater
bounds of Hui and Walter (1980) <doi:10.2307/2530508>.

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
