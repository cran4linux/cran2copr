%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  familiar
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          End-to-End Automated Machine Learning and Model Evaluation

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstream 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-rstream 
Requires:         R-CRAN-survival 

%description
Single unified interface for end-to-end modelling of regression,
categorical and time-to-event (survival) outcomes. Models created using
familiar are self-containing, and their use does not require additional
information such as baseline survival, feature clustering, or feature
transformation and normalisation parameters. Model performance,
calibration, risk group stratification, (permutation) variable importance,
individual conditional expectation, partial dependence, and more, are
assessed automatically as part of the evaluation process and exported in
tabular format and plotted, and may also be computed manually using export
and plot functions. Where possible, metrics and values obtained during the
evaluation process come with confidence intervals.

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
