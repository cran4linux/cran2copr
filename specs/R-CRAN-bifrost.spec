%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bifrost
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Branch-Level Inference Framework for Recognizing Optimal Shifts in Traits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-phytools >= 2.0.3
BuildRequires:    R-CRAN-future >= 1.49.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-RRphylo 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvMORPH 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-txtplot 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-phytools >= 2.0.3
Requires:         R-CRAN-future >= 1.49.0
Requires:         R-CRAN-ape 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-future.apply 
Requires:         R-parallel 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-RRphylo 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-mvMORPH 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-txtplot 

%description
Methods for detecting, visualizing, and evaluating cladogenic shifts in
multivariate trait data on phylogenies. Implements penalized-likelihood
multivariate generalized least squares models and a greedy step-wise shift
search for high-dimensional trait datasets and large trees via
searchOptimalConfiguration(). Provides tools for inspecting search
trajectories, summarizing branch and lineage rates, analyzing shift timing
and magnitudes, estimating post-hoc regime covariance and integration, and
running simulation-based calibration and tuning. The search follows
approaches developed in Smith et al. (2023) <doi:10.1111/nph.19099> and
Berv et al. (2024) <doi:10.1126/sciadv.adp0114>. Methods build on
multivariate generalized least squares approaches described in Clavel et
al. (2019) <doi:10.1093/sysbio/syy045> and implemented in the mvgls()
function from the 'mvMORPH' package. Documentation and worked examples are
available at <https://jakeberv.com/bifrost/>.

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
