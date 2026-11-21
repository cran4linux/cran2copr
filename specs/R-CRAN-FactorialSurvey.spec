%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FactorialSurvey
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analysis of Factorial Survey (Vignette) Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-AlgDesign 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-AlgDesign 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-sandwich 

%description
An integrated workflow for factorial survey (vignette) experiments.
Constructs D-efficient sets of vignettes from a factorial structure and
reports their D- and A-efficiency following Kuhfeld, Tobias and Garratt
(1994) <doi:10.1177/002224379403100408>, allocates them to blocks and to
respondents in carryover-balanced orders, renders them as prose, and
writes them out for survey platforms. Simulates responses to evaluate
statistical power before fielding. Estimates beta regression models for
bounded ratings and logit models for yes/no responses, with standard
errors clustered by respondent, and derives average marginal effects,
marginal willingness to pay and the expected willingness to pay for
complete policy scenarios. The latter is the mean of willingness to pay
truncated at zero, Hanemann (1989) <doi:10.2307/1242685>, applied to
factorial surveys as in Tanaka et al. (2027)
<doi:10.1016/j.tra.2026.105293>. Efficient designs and optimal blocking
use the exchange algorithms of Fedorov (1972, ISBN:0122507509) as
implemented in 'AlgDesign'. Presentation orders follow Williams (1949)
<doi:10.1071/CH9490149>. Beta regression follows Ferrari and Cribari-Neto
(2004) <doi:10.1080/0266476042000214501>. Bounded ratings are mapped to
the open unit interval following Smithson and Verkuilen (2006)
<doi:10.1037/1082-989X.11.1.54>.

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
