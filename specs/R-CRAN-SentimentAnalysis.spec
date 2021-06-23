%global __brp_check_rpaths %{nil}
%global packname  SentimentAnalysis
%global packver   1.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Dictionary-Based Sentiment Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spikeslab >= 1.1
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-CRAN-ngramrr >= 0.1
BuildRequires:    R-CRAN-qdapDictionaries 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-spikeslab >= 1.1
Requires:         R-CRAN-tm >= 0.6
Requires:         R-CRAN-ngramrr >= 0.1
Requires:         R-CRAN-qdapDictionaries 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 

%description
Performs a sentiment analysis of textual contents in R. This
implementation utilizes various existing dictionaries, such as Harvard IV,
or finance-specific dictionaries. Furthermore, it can also create
customized dictionaries. The latter uses LASSO regularization as a
statistical approach to select relevant terms based on an exogenous
response variable.

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
