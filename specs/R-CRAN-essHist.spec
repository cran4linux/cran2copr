%global packname  essHist
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          The Essential Histogram

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Provide an optimal histogram, in the sense of probability density
estimation and features detection, by means of multiscale variational
inference. In other words, the resulting histogram servers as an optimal
density estimator, and meanwhile recovers the features, such as increases
or modes, with both false positive and false negative controls. Moreover,
it provides a parsimonious representation in terms of the number of
blocks, which simplifies data interpretation. The only assumption for the
method is that data points are independent and identically distributed, so
it applies to fairly general situations, including continuous
distributions, discrete distributions, and mixtures of both. For details
see Li, Munk, Sieling and Walther (2016) <arXiv:1612.07216>.

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
%{rlibdir}/%{packname}/libs
