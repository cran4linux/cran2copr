%global __brp_check_rpaths %{nil}
%global packname  tsentiment
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fetching Tweet Data for Sentiment Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-wordcloud2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-syuzhet 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-wordcloud2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-syuzhet 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-stringi 

%description
Which uses Twitter APIs for the necessary data in sentiment analysis, acts
as a middleware with the approved Twitter Application. A special access
key is given to users who subscribe to the application with their Twitter
account. With this special access key, the user defined keyword for
sentiment analysis can be searched in twitter recent searches and results
can be obtained( more information
<https://github.com/hakkisabah/tsentiment> ). In addition, a service named
tsentiment-services has been developed to provide all these operations (
for more information <https://github.com/hakkisabah/tsentiment-services>
). After the successful results obtained and in line with the permissions
given by the user, the results of the analysis of the word cloud and bar
graph saved in the user folder directory can be seen. In each analysis
performed, the previous analysis visual result is deleted and this is the
basic information you need to know as a practice rule. 'tsentiment'
package provides a free service that acts as a middleware for easy data
extraction from Twitter, and in return, the user rate limit is reduced by
30 requests from the total limit and the remaining requests are used.
These 30 requests are reserved for use in application analytics. For
information about endpoints, you can refer to the limit information in the
"GET search/tweets" row in the Endpoints column in the list at
<https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits>.

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
