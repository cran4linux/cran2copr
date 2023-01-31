%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scoringutils
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Scoring and Assessing Predictions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-ggdist >= 3.2.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scoringRules 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-ggdist >= 3.2.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scoringRules 
Requires:         R-stats 

%description
Provides a collection of metrics and proper scoring rules (Tilmann
Gneiting & Adrian E Raftery (2007) <doi:10.1198/016214506000001437>,
Jordan, A., Krüger, F., & Lerch, S. (2019) <doi:10.18637/jss.v090.i12>)
within a consistent framework for evaluation, comparison and visualisation
of forecasts. In addition to proper scoring rules, functions are provided
to assess bias, sharpness and calibration (Sebastian Funk, Anton Camacho,
Adam J. Kucharski, Rachel Lowe, Rosalind M. Eggo, W. John Edmunds (2019)
<doi:10.1371/journal.pcbi.1006785>) of forecasts. Several types of
predictions (e.g. binary, discrete, continuous) which may come in
different formats (e.g. forecasts represented by predictive samples or by
quantiles of the predictive distribution) can be evaluated. Scoring
metrics can be used either through a convenient data.frame format, or can
be applied as individual functions in a vector / matrix format. All
functionality has been implemented with a focus on performance and is
robustly tested.

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
