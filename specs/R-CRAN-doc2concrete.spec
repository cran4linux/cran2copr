%global packname  doc2concrete
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Measuring Concreteness in Natural Language

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-english 
BuildRequires:    R-CRAN-textstem 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-quanteda 
Requires:         R-parallel 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-english 
Requires:         R-CRAN-textstem 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stringi 

%description
Models for detecting concreteness in natural language. This package is
built in support of Yeomans (2021) <doi:10.1016/j.obhdp.2020.10.008>,
which reviews linguistic models of concreteness in several domains. Here,
we provide an implementation of the best-performing domain-general model
(from Brysbaert et al., (2014) <doi:10.3758/s13428-013-0403-5>) as well as
two pre-trained models for the feedback and plan-making domains.

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
