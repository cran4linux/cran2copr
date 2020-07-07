%global packname  frechet
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Statistical Analysis for Random Objects and Non-Euclidean Data

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fdapace >= 0.5.3
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-fdadensity 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rosqp 
Requires:         R-CRAN-fdapace >= 0.5.3
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-fdadensity 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rosqp 

%description
Provides implementation of statistical methods for random objects lying in
various metric spaces, which are not necessarily linear spaces. The core
of this package is Fréchet regression for random objects with Euclidean
predictors, which allows one to perform regression analysis for
non-Euclidean responses under some mild conditions. Examples include
distributions in L^2-Wasserstein space, covariance matrices endowed with
power metric (with Frobenius metric as a special case), Cholesky and
log-Cholesky metrics. References: Petersen, A., & Müller, H.-G. (2019)
<doi:10.1214/17-AOS1624>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
