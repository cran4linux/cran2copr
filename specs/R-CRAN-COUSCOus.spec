%global packname  COUSCOus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Residue-Residue Contact Detecting Method

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-utils >= 3.2.2
BuildRequires:    R-CRAN-bio3d >= 2.2.2
BuildRequires:    R-CRAN-matrixcalc >= 1.0.3
Requires:         R-utils >= 3.2.2
Requires:         R-CRAN-bio3d >= 2.2.2
Requires:         R-CRAN-matrixcalc >= 1.0.3

%description
Contact prediction using shrinked covariance (COUSCOus). COUSCOus is a
residue-residue contact detecting method approaching the contact inference
using the glassofast implementation of Matyas and Sustik (2012, The
University of Texas at Austin UTCS Technical Report 2012:1-3. TR-12-29.)
that solves the L_1 regularised Gaussian maximum likelihood estimation of
the inverse of a covariance matrix. Prior to the inverse covariance matrix
estimation we utilise a covariance matrix shrinkage approach, the
empirical Bayes covariance estimator, which has been shown by Haff (1980)
<DOI:10.1214/aos/1176345010> to be the best estimator in a Bayesian
framework, especially dominating estimators of the form aS, such as the
smoothed covariance estimator applied in a related contact inference
technique PSICOV.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
