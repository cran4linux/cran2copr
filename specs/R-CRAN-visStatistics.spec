%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visStatistics
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
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
Automatically selects and visualises statistical hypothesis tests between
two vectors, based on their class, distribution, sample size, and a
user-defined confidence level (conf.level). Visual outputs - including box
plots, bar charts, regression lines with confidence bands, mosaic plots,
residual plots, and Q-Q plots - are annotated with relevant test
statistics, assumption checks, and post-hoc analyses where applicable. The
algorithmic workflow helps the user focus on the interpretation of test
results rather than test selection. It is particularly suited for quick
data analysis, e.g., in statistical consulting projects or educational
settings. The test selection algorithm proceeds as follows: Input vectors
of class numeric or integer are considered numerical; those of class
factor are considered categorical. Assumptions of residual normality and
homogeneity of variances are considered met if the corresponding test
yields a p-value greater than the significance level alpha = 1 -
conf.level. (1) When the response vector is numerical and the predictor
vector is categorical, a test of central tendencies is selected. If the
categorical predictor has exactly two levels, t.test() is applied when
group sizes exceed 30 (Lumley et al. (2002)
<doi:10.1146/annurev.publhealth.23.100901.140546>). For smaller samples,
normality of residuals is tested using shapiro.test(); if met, t.test() is
used; otherwise, wilcox.test(). If the predictor is categorical with more
than two levels, an aov() is initially fitted. Residual normality is
evaluated using both shapiro.test() and ad.test(); residuals are
considered approximately normal if at least one test yields a p-value
above alpha. If this assumption is met, bartlett.test() assesses variance
homogeneity. If variances are homogeneous, aov() is used; otherwise
oneway.test(). Both tests are followed by TukeyHSD(). If residual
normality cannot be assumed, kruskal.test() is followed by
pairwise.wilcox.test(). (2) When both the response and predictor vectors
are numerical, a simple linear regression model is fitted using lm(). (3)
When both vectors are categorical, Cochran's rule (Cochran (1954)
<doi:10.2307/3001666>) is applied to test independence either by
chisq.test() or fisher.test().

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
