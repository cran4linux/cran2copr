%global packname  npsf
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          2%{?dist}
Summary:          Nonparametric and Stochastic Efficiency and ProductivityAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Formula 

%description
Nonparametric efficiency measurement and statistical inference via DEA
type of estimators (see e.g., Kneip, Simar, and Wilson (2008)
<doi:10.1017/S0266466608080651> and Badunenko and Mozharovskyi (2020)
<doi:10.1080/01605682.2019.1599778>) as well as Stochastic Frontier
estimators for both cross-sectional data and 1st, 2nd, and 4th generation
models for panel data (see e.g., Kumbhakar and Lovell (2003), Badunenko
and Kumbhakar (2016) <doi:10.1016/j.ejor.2016.04.049>). The stochastic
frontier estimators can handle both half-normal and truncated normal
models with conditional mean and heteroskedasticity. The marginal effects
of determinants can be obtained.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
