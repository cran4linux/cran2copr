%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prediction
%global packver   0.3.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.18
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy, Type-Safe 'prediction()' Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-data.table 

%description
A one-function package containing prediction(), a type-safe alternative to
predict() that always returns a data frame. The summary() method provides
a data frame with average predictions, possibly over counterfactual
versions of the data (à la the margins command in 'Stata'). Marginal
effect estimation is provided by the related package, 'margins'
<https://cran.r-project.org/package=margins>. The package currently
supports common model types (e.g., lm, glm) from the 'stats' package, as
well as numerous other model classes from other add-on packages. See the
README file or main package documentation page for a complete listing.

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
