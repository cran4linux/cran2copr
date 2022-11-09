%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LocalControlStrategy
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Local Control Strategy for Robust Analysis of Cross-Sectional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-lattice 

%description
Especially when cross-sectional data are observational, effects of
treatment selection bias and confounding are revealed by using the
Nonparametric and Unsupervised "preprocessing" methods central to Local
Control (LC) Strategy. The LC objective is to estimate the "effect-size
distribution" that best quantifies a potentially causal relationship
between a numeric y-Outcome variable and a t-Treatment or e-Exposure
variable. Treatment variables are binary {either 1 = "new" or 0 =
"control"}, while Exposure variables vary continuously over a finite
range. LC Strategy starts by CLUSTERING experimental units (individual
patients, US Counties, etc.) on their X-confounder characteristics.
Clusters represent exclusive and exhaustive BLOCKS of relatively
well-matched units. The implicit statistical model for LC is thus simple
one-way ANOVA. Within-Block measures of effect-size are Local Rank
Correlations (LRCs) when Exposure is numeric with (many) more than two
levels. Otherwise, Treatment choice is Nested within BLOCKS, and
effect-sizes are LOCAL Treatment Differences (LTDs) between Within-Cluster
y-Outcome Means ["new" minus "control"]. An Instrumental Variable (IV)
method is also provided so that Local Average y-Outcomes (LAOs) within
BLOCKS may also contribute information for effect-size inferences
...assuming that X-Covariates influence only Treatment choice or Exposure
level and otherwise have no direct effects on y-Outcome. Finally, a
"Most-Like-Me" function provides histograms of effect-size distributions
to aid Doctor-Patient or Researcher-Society communications about
Heterogeneous Outcomes.

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
