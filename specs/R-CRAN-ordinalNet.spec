%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ordinalNet
%global packver   2.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.14
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Ordinal Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Fits ordinal regression models with elastic net penalty. Supported model
families include cumulative probability, stopping ratio, continuation
ratio, and adjacent category. These families are a subset of vector glm's
which belong to a model class we call the elementwise link
multinomial-ordinal (ELMO) class. Each family in this class links a vector
of covariates to a vector of class probabilities. Each of these families
has a parallel form, which is appropriate for ordinal response data, as
well as a nonparallel form that is appropriate for an unordered
categorical response, or as a more flexible model for ordinal data. The
parallel model has a single set of coefficients, whereas the nonparallel
model has a set of coefficients for each response category except the
baseline category. It is also possible to fit a model with both parallel
and nonparallel terms, which we call the semi-parallel model. The
semi-parallel model has the flexibility of the nonparallel model, but the
elastic net penalty shrinks it toward the parallel model. For details,
refer to Wurm, Hanlon, and Rathouz (2021) <doi:10.18637/jss.v099.i06>.

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
