%global __brp_check_rpaths %{nil}
%global packname  sumSome
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Permutation True Discovery Guarantee by Sum-Based Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-pARI 
BuildRequires:    R-CRAN-ARIbrain 
BuildRequires:    R-CRAN-RNifti 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-pARI 
Requires:         R-CRAN-ARIbrain 
Requires:         R-CRAN-RNifti 

%description
It allows to quickly perform permutation-based closed testing by sum-based
global tests, and construct lower confidence bounds for the TDP,
simultaneously over all subsets of hypotheses. As a main feature, it
produces simultaneous lower confidence bounds for the proportion of active
voxels in different clusters for fMRI cluster analysis. Details may be
found in Vesely, Finos, and Goeman (2020) <arXiv:2102.11759>.

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
