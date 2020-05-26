%global packname  distributionsrd
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}
Summary:          Distribution Fitting and Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-modeltools 
Requires:         R-methods 

%description
A library of density, distribution function, quantile function, (bounded)
raw moments and random generation for a collection of distributions
relevant for the firm size literature. Additionally, the package contains
tools to fit these distributions using maximum likelihood and evaluate
these distributions based on (i) log-likelihood ratio and (ii) deviations
between the empirical and parametrically implied moments of the
distributions. We add flexibility by allowing the considered distributions
to be combined into piecewise composite or finite mixture distributions,
as well as to be used when truncated. See Dewitte (2020)
<https://hdl.handle.net/1854/LU-8644700> for a description and application
of methods available in this package.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
