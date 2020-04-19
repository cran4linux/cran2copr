%global packname  MVNtestchar
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Multivariate Normal Distribution Characterization Test

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
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 

%description
Provides a test of multivariate normality of a sample which does not
require estimation of the nuisance parameters, the mean and covariance
matrix.  Rather, a sequence of transformations removes these nuisance
parameters and results in a set of sample matrices that are positive
definite.  These matrices are uniformly distributed on the space of
positive definite matrices in the unit hyperrectangle if and only if the
original data is multivariate normal. The package performs a goodness of
fit test of this hypothesis. Four sample datasets are included: a
bivariate and a trivariate normal set and a bivariate and trivariate
Bernoulli set. In addition to the test, functions in the package give
rotatable visualizations of the support region of positive definite
matrices for bivariate samples.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
