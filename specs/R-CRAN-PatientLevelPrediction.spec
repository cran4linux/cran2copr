%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PatientLevelPrediction
%global packver   6.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Develop Clinical Prediction Models Using the Common Data Model

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DatabaseConnector >= 6.0.0
BuildRequires:    R-CRAN-Cyclops >= 3.0.0
BuildRequires:    R-CRAN-FeatureExtraction >= 3.0.0
BuildRequires:    R-CRAN-ParallelLogger >= 2.0.0
BuildRequires:    R-CRAN-SqlRender >= 1.1.3
BuildRequires:    R-CRAN-Andromeda 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-memuse 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-DatabaseConnector >= 6.0.0
Requires:         R-CRAN-Cyclops >= 3.0.0
Requires:         R-CRAN-FeatureExtraction >= 3.0.0
Requires:         R-CRAN-ParallelLogger >= 2.0.0
Requires:         R-CRAN-SqlRender >= 1.1.3
Requires:         R-CRAN-Andromeda 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-memuse 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-PRROC 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
A user friendly way to create patient level prediction models using the
Observational Medical Outcomes Partnership Common Data Model. Given a
cohort of interest and an outcome of interest, the package can use data in
the Common Data Model to build a large set of features. These features can
then be used to fit a predictive model with a number of machine learning
algorithms. This is further described in Reps (2017)
<doi:10.1093/jamia/ocy032>.

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
