%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WeatherSentiment
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Analysis of Tweet Sentiments and Weather Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-sentimentr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-sentimentr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-tidyr 

%description
A comprehensive suite of functions for processing, analyzing, and
visualizing textual data from tweets is offered. Users can clean tweets,
analyze their sentiments, visualize data, and examine the correlation
between sentiments and environmental data such as weather conditions. Main
features include text processing, sentiment analysis, data visualization,
correlation analysis, and synthetic data generation. Text processing
involves cleaning and preparing tweets by removing textual noise and
irrelevant words. Sentiment analysis extracts and accurately analyzes
sentiments from tweet texts using advanced algorithms. Data visualization
creates various charts like word clouds and sentiment polarity graphs for
visual representation of data. Correlation analysis examines and
calculates the correlation between tweet sentiments and environmental
variables such as weather conditions. Additionally, random tweets can be
generated for testing and evaluating the performance of analyses,
empowering users to effectively analyze and interpret 'Twitter' data for
research and commercial purposes.

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
