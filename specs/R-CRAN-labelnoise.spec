%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  labelnoise
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Find Label Errors in Classification Data with Confident Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
Finds examples whose given class label is likely wrong, using
out-of-sample predicted probabilities from any classifier. Implements
confident learning (Northcutt, Jiang and Chuang, 2021)
<doi:10.1613/jair.1.12125>: per-class confidence thresholds, the confident
joint, calibrated estimates of the joint distribution of given and true
labels, noise transition matrices, and five rank-and-prune rules for
flagging label issues. Also provides model-agnostic label quality scores
(Kuan and Mueller, 2022) <doi:10.5281/zenodo.18168246> and a per-class
label health summary. Inputs can be a label vector with a probability
matrix, a data frame of predictions, resampling results from 'tune',
predictions from 'mlr3', or a fitted 'caret' model.

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
