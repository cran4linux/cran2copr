%global packname  LocalControlStrategy
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          2%{?dist}
Summary:          Local Control Strategy for Robust Analysis of Cross-SectionalData

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-lattice 
Requires:         R-cluster 
Requires:         R-lattice 

%description
Especially when cross-sectional data are observational, effects of
treatment selection bias and confounding are revealed by using the
Nonparametric and Unsupervised "preprocessing" methods central to Local
Control (LC) Strategy. The LC objective is to estimate the "effect-size
distribution" that best quantifies a potentially causal relationship
between a numeric y-Outcome variable and a t-Treatment variable. This
t-variable may be either binary {1 = "new" vs 0 = "control"} or a numeric
measure of Exposure level. LC Strategy starts by CLUSTERING experimental
units (patients) on their pre-exposure X-Covariates, forming mutually
exclusive and exhaustive BLOCKS of relatively well-matched units. The
implicit statistical model for LC is thus simple one-way ANOVA. The
Within-Block measures of effect-size are Local Rank Correlations (LRCs)
when Exposure is numeric with more than two levels. Otherwise, Treatment
choice is Nested within BLOCKS, and effect-sizes are LOCAL Treatment
Differences (LTDs) between within-cluster y-Outcome Means ["new" minus
"control"]. An Instrumental Variable (IV) method is also provided so that
Local Average y-Outcomes (LAOs) within BLOCKS may also contribute
information for effect-size inferences ...assuming that X-Covariates
influence only Treatment choice or Exposure level and otherwise have no
direct effects on y-Outcome. Finally, a "Most-Like-Me" function provides
histograms of effect-size distributions to aid Doctor-Patient
communications about Personalized Medicine.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
