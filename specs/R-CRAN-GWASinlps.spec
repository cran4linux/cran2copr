%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GWASinlps
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Local Prior Based Iterative Variable Selection Tool for Genome-Wide Association Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-mombf 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-fastglm 
BuildRequires:    R-CRAN-horseshoe 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-mombf 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-fastglm 
Requires:         R-CRAN-horseshoe 
Requires:         R-CRAN-survival 

%description
Performs variable selection with data from Genome-wide association studies
(GWAS), or other high-dimensional data with continuous, binary or survival
outcomes, combining in an iterative framework the computational efficiency
of the structured screen-and-select variable selection strategy based on
some association learning and the parsimonious uncertainty quantification
provided by the use of non-local priors (see Sanyal et al., 2019
<DOI:10.1093/bioinformatics/bty472>).

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
