%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMF
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Collective Matrix Factorization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-stats 

%description
Collective matrix factorization (CMF) finds joint low-rank representations
for a collection of matrices with shared row or column entities. This code
learns a variational Bayesian approximation for CMF, supporting multiple
likelihood potentials and missing data, while identifying both factors
shared by multiple matrices and factors private for each matrix. For
further details on the method see Klami et al. (2014) <arXiv:1312.5921>.
The package can also be used to learn Bayesian canonical correlation
analysis (CCA) and group factor analysis (GFA) models, both of which are
special cases of CMF. This is likely to be useful for people looking for
CCA and GFA solutions supporting missing data and non-Gaussian
likelihoods. See Klami et al. (2013)
<https://research.cs.aalto.fi/pml/online-papers/klami13a.pdf> and Virtanen
et al. (2012) <http://proceedings.mlr.press/v22/virtanen12.html> for
details on Bayesian CCA and GFA, respectively.

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
