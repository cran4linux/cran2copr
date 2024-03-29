%global __brp_check_rpaths %{nil}
%global packname  Twitmo
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Twitter Topic Modeling and Visualization for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rtweet 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-quanteda.textstats 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-stm 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-LDAvis 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-ldatuning 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tm 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rtweet 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-quanteda.textstats 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-stm 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-LDAvis 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-ldatuning 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tm 

%description
Tailored for topic modeling with tweets and fit for visualization tasks in
R. Collect, pre-process and analyze the contents of tweets using LDA and
structural topic models (STM). Comes with visualizing capabilities like
tweet and hashtag maps and built-in support for 'LDAvis'.

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
