%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  topiclabels
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Topic Labeling with Language Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-httr 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-CRAN-jsonlite 

%description
Leveraging (large) language models for automatic topic labeling. The main
function converts a list of top terms into a label for each topic. Hence,
it is complementary to any topic modeling package that produces a list of
top terms for each topic. While human judgement is indispensable for topic
validation (i.e., inspecting top terms and most representative documents),
automatic topic labeling can be a valuable tool for researchers in various
scenarios.

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
