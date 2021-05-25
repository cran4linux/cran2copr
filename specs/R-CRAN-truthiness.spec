%global packname  truthiness
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Illusory Truth Longitudinal Study

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ez 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ez 

%description
Data and functions for analyzing and simulating illusory truth datasets,
developed as part of a longitudinal study by Henderson, Barr, and Simons
(2020). The illusory truth effect is the observation that people rate
repeated statements as more likely to be true than novel statements. We
tested the trajectory of the illusory truth effect by collecting truth
ratings for statements repeated across four time intervals: immediately,
one day, one week, and one month following initial presentation. The
package contains the anonymized data from the study along with stimulus
materials, as well as functions for analyzing the data, running
simulations, and calculating power. Further details about the project are
available at <https://osf.io/nvugt/>, which includes Stage 1 of the
Registered Report at the Journal of Cognition (<https://osf.io/vqnx2/>).

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
