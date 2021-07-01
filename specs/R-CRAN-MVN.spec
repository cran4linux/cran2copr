%global __brp_check_rpaths %{nil}
%global packname  MVN
%global packver   5.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.9
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Normality Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-car 
Requires:         R-methods 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-car 

%description
Performs multivariate normality tests and graphical approaches and
implements multivariate outlier detection and univariate normality of
marginal distributions through plots and tests, and performs multivariate
Box-Cox transformation (Korkmaz et al, (2014),
<https://journal.r-project.org/archive/2014-2/korkmaz-goksuluk-zararsiz.pdf>).

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
