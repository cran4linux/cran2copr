%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NU.Learning
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric and Unsupervised Learning from Cross-Sectional Observational Data

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
treatment selection bias and confounding are best revealed by using
Nonparametric and Unsupervised methods to "Design" the analysis of the
given data ...rather than the collection of "designed data". Specifically,
the "effect-size distribution" that best quantifies a potentially causal
relationship between a numeric y-Outcome variable and either a binary
t-Treatment or continuous e-Exposure variable needs to consist of BLOCKS
of relatively well-matched experimental units (e.g. patients) that have
the most similar X-confounder characteristics. Since our NU Learning
approach will form BLOCKS by "clustering" experimental units in confounder
X-space, the implicit statistical model for learning is One-Way ANOVA.
Within Block measures of effect-size are then either [a] LOCAL Treatment
Differences (LTDs) between Within-Cluster y-Outcome Means ("new" minus
"control") when treatment choice is Binary or else [b] LOCAL Rank
Correlations (LRCs) when the e-Exposure variable is numeric with
(hopefully many) more than two levels. An Instrumental Variable (IV)
method is also provided so that Local Average y-Outcomes (LAOs) within
BLOCKS may also contribute information for effect-size inferences when
X-Covariates are assumed to influence Treatment choice or Exposure level
but otherwise have no direct effects on y-Outcomes. Finally, a
"Most-Like-Me" function provides histograms of effect-size distributions
to aid Doctor-Patient (or Researcher-Society) communications about
Heterogeneous Outcomes. Obenchain and Young (2013)
<doi:10.1080/15598608.2013.772821>; Obenchain, Young and Krstic (2019)
<doi:10.1016/j.yrtph.2019.104418>.

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
