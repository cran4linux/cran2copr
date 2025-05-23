%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  apm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Averaged Prediction Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-pbapply >= 1.7.2
BuildRequires:    R-CRAN-ggrepel >= 0.9.6
BuildRequires:    R-CRAN-fwb >= 0.3.0
BuildRequires:    R-CRAN-ggh4x >= 0.2.8
BuildRequires:    R-CRAN-chk >= 0.10.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-pbapply >= 1.7.2
Requires:         R-CRAN-ggrepel >= 0.9.6
Requires:         R-CRAN-fwb >= 0.3.0
Requires:         R-CRAN-ggh4x >= 0.2.8
Requires:         R-CRAN-chk >= 0.10.0
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sandwich 

%description
In panel data settings, specifies set of candidate models, fits them to
data from pre-treatment validation periods, and selects model as average
over candidate models, weighting each by posterior probability of being
most robust given its differential average prediction errors in
pre-treatment validation periods. Subsequent estimation and inference of
causal effect's bounds accounts for both model and sampling uncertainty,
and calculates the robustness changepoint value at which bounds go from
excluding to including 0. The package also includes a range of diagnostic
plots, such as those illustrating models' differential average prediction
errors and the posterior distribution of which model is most robust.

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
