%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stgam
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially and Temporally Varying Coefficient Models Using Generalized Additive Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv >= 1.9.1
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-mgcv >= 1.9.1
Requires:         R-CRAN-glue 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 

%description
A framework for specifying spatially, temporally and
spatially-and-temporally varying coefficient models using Generalized
Additive Models with smooths. The smooths are parameterised with location,
time and predictor variables. The framework supports the investigation of
the presence and nature of any space-time dependencies in the data by
evaluating multiple model forms (specifications) using a Generalized
Cross-Validation score. The workflow sequence is to: i) Prepare the data
by lengthening it to have a single location and time variables for each
observation. ii) Evaluate all possible spatial and/or temporal models in
which each predictor is specified in different ways. iii) Evaluate each
model and pick the best one. iv) Create the final model. v) Calculate the
varying coefficient estimates to quantify how the relationships between
the target and predictor variables vary over space, time or space-time.
vi) Create maps, time series plots etc. For more details see: Comber et al
(2023) <doi:10.4230/LIPIcs.GIScience.2023.22>, Comber et al (2024)
<doi:10.1080/13658816.2023.2270285> and Comber et al (2004)
<doi:10.3390/ijgi13120459>.

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
