%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  text2emotion
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Emotion Analysis and Emoji Mapping for Text

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-textclean 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-text2vec 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-textclean 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-text2vec 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-caret 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 

%description
Allows users to analyze text and classify emotions such as happiness,
sadness, anger, fear, and neutrality. It combines text preprocessing,
TF-IDF (Term Frequency-Inverse Document Frequency) feature extraction, and
Random Forest classification to predict emotions and map them to
corresponding emojis for enhanced sentiment visualization.

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
