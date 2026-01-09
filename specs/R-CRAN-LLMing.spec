%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LLMing
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Large Language Model (LLM) Tools for Psychological Text Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-text 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-text 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-jsonlite 

%description
A collection of large language model (LLM) text analysis methods designed
with psychological data in mind. Currently, LLMing (aka "lemming")
includes a text anomaly detection method based on the angle-based subspace
approach described by Zhang, Lin, and Karim (2015) and a text generation
method. <doi:10.1016/j.ress.2015.05.025>.

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
