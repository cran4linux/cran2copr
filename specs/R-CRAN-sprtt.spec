%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sprtt
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Probability Ratio Tests Toolbox

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 

%description
It is a toolbox for Sequential Probability Ratio Tests (SPRT), Wald (1945)
<doi:10.2134/agronj1947.00021962003900070011x>. SPRTs are applied to the
data during the sampling process, ideally after each observation. At any
stage, the test will return a decision to either continue sampling or
terminate and accept one of the specified hypotheses. The seq_ttest()
function performs one-sample, two-sample, and paired t-tests for testing
one- and two-sided hypotheses (Schnuerch & Erdfelder (2019)
<doi:10.1037/met0000234>). The seq_anova() function allows to perform a
sequential one-way fixed effects ANOVA (Steinhilber et al. (2023)
<doi:10.31234/osf.io/m64ne>). Learn more about the package by using
vignettes "browseVignettes(package = "sprtt")" or go to the website
<https://meikesteinhilber.github.io/sprtt/>.

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
