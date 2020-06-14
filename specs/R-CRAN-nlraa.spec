%global packname  nlraa
%global packver   0.73
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.73
Release:          2%{?dist}
Summary:          Nonlinear Regression for Agricultural Applications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-mgcv 
BuildRequires:    R-nlme 
BuildRequires:    R-stats 
Requires:         R-boot 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-mgcv 
Requires:         R-nlme 
Requires:         R-stats 

%description
Additional nonlinear regression functions using self-start (SS)
algorithms. One of the functions is the Beta growth function proposed by
Yin et al. (2003) <doi:10.1093/aob/mcg029>. There are several other
functions with breakpoints (e.g. linear-plateau, plateau-linear,
exponential-plateau, plateau-exponential, quadratic-plateau,
plateau-quadratic and bilinear), a non-rectangular hyperbola and a
bell-shaped curve. Twenty one (21) new self-start (SS) functions in total.
This package also supports the publication 'Nonlinear regression Models
and applications in agricultural research' by Archontoulis and Miguez
(2015) <doi:10.2134/agronj2012.0506>, a book chapter with similar material
<doi:10.2134/appliedstatistics.2016.0003.c15> and a publication by Oddi
et. al. (2019) in Ecology and Evolution <doi:10.1002/ece3.5543>. The
function 'nlsLMList' uses nlsLM for fitting, but it is otherwise almost
identical to 'nlme::nlsList'.In addition, this release of the package
provides functions for conducting simulation for 'nlme' and 'gnls' objects
as well as bootstrapping. These functions are intended to work with the
modeling framework of the 'nlme' package. It also provides four vignettes
with extended examples.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
