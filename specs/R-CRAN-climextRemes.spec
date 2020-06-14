%global packname  climextRemes
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Tools for Analyzing Climate Extremes

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-extRemes >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-boot 
Requires:         R-CRAN-extRemes >= 2.0.0
Requires:         R-methods 
Requires:         R-boot 

%description
Functions for fitting GEV and POT (via point process fitting) models for
extremes in climate data, providing return values, return probabilities,
and return periods for stationary and nonstationary models. Also provides
differences in return values and differences in log return probabilities
for contrasts of covariate values. Functions for estimating risk ratios
for event attribution analyses, including uncertainty. Under the hood,
many of the functions use functions from 'extRemes', including for fitting
the statistical models. Details are given in Paciorek, Stone, and Wehner
(2018) <doi:10.1016/j.wace.2018.01.002>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/conda
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/pip
%doc %{rlibdir}/%{packname}/python
%doc %{rlibdir}/%{packname}/python_help
%doc %{rlibdir}/%{packname}/python_wrapper
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
