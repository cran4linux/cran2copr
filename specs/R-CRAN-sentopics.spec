%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sentopics
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Joint Sentiment and Topic Analysis of Textual Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-quanteda >= 3.2.0
BuildRequires:    R-CRAN-data.table >= 1.13.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-RcppHungarian 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-quanteda >= 3.2.0
Requires:         R-CRAN-data.table >= 1.13.6
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-methods 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-RcppHungarian 

%description
A framework that joins topic modeling and sentiment analysis of textual
data. The package implements a fast Gibbs sampling estimation of Latent
Dirichlet Allocation (Griffiths and Steyvers (2004)
<doi:10.1073/pnas.0307752101>) and Joint Sentiment/Topic Model (Lin, He,
Everson and Ruger (2012) <doi:10.1109/TKDE.2011.48>). It offers a variety
of helpers and visualizations to analyze the result of topic modeling. The
framework also allows enriching topic models with dates and externally
computed sentiment measures. A flexible aggregation scheme enables the
creation of time series of sentiment or topical proportions from the
enriched topic models. Moreover, a novel method jointly aggregates topic
proportions and sentiment measures to derive time series of topical
sentiment.

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
