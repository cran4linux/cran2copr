%global packname  HDcpDetect
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Detect Change Points in Means of High Dimensional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
Objective: Implement new methods for detecting change points in
high-dimensional time series data. These new methods can be applied to
non-Gaussian data, account for spatial and temporal dependence, and detect
a wide variety of change-point configurations, including changes near the
boundary and changes in close proximity. Additionally, this package helps
address the “small n, large p” problem, which occurs in many research
contexts. This problem arises when a dataset contains changes that are
visually evident but do not rise to the level of statistical significance
due to the small number of observations and large number of parameters.
The problem is overcome by treating the dimensions as a whole and scaling
the test statistics only by its standard deviation, rather than scaling
each dimension individually. Due to the computational complexity of the
functions, the package runs best on datasets with a relatively large
number of attributes but no more than a few hundred observations.

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
