%global __brp_check_rpaths %{nil}
%global packname  papci
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prevalence Adjusted PPV Confidence Interval

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-PropCIs 
BuildRequires:    R-CRAN-ratesci 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-PropCIs 
Requires:         R-CRAN-ratesci 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-DT 
Requires:         R-stats 

%description
Positive predictive value (PPV) defined as the conditional probability of
clinical trial assay (CTA) being positive given Companion diagnostic
device (CDx) being positive is a key performance parameter for evaluating
the clinical validity utility of a companion diagnostic test in clinical
bridging studies. When bridging study patients are enrolled based on CTA
assay results, Binomial-based confidence intervals (CI) may are not
appropriate for PPV CI estimation. Bootstrap CIs which are not restricted
by the Binomial assumption may be used for PPV CI estimation only when PPV
is not 100%%. Bootstrap CI is not valid when PPV is 100%% and becomes a
single value of [1, 1]. We proposed a risk ratio-based method for
constructing CI for PPV. By simulation we illustrated that the coverage
probability of the proposed CI is close to the nominal value even when PPV
is high and negative percent agreement (NPA) is close to 100%%. There is a
lack of R package for PPV CI calculation. we developed a publicly
available R package along with this shiny app to implement the proposed
approach and some other existing methods.

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
