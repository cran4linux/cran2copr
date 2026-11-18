%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prCGGM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prior-Informed Conditional Gaussian Graphical Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sparsegl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-sparsegl 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimates Gaussian graphical models whose mean and precision matrix depend
linearly on sample-level covariates, while integrating prior knowledge on
the network structure. A typical application is the reconstruction of
personalised protein-protein interaction networks from proteomics data,
with clinical or demographic variables as covariates and interaction
confidence scores from the 'STRING' database as prior knowledge. Prior
knowledge enters through a weighted sparse-group lasso penalty that is
applied only to the population-level network, so that covariate-specific
changes remain entirely data-driven. Node-wise regressions are fitted with
'glmnet' and 'sparsegl', structural hyperparameters are tuned per node by
the Bayesian information criterion, and personalised networks can be
predicted for new individuals from their covariates. Estimation runs
sequentially, in parallel on a single machine, or as 'SLURM' array jobs on
computing clusters. The method is described in Mapelli et al. (2026)
<doi:10.48550/arXiv.2606.31805>.

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
