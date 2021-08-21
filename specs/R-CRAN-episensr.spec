%global __brp_check_rpaths %{nil}
%global packname  episensr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Sensitivity Analysis of Epidemiological Results

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-trapezoid 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-dagitty 
BuildRequires:    R-CRAN-ggdag 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-trapezoid 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-dagitty 
Requires:         R-CRAN-ggdag 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-magrittr 

%description
Basic sensitivity analysis of the observed relative risks adjusting for
unmeasured confounding and misclassification of the exposure/outcome, or
both. It follows the bias analysis methods and examples from the book by
Lash T.L, Fox M.P, and Fink A.K. "Applying Quantitative Bias Analysis to
Epidemiologic Data", ('Springer', 2009).

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
