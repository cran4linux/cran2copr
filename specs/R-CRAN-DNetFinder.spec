%global packname  DNetFinder
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Estimating Differential Networks under Semiparametric GaussianGraphical Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flare 
BuildRequires:    R-stats 
Requires:         R-CRAN-flare 
Requires:         R-stats 

%description
Provides a modified hierarchical test (Liu (2017)
<doi:10.1214/17-AOS1539>) for detecting the structural difference between
two Semiparametric Gaussian graphical models. The multiple testing
procedure asymptotically controls the false discovery rate (FDR) at a
user-specified level. To construct the test statistic, a truncated
estimator is used to approximate the transformation functions and two R
functions including lassoGGM() and lassoNPN() are provided to compute the
lasso estimates of the regression coefficients.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
