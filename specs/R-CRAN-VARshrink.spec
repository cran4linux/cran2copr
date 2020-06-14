%global packname  VARshrink
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Shrinkage Estimation Methods for Vector Autoregressive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.9
BuildRequires:    R-CRAN-vars >= 1.5.3
BuildRequires:    R-CRAN-ars >= 0.6
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-corpcor >= 1.6.9
Requires:         R-CRAN-vars >= 1.5.3
Requires:         R-CRAN-ars >= 0.6
Requires:         R-CRAN-strucchange 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Vector autoregressive (VAR) model is a fundamental and effective approach
for multivariate time series analysis. Shrinkage estimation methods can be
applied to high-dimensional VAR models with dimensionality greater than
the number of observations, contrary to the standard ordinary least
squares method. This package is an integrative package delivering
nonparametric, parametric, and semiparametric methods in a unified and
consistent manner, such as the multivariate ridge regression in Golub,
Heath, and Wahba (1979) <doi:10.2307/1268518>, a James-Stein type
nonparametric shrinkage method in Opgen-Rhein and Strimmer (2007)
<doi:10.1186/1471-2105-8-S2-S3>, and Bayesian estimation methods using
noninformative and informative priors in Lee, Choi, and S.-H. Kim (2016)
<doi:10.1016/j.csda.2016.03.007> and Ni and Sun (2005)
<doi:10.1198/073500104000000622>.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
