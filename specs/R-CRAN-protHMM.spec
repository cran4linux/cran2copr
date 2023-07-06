%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  protHMM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Protein Feature Extraction from Profile Hidden Markov Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-phonTools 
Requires:         R-CRAN-gtools 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-phonTools 

%description
Calculates a comprehensive list of features from profile hidden Markov
models (HMMs) of proteins. Adapts and ports features for use with HMMs
instead of Position Specific Scoring Matrices, in order to take advantage
of more accurate multiple sequence alignment by programs such as 'HHBlits'
Remmert et al. (2012) <DOI:10.1038/nmeth.1818> and 'HMMer' Eddy (2011)
<DOI:10.1371/journal.pcbi.1002195>. Features calculated by this package
can be used for protein fold classification, protein structural class
prediction, sub-cellular localization and protein-protein interaction,
among other tasks. Some examples of features extracted are found in Song
et al. (2018) <DOI:10.3390/app8010089>, Jin & Zhu (2021)
<DOI:10.1155/2021/8629776>, Lyons et al. (2015)
<DOI:10.1109/tnb.2015.2457906> and Saini et al. (2015)
<DOI:10.1016/j.jtbi.2015.05.030>.

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
