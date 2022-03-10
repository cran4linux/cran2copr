%global __brp_check_rpaths %{nil}
%global packname  sentiment.ai
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Sentiment Analysis Using Deep Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 2.2.0
BuildRequires:    R-CRAN-roperators >= 1.2.0
BuildRequires:    R-CRAN-reticulate >= 1.16
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-tfhub >= 0.8.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-tensorflow >= 2.2.0
Requires:         R-CRAN-roperators >= 1.2.0
Requires:         R-CRAN-reticulate >= 1.16
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-tfhub >= 0.8.0
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xgboost 

%description
Sentiment Analysis via deep learning and gradient boosting models with a
lot of the underlying hassle taken care of to make the process as simple
as possible. In addition to out-performing traditional, lexicon-based
sentiment analysis (see
<https://benwiseman.github.io/sentiment.ai/#Benchmarks>), it also allows
the user to create embedding vectors for text which can be used in other
analyses. GPU acceleration is supported on Windows and Linux.

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
