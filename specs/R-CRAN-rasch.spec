%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rasch
%global packver   1.11.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.7
Release:          1%{?dist}%{?buildtag}
Summary:          Pairwise Conditional Rasch Measurement Analysis and Diagnostics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Pairwise conditional maximum likelihood estimation of dichotomous and
polytomous Rasch models (partial credit and rating scale) after Andrich
and Luo (2003) and Zwinderman (1995) <doi:10.1177/014662169501900406>,
with standard errors from a Godambe sandwich estimator. An optional
alternative estimator reparameterises each item's thresholds as Andrich's
(1978 <doi:10.1007/BF02293814>, 1985) orthogonal-polynomial principal
components (location, spread, skewness, and kurtosis; Pedler 1987), exact
for items with up to 3 thresholds and a smoothed reduced-rank model for
items with more, useful when some categories are sparsely populated.
Person measures are Warm's (1989) <doi:10.1007/BF02294627> weighted
likelihood estimates, computed per missing-data pattern. The diagnostic
suite follows the conventions set out in Andrich and Marais (2019)
<doi:10.1007/978-981-13-7496-8>: the log-of-mean-square fit residual with
apportioned degrees of freedom (and its natural form), infit and outfit,
the item-trait interaction chi-square over automatically sized class
intervals with its per-interval detail table, the class-interval ANOVA
item-fit F, the person separation index with and without extremes and the
item separation index, Cronbach's alpha, summary distribution statistics
with skewness and kurtosis, targeting, the score-to-measure table with
maximum likelihood and geometric extreme-score extrapolation options, test
information, threshold and category diagnostics, residual
principal-components dimensionality testing, local dependence by residual
correlation, and differential item functioning by two-way residual
analysis of variance over any number of person factors, factor-at-a-time
(the full two-way table with partial eta-squared effect sizes) or as a
full factorial with interaction precedence, Tukey HSD post-hoc comparisons
on significant group terms and interaction cells, false-discovery-rate or
familywise adjustment, and DIF magnitudes in logits by resolved-item
locations with a practical-significance criterion. Violations of
independence are quantified, not just flagged: the magnitude of response
dependence between two items by the resolution method of Andrich and
Kreiner (2010) <doi:10.1177/0146621609360202> (polytomous form Andrich,
Humphry and Marais 2012 <doi:10.1177/0146621612441858>), the
spread-parameter least-upper-bound screen (Andrich 1985), and the
magnitude of multidimensionality (latent subscale correlation and
common-variance proportion) from Andrich's (2016) two-calculation
reliability comparison. A likelihood-ratio test of the partial credit
against the rating parameterisation is reported both raw, as
conventionally displayed, and with a first-order composite-likelihood
calibration (Kent 1982 <doi:10.1093/biomet/69.1.19>) from the Godambe
matrices. Also included: anchored estimation for test equating (individual
threshold and average item-location anchors), common-item equating tests
and plots, item splitting to resolve invariance violations, tailored
analysis for guessing with the four-step anchored comparison (Andrich,
Marais and Humphry 2012 <doi:10.3102/1076998611411914>), classical test
theory companion statistics, racked and stacked reshaping for repeated
measurements, model comparison by composite-likelihood information
criteria whose penalty is the Godambe effective parameter count (Varin and
Vidoni 2005 <doi:10.1093/biomet/92.3.519>; Gao and Song 2010
<doi:10.1198/jasa.2010.tm09414>), absorbing the pairwise over-counting
that a nominal AIC or BIC would ignore, the many-facet Rasch model
(Linacre 1989) for rated long-format data with facet severities, fit, and
optional item-by-facet interactions, subtest formation for locally
dependent items, multiple-choice scoring against a key with double keying
and polytomous option scoring of informative distractors (Andrich and
Styles 2011, with an evidence-based rescoring proposal), rest-measure
distractor analysis and option curves, the Guttman scalogram with the
coefficient of reproducibility, the Bradley-Terry-Luce model for paired
comparisons (Bradley and Terry 1952 <doi:10.1093/biomet/39.3-4.324>; Luce
1959) as the conditional form of the dichotomous Rasch model (Andrich
1978), estimated by the same conventions with judge-clustered sandwich
errors and judge fit diagnostics, and the first software implementation of
the extended frame of reference model (Humphry 2005; Humphry and Andrich
2008), in which the unit of the latent scale differs across item-set by
person-group frames: group units are estimated by person-free within-frame
pairwise conditioning and set units by error-corrected person linking, all
reported in a common arbitrary unit; its paired-comparison form estimates
judge-panel and object-set units with the linking identified from
cross-set comparisons alone. A modern 'shiny' interface and a one-call
exporter for every table and plot are included. Implemented from published
measurement theory in base R, with no dependence on other estimation
engines.

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
