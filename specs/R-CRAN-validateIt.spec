%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  validateIt
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Validating Topic Coherence and Topic Labels

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tm >= 0.7.11
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-pyMTurkR 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-SnowballC 
Requires:         R-CRAN-tm >= 0.7.11
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-pyMTurkR 
Requires:         R-CRAN-here 
Requires:         R-CRAN-SnowballC 

%description
By creating crowd-sourcing tasks that can be easily posted and results
retrieved using Amazon's Mechanical Turk (MTurk) API, researchers can use
this solution to validate the quality of topics obtained from unsupervised
or semi-supervised learning methods, and the relevance of topic labels
assigned. This helps ensure that the topic modeling results are accurate
and useful for research purposes. See Ying and others (2022)
<doi:10.1101/2023.05.02.538599>. For more information, please visit
<https://github.com/Triads-Developer/Topic_Model_Validation>.

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
