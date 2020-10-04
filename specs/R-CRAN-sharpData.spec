%global packname  sharpData
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Data Sharpening

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.1
Requires:         R-core >= 2.0.1
BuildRequires:    R-KernSmooth 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-KernSmooth 
Requires:         R-stats 
Requires:         R-CRAN-quadprog 

%description
Functions and data sets inspired by data sharpening - data perturbation to
achieve improved performance in nonparametric estimation, as described in
Choi, E., Hall, P. and Rousson, V. (2000) <doi:10.1214/aos/1015957396>.
Capabilities for enhanced local linear regression function and derivative
estimation are included, as well as an asymptotically correct iterated
data sharpening estimator for any degree of local polynomial regression
estimation. A cross-validation-based bandwidth selector is included which,
in concert with the iterated sharpener, will often provide superior
performance, according to a median integrated squared error criterion.
Sample data sets are provided to illustrate function usage.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
