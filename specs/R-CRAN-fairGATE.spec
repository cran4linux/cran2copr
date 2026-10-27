%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fairGATE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fair Gated Algorithm for Targeted Equity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggalluvial 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggalluvial 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Fairness-aware correction of a prediction model for binary and continuous
outcomes with two or more protected groups and their intersections. A
cross-fitted base learner (gradient-boosted trees or a neural network) is
fitted without the protected attribute, and a gated mixture of neural
experts learns a per-person correction to its score under a fairness
penalty (a random-effects or variance penalty on outcome-stratified group
means, or a thresholded worst-group penalty on error rates), with a
cross-fitted disparity signal, an intervention cost, smoothed early
stopping, a per-person export of adjustments with bootstrap stability
intervals, and routing analyses of which expert corrects whom. Methods
draw on mixture-of-experts neural networks by Jordan and Jacobs (1994)
<doi:10.1007/978-1-4471-2097-1_113>, gradient boosting by Chen and
Guestrin (2016) <doi:10.1145/2939672.2939785>, cross-fitting by
Chernozhukov and co-authors (2018) <doi:10.1111/ectj.12097>, equalised
odds by Hardt, Price and Srebro (2016) <doi:10.48550/arXiv.1610.02413>,
the random-effects variance estimator of DerSimonian and Laird (1986)
<doi:10.1016/0197-2456(86)90046-2>, and personalised treatment prediction
for depression by Iniesta, Stahl and McGuffin (2016)
<doi:10.1016/j.jpsychires.2016.03.016>.

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
