%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SamplingStrata
%global packver   1.5-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Stratification of Sampling Frames for Multipurpose Sampling Surveys

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-SamplingBigData 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-SamplingBigData 
Requires:         R-CRAN-glue 
Requires:         R-methods 

%description
Tools for the optimization of stratified sampling design. It determines a
stratification of a sampling frame that minimizes sample cost while
satisfying precision constraints in a multivariate and multidomain
context. The approach relies on a genetic algorithm; each candidate
partition of the frame is an individual whose fitness is evaluated via the
Bethel-Chromy allocation to meet target precisions. Functions support
analysis of optimization results, labeling of the frame with new strata,
and drawing a sample according to the optimal allocation. Algorithmic
components adapt code from the 'genalg' package. See M. Ballin and G.
Barcaroli (2020) "R package SamplingStrata: new developments and extension
to Spatial Sampling" <doi:10.48550/arXiv.2004.09366>.

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
