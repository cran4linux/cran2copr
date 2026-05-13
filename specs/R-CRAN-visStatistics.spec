%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visStatistics
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Selection and Visualisation of Statistical Hypothesis Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vcd 
Requires:         R-CRAN-Cairo 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-nortest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vcd 

%description
The right test, visualised. 'visStatistics' automatically selects and
visualises statistical hypothesis tests comparing two vectors, based on
their class, distribution, and sample size. Visual outputs, including box
plots, bar charts, regression lines with confidence bands, mosaic plots,
residual plots, and Q-Q plots, are annotated with relevant test
statistics, assumption checks, and post-hoc analyses where applicable. The
algorithmic workflow shifts attention from ad-hoc test selection to visual
diagnostic assessment and statistical interpretation. It is particularly
suited for server-side R applications, where end users interact solely
through a web interface to select data groups and receive a complete
visual statistical analysis automatically. The same automation makes it
useful in time-constrained contexts such as statistical consulting, where
it reduces effort spent on test selection and leaves more room for
interpretation. The implemented tests cover the most frequently applied
inferential methods in biomedical research (Hayat et al. (2017)
<doi:10.1371/journal.pone.0179032>). The test selection algorithm proceeds
as follows: Input vectors of class numeric or integer are considered
numerical; those of class factor are considered categorical; those of
class ordered are considered ordinal. Assumptions of residual normality
and homogeneity of variances are considered met if the corresponding test
yields a p-value greater than the significance level alpha = 1 -
conf.level. (1) When the response is numerical and the predictor is
categorical, a test comparing central tendencies is selected. If every
group contains more than 50 observations, the sampling distribution of the
group means is assumed approximately normal by the central limit theorem
(Lumley et al. (2002) <doi:10.1146/annurev.publhealth.23.100901.140546>);
otherwise, residual normality is assessed using shapiro.test() applied to
the standardised residuals of lm(). If normality is not met, wilcox.test()
is used when the predictor has two levels and kruskal.test() followed by
pairwise.wilcox.test() otherwise. If normality is met, levene.test()
assesses variance homogeneity. For two-level predictors, Student's
t.test(var.equal = TRUE) is applied if variances are homogeneous and
Welch's t.test() otherwise. For predictors with more than two levels,
aov() followed by TukeyHSD() is applied if variances are homogeneous, and
oneway.test() followed by games.howell() otherwise. (2) When both vectors
are numerical, lm() is fitted by default (correlation = FALSE). If
correlation = TRUE, Spearman rank correlation is performed. (3) When the
response is ordinal, it is converted to numeric ranks and the
non-parametric path from (1) is followed (Wilcoxon or Kruskal-Wallis).
When both variables are ordinal and correlation = TRUE, Kendall's tau_b is
used instead. (4) When both vectors are categorical, Cochran's rule
(Cochran (1954) <doi:10.2307/3001666>) is applied to test independence
either by chisq.test() or fisher.test().

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
