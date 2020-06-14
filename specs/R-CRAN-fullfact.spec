%global packname  fullfact
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Full Factorial Breeding Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-afex 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-afex 

%description
We facilitate the analysis of full factorial mating designs with
mixed-effects models. The observed data functions extract the variance
explained by random and fixed effects and provide their significance. We
then calculate the additive genetic, nonadditive genetic, and maternal
variance components explaining the phenotype. In particular, we integrate
nonnormal error structures for estimating these components for nonnormal
data types. The resampled data functions are used to produce bootstrap
confidence intervals, which can then be plotted using a simple function.
This package will facilitate the analyses of full factorial mating designs
in R, especially for the analysis of binary, proportion, and/or count data
types and for the ability to incorporate additional random and fixed
effects and power analyses. The paper associated with the package
including worked examples is: Houde ALS, Pitcher TE (2016)
<doi:10.1002/ece3.1943>.

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
%{rlibdir}/%{packname}/INDEX
