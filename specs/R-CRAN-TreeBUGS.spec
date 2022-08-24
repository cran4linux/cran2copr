%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TreeBUGS
%global packver   1.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Multinomial Processing Tree Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-logspline 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-runjags 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-coda 
Requires:         R-parallel 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-logspline 

%description
User-friendly analysis of hierarchical multinomial processing tree (MPT)
models that are often used in cognitive psychology. Implements the
latent-trait MPT approach (Klauer, 2010) <DOI:10.1007/s11336-009-9141-0>
and the beta-MPT approach (Smith & Batchelder, 2010)
<DOI:10.1016/j.jmp.2009.06.007> to model heterogeneity of participants.
MPT models are conveniently specified by an .eqn-file as used by other MPT
software and data are provided by a .csv-file or directly in R. Models are
either fitted by calling JAGS or by an MPT-tailored Gibbs sampler in C++
(only for nonhierarchical and beta MPT models). Provides tests of
heterogeneity and MPT-tailored summaries and plotting functions. A
detailed documentation is available in Heck, Arnold, & Arnold (2018)
<DOI:10.3758/s13428-017-0869-7>.

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
