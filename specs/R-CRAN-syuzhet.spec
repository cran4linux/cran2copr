%global packname  syuzhet
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Extracts Sentiment and Sentiment-Derived Plot Arcs from Text

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-textshape >= 1.3.0
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-dtt 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-textshape >= 1.3.0
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-dtt 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 

%description
Extracts sentiment and sentiment-derived plot arcs from text using a
variety of sentiment dictionaries conveniently packaged for consumption by
R users.  Implemented dictionaries include "syuzhet" (default) developed
in the Nebraska Literary Lab "afinn" developed by Finn Årup Nielsen,
"bing" developed by Minqing Hu and Bing Liu, and "nrc" developed by
Mohammad, Saif M. and Turney, Peter D. Applicable references are available
in README.md and in the documentation for the "get_sentiment" function.
The package also provides a hack for implementing Stanford's coreNLP
sentiment parser. The package provides several methods for plot arc
normalization.

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
