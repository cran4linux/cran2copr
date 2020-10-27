%global packname  DALEX
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          moDel Agnostic Language for Exploration and eXplanation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ingredients >= 2.0
BuildRequires:    R-CRAN-iBreakDown >= 1.3.1
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ingredients >= 2.0
Requires:         R-CRAN-iBreakDown >= 1.3.1
Requires:         R-CRAN-ggplot2 

%description
Unverified black box model is the path to the failure. Opaqueness leads to
distrust. Distrust leads to ignoration. Ignoration leads to rejection.
DALEX package xrays any model and helps to explore and explain its
behaviour. Machine Learning (ML) models are widely used and have various
applications in classification or regression. Models created with
boosting, bagging, stacking or similar techniques are often used due to
their high performance. But such black-box models usually lack of direct
interpretability. DALEX package contains various methods that help to
understand the link between input variables and model output. Implemented
methods help to explore model on the level of a single instance as well as
a level of the whole dataset. All model explainers are model agnostic and
can be compared across different models. DALEX package is the cornerstone
for 'DrWhy.AI' universe of packages for visual model exploration. Find
more details in (Biecek 2018) <arXiv:1806.08915>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
