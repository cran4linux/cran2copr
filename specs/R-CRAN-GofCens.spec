%global __brp_check_rpaths %{nil}
%global packname  GofCens
%global packver   0.92
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.92
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Methods for Right-Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-survsim 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-survsim 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Graphical tools and goodness-of-fit tests for right-censored data: 1.
Kolmogorov-Smirnov, Crámer-von Mises, and Anderson-Darling tests based on
the empirical distribution function for complete data and their extensions
for right-censored data. 2. Generalized chi-squared-type tests based on
the squared difference between observed and expected counts using random
cells with right-censored data. 3. A series of graphical tools such as
probability or cumulative hazard plots to guide the decision about the
parametric model that best fits the data.

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
