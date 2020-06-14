%global packname  probhat
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Multivariate Generalized Kernel Smoothing and RelatedStatistical Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intoo 
BuildRequires:    R-CRAN-barsurf 
BuildRequires:    R-CRAN-kubik 
Requires:         R-CRAN-intoo 
Requires:         R-CRAN-barsurf 
Requires:         R-CRAN-kubik 

%description
Constructs, plots and evaluates probability distributions (probability
mass/density functions, cumulative distribution functions and quantile
functions) with continuous kernel smoothing, and to a lesser extent,
discrete kernel smoothing. Supports univariate, multivariate and
conditional distributions, including multivariate-conditional
distributions. Also, supports other probability distributions
(categorical, frequency and empirical-like) and weighted data, which is
possibly useful mixed with fuzzy clustering. Furthermore, there are
extensions for computing multivariate probabilities and multivariate
random numbers, and for parameter and mode estimation.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
