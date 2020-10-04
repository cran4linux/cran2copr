%global packname  MVNtestchar
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Test for Multivariate Normal Distribution Based on aCharacterization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 

%description
Provides a test of multivariate normality of an unknown sample that does
not require estimation of the nuisance parameters, the mean and covariance
matrix.  Rather, a sequence of transformations removes these nuisance
parameters and results in a set of sample matrices that are positive
definite.  These matrices are uniformly distributed on the space of
positive definite matrices in the unit hyper-rectangle if and only if the
original data is multivariate normal (Fairweather, 1973, Doctoral
dissertation, University of Washington). The package performs a goodness
of fit test of this hypothesis. In addition to the test, functions in the
package give visualizations of the support region of positive definite
matrices for bivariate samples.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
