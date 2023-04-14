%global __brp_check_rpaths %{nil}
%global packname  BMT
%global packver   0.1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          The BMT Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-fitdistrplus 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-fitdistrplus 

%description
Density, distribution, quantile function, random number generation for the
BMT (Bezier-Montenegro-Torres) distribution. Torres-Jimenez C.J. and
Montenegro-Diaz A.M. (2017) <arXiv:1709.05534>. Moments, descriptive
measures and parameter conversion for different parameterizations of the
BMT distribution. Fit of the BMT distribution to non-censored data by
maximum likelihood, moment matching, quantile matching, maximum
goodness-of-fit, also known as minimum distance, maximum product of
spacing, also called maximum spacing, and minimum quantile distance, which
can also be called maximum quantile goodness-of-fit. Fit of univariate
distributions for non-censored data using maximum product of spacing
estimation and minimum quantile distance estimation is also included.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
