%global packname  DistributionOptimization
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
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
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-AdaptGauss 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-pracma 

%description
Fits Gaussian Mixtures by applying evolution. As fitness function a
mixture of the chi square test for distributions and a novel measure for
approximating the common area under curves between multiple Gaussians is
used. The package presents an alternative to the commonly used Likelihood
Maximization as is used in Expectation Maximization. The algorithm and
applications of this package are published under: Lerch, F., Ultsch, A.,
Lotsch, J. (2020) <doi:10.1038/s41598-020-57432-w>. The evolution is based
on the 'GA' package: Scrucca, L. (2013) <doi:10.18637/jss.v053.i04> while
the Gaussian Mixture Logic stems from 'AdaptGauss': Ultsch, A, et al.
(2015) <doi:10.3390/ijms161025897>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
