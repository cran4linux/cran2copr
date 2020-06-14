%global packname  copula
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Multivariate Dependence with Copulas

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-stabledist >= 0.6.4
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-Matrix 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-ADGofTest 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-stabledist >= 0.6.4
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-Matrix 
Requires:         R-lattice 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-ADGofTest 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-numDeriv 

%description
Classes (S4) of commonly used elliptical, Archimedean, extreme-value and
other copula families, as well as their rotations, mixtures and
asymmetrizations. Nested Archimedean copulas, related tools and special
functions. Methods for density, distribution, random number generation,
bivariate dependence measures, Rosenblatt transform, Kendall distribution
function, perspective and contour plots. Fitting of copula models with
potentially partly fixed parameters, including standard errors. Serial
independence tests, copula specification tests (independence,
exchangeability, radial symmetry, extreme-value dependence,
goodness-of-fit) and model selection based on cross-validation. Empirical
copula, smoothed versions, and non-parametric estimators of the Pickands
dependence function.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/docs
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/rData
%doc %{rlibdir}/%{packname}/Rsource
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
