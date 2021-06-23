%global __brp_check_rpaths %{nil}
%global packname  MSiP
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          'MassSpectrometry' Interaction Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.88
BuildRequires:    R-CRAN-mice >= 3.13.0
BuildRequires:    R-CRAN-tibble >= 3.1.2
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-e1071 >= 1.7.7
BuildRequires:    R-CRAN-PRROC >= 1.3.1
BuildRequires:    R-CRAN-pROC >= 1.17.0.1
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-ranger >= 0.12.1
Requires:         R-CRAN-caret >= 6.0.88
Requires:         R-CRAN-mice >= 3.13.0
Requires:         R-CRAN-tibble >= 3.1.2
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-e1071 >= 1.7.7
Requires:         R-CRAN-PRROC >= 1.3.1
Requires:         R-CRAN-pROC >= 1.17.0.1
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-ranger >= 0.12.1

%description
The 'MSiP' is a computational approach to predict protein-protein
interactions from large-scale affinity purification mass 'spectrometry'
(AP-MS) data. This approach includes both spoke and matrix models for
interpreting AP-MS data in a network context. The "spoke" model considers
only bait-prey interactions, whereas the "matrix" model assumes that each
of the identified proteins (baits and prey) in a given AP-MS experiment
interacts with each of the others. The spoke model has a high
false-negative rate, whereas the matrix model has a high false-positive
rate. Although, both statistical models have merits, a combination of both
models has shown to increase the performance of machine learning
classifiers in terms of their capabilities in discrimination between true
and false positive interactions.

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
