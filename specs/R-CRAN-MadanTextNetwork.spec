%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MadanTextNetwork
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Persian Text Mining Tool for Co-Occurrence Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.0
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-textmineR 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-udpipe 
BuildRequires:    R-CRAN-PersianStemmer 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-hwordcloud 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ngram 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-shiny >= 1.8.0
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-textmineR 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-udpipe 
Requires:         R-CRAN-PersianStemmer 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-hwordcloud 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ngram 
Requires:         R-CRAN-visNetwork 

%description
Provides an extension to 'MadanText' for creating and analyzing
co-occurrence networks in Persian text data. This package mainly makes use
of the 'PersianStemmer' (Safshekan, R., et al. (2019).
<https://CRAN.R-project.org/package=PersianStemmer>), 'udpipe' (Wijffels,
J., et al. (2023). <https://CRAN.R-project.org/package=udpipe>), and
'shiny' (Chang, W., et al. (2023).
<https://CRAN.R-project.org/package=shiny>) packages.

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
