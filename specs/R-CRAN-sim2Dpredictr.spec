%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sim2Dpredictr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Outcomes Using Spatially Dependent Design Matrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spam >= 2.2.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-spam >= 2.2.0
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-matrixcalc 

%description
Provides tools for simulating spatially dependent predictors (continuous
or binary), which are used to generate scalar outcomes in a (generalized)
linear model framework. Continuous predictors are generated using
traditional multivariate normal distributions or Gauss Markov random
fields with several correlation function approaches (e.g., see Rue (2001)
<doi:10.1111/1467-9868.00288> and Furrer and Sain (2010)
<doi:10.18637/jss.v036.i10>), while binary predictors are generated using
a Boolean model (see Cressie and Wikle (2011, ISBN: 978-0-471-69274-4)).
Parameter vectors exhibiting spatial clustering can also be easily
specified by the user.

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
