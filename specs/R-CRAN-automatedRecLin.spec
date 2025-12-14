%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  automatedRecLin
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Record Linkage Based on an Entropy-Maximizing Classifier

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-densityratio 
BuildRequires:    R-CRAN-FixedPoint 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reclin2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-densityratio 
Requires:         R-CRAN-FixedPoint 
Requires:         R-methods 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reclin2 
Requires:         R-stats 
Requires:         R-utils 

%description
The goal of 'automatedRecLin' is to perform record linkage (also known as
entity resolution) in unsupervised or supervised settings. It compares
pairs of records from two datasets using selected comparison functions to
estimate the probability or density ratio between matched and non-matched
records. Based on these estimates, it predicts a set of matches that
maximizes entropy. For details see: Lee et al. (2022)
<https://www150.statcan.gc.ca/n1/pub/12-001-x/2022001/article/00007-eng.htm>,
Vo et al. (2023)
<https://ideas.repec.org/a/eee/csdana/v179y2023ics0167947322002365.html>,
Sugiyama et al. (2008) <doi:10.1007/s10463-008-0197-x>.

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
