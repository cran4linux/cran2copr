%global packname  bamlss
%global packver   1.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}
Summary:          Bayesian Additive Models for Location, Scale, and Shape (andBeyond)

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-Matrix 
BuildRequires:    R-survival 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-colorspace 
Requires:         R-mgcv 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sp 
Requires:         R-Matrix 
Requires:         R-survival 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-raster 

%description
Infrastructure for estimating probabilistic distributional regression
models in a Bayesian framework. The distribution parameters may capture
location, scale, shape, etc. and every parameter may depend on complex
additive terms (fixed, random, smooth, spatial, etc.) similar to a
generalized additive model. The conceptual and computational framework is
introduced in Umlauf, Klein, Zeileis (2019)
<doi:10.1080/10618600.2017.1407325> and the R package in Umlauf, Klein,
Simon, Zeileis (2019) <arXiv:1909.11784>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
