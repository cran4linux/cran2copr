%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  respondeR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Imputing Responder Proportions from Continuous Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Express meta-analyses of continuous trial outcomes in terms of responder
risks, following the interpretability tutorial of Thorlund, Walter,
Johnston, Furukawa and Guyatt (2011) <doi:10.1002/jrsm.46>. Given the mean
change, standard deviation and sample size per arm across studies,
respondeR estimates the proportion of patients who cross a minimal
important difference (MID) threshold under a parametric model for the
change scores, and contrasts the arms as a risk difference, risk ratio,
odds ratio or number needed to treat. It provides per-study (fixed- or
random-effects) pooling with exact tail probabilities, a pooled-summary
method anchored on the within-study mean difference, median and
unweighted-mean summaries, the standardized-mean-difference to odds-ratio
bridge of Anzures-Cabrera, Sarpatwari and Higgins (2011)
<doi:10.1002/sim.4298>, a threshold-free common-language effect size,
results across a range of thresholds, GRADE summary-of-findings rows,
change-score standard deviation imputation, shared-control handling for
multi-arm trials, and a point-and-click 'Shiny' application. It can also
read a continuous meta-analysis already fitted with 'meta' or 'metafor'
and convert it to responder risks. The framework follows the simulation
study of Sofi-Mahmudi (2024) <https://hdl.handle.net/11375/30210>.

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
