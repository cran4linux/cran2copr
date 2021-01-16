%global packname  convoSPAT
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Convolution-Based Nonstationary Spatial Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-StatMatch 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-StatMatch 

%description
Fits convolution-based nonstationary Gaussian process models to
point-referenced spatial data. The nonstationary covariance function
allows the user to specify the underlying correlation structure and which
spatial dependence parameters should be allowed to vary over space: the
anisotropy, nugget variance, and process variance. The parameters are
estimated via maximum likelihood, using a local likelihood approach. Also
provided are functions to fit stationary spatial models for comparison,
calculate the Kriging predictor and standard errors, and create various
plots to visualize nonstationarity.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
