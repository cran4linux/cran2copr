%global packname  simplexreg
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Regression Analysis of Proportional Data Using SimplexDistribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel >= 1.8
Requires:         gsl
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-plotrix 
Requires:         R-graphics 
Requires:         R-stats 

%description
Simplex density, distribution, quantile functions as well as random
variable generation of the simplex distribution are given. Regression
analysis of proportional data using various kinds of simplex models is
available. In addition, GEE method can be applied to longitudinal data to
model the correlation. Residual analysis is also involved. Some
subroutines are written in C with GNU Scientific Library (GSL) so as to
facilitate the computation.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
