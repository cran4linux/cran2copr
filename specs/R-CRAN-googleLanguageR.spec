%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  googleLanguageR
%global packver   0.3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Call Google's 'Natural Language', 'Cloud Translation', 'Cloud Speech', and 'Cloud Text-to-Speech' APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-googleAuthR >= 1.1.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-googleAuthR >= 1.1.1
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Access Google Cloud machine learning APIs for text and speech tasks. Use
the Cloud Translation API for text detection and translation, the Natural
Language API to analyze sentiment, entities, and syntax, the Cloud Speech
API to transcribe audio to text, and the Cloud Text-to-Speech API to
synthesize text into audio files.

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
