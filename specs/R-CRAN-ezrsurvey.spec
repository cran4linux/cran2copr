%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ezrsurvey
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Line Helpers for Consumer Survey Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-withr 

%description
Simplifies the day-to-day work of research and insights professionals who
analyse consumer and customer survey data but have limited coding
experience. Wraps common 'tidyverse' patterns into single-line functions
for the tasks these teams repeat constantly: loading and combining survey
exports, turning questions into percentages and summaries, recoding rating
and Net Promoter scales, deriving demographics such as age cohorts and
regions, modelling the drivers of satisfaction, checking sampling
precision, selecting illustrative open-text comments, and producing
presentation-ready charts and reports. A simulated consumer-survey dataset
is included for learning and examples. Weighting rakes to target margins
as in Deming and Stephan (1940) <doi:10.1214/aoms/1177731829> and reports
the design effect of Kish (1965, ISBN:978-0-471-10949-5); driver models
use the relative weights of Johnson (2000)
<doi:10.1207/S15327906MBR3501_1> or the random forests of Breiman (2001)
<doi:10.1023/A:1010933404324>; the Net Promoter Score follows Reichheld
(2003) <https://hbr.org/2003/12/the-one-number-you-need-to-grow>; and
diverse comments are chosen by maximal marginal relevance as in Carbonell
and Goldstein (1998) <doi:10.1145/290941.291025>.

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
