%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gputools
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          GPU Drop-Ins for Statistics on Wide Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-utils 
Requires:         R-utils 

%description
GPU versions of base R statistics for data with many variables, using the
NVIDIA 'CUDA' toolkit: correlation matrices (Pearson, Spearman and
Kendall) and their tests, the strongest correlated pairs among tens of
thousands of variables without forming the matrix, association scans with
covariates as in expression quantitative trait loci studies (Shabalin 2012
<doi:10.1093/bioinformatics/bts163>), permutation tests with
Westfall-Young maxT adjustment, distance matrices, hierarchical and
k-means clustering, Granger causality tests, B-spline mutual information,
principal components, and least-squares fits. Results agree with the base
R functions they replace. Without 'CUDA' the package installs, and its
functions explain how to get a 'CUDA' build. Described in Buckner et al.
(2010) <doi:10.1093/bioinformatics/btp608>.

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
