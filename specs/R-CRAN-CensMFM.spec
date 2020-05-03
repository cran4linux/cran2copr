%global packname  CensMFM
%global packver   2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.11
Release:          1%{?dist}
Summary:          Finite Mixture of Multivariate Censored/Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MomTrunc >= 5.87
BuildRequires:    R-CRAN-tlrmvnmvt >= 1.1.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MomTrunc >= 5.87
Requires:         R-CRAN-tlrmvnmvt >= 1.1.0
Requires:         R-CRAN-mvtnorm >= 1.0.11
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 

%description
It fits finite mixture models for censored or/and missing data using
several multivariate distributions. Point estimation and asymptotic
inference (via empirical information matrix) are offered as well as
censored data generation. Pairwise scatter and contour plots can be
generated. Possible multivariate distributions are the well-known normal,
Student-t and skew-normal distributions. This package is an complement of
Lachos, V. H., Moreno, E. J. L., Chen, K. & Cabral, C. R. B. (2017)
<doi:10.1016/j.jmva.2017.05.005> for the multivariate skew-normal case.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
