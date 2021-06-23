%global __brp_check_rpaths %{nil}
%global packname  FlexGAM
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Additive Models with Flexible Response Functions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-mgcv >= 1.8.23
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-mgcv >= 1.8.23
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-scam 
Requires:         R-splines 
Requires:         R-stats 

%description
Standard generalized additive models assume a response function, which
induces an assumption on the shape of the distribution of the response.
However, miss-specifying the response function results in biased
estimates. Therefore in Spiegel et al. (2017)
<doi:10.1007/s11222-017-9799-6> we propose to estimate the response
function jointly with the covariate effects. This package provides the
underlying functions to estimate these generalized additive models with
flexible response functions. The estimation is based on an iterative
algorithm. In the outer loop the response function is estimated, while in
the inner loop the covariate effects are determined. For the response
function a strictly monotone P-spline is used while the covariate effects
are estimated based on a modified Fisher-Scoring algorithm. Overall the
estimation relies on the 'mgcv'-package.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
