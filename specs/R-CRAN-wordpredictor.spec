%global packname  wordpredictor
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Develop Text Prediction Models Based on N-Grams

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-SnowballC 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-SnowballC 

%description
A framework for developing n-gram models for text prediction. It provides
data cleaning, data sampling, extracting tokens from text, model
generation, model evaluation and word prediction. For information on how
n-gram models work we referred to: "Speech and Language Processing"
<https://web.stanford.edu/~jurafsky/slp3/3.pdf>. For optimizing R code and
using R6 classes we referred to "Advanced R"
<https://adv-r.hadley.nz/r6.html>. For writing R extensions we referred to
"R Packages", <https://r-pkgs.org/index.html>.

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
