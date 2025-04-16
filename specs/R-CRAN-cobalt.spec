%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cobalt
%global packver   4.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate Balance Tables and Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-crayon >= 1.5.3
BuildRequires:    R-CRAN-rlang >= 1.1.5
BuildRequires:    R-CRAN-gtable >= 0.3.6
BuildRequires:    R-CRAN-chk >= 0.10.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-crayon >= 1.5.3
Requires:         R-CRAN-rlang >= 1.1.5
Requires:         R-CRAN-gtable >= 0.3.6
Requires:         R-CRAN-chk >= 0.10.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-grDevices 

%description
Generate balance tables and plots for covariates of groups preprocessed
through matching, weighting or subclassification, for example, using
propensity scores. Includes integration with 'MatchIt', 'WeightIt',
'MatchThem', 'twang', 'Matching', 'optmatch', 'CBPS', 'ebal', 'cem',
'sbw', and 'designmatch' for assessing balance on the output of their
preprocessing functions. Users can also specify data for balance
assessment not generated through the above packages. Also included are
methods for assessing balance in clustered or multiply imputed data sets
or data sets with multi-category, continuous, or longitudinal treatments.

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
