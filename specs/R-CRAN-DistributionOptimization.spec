%global packname  DistributionOptimization
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Distribution Optimization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-AdaptGauss 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-AdaptGauss 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits Gaussian mixtures by applying evolution. As fitness function a
mixture of the chi square test for distributions and a novel measure for
approximating the common area under curves between multiple Gaussians is
used. The package presents an alternative to the commonly used likelihood
maximisation as is used in Expectation maximisation. The evolution is
based on the 'GA' package: Luca Scrucca (2013) <doi:10.18637/jss.v053.i04>
while the Gaussian Mixture Logic stems from 'AdaptGauss': Alfred Ultsch,
Michael Thrun, Onno Hansen-Goos, Jorn Lotsch (2015)
<doi:10.3390/ijms161025897>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
