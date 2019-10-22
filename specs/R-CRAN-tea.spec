%global packname  tea
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Threshold Estimation Approaches

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-eva 
Requires:         R-CRAN-eva 

%description
Different approaches for selecting the threshold in generalized Pareto
distributions. Most of them are based on minimizing the AMSE-criterion or
at least by reducing the bias of the assumed GPD-model. Others are
heuristically motivated by searching for stable sample paths, i.e. a
nearly constant region of the tail index estimator with respect to k,
which is the number of data in the tail. The third class is motivated by
graphical inspection. In addition to the very helpful eva package which
includes many goodness of fit tests for the generalized Pareto
distribution, the sequential testing procedure provided in Thompson et al.
(2009) <doi:10.1016/j.coastaleng.2009.06.003> is also implemented here.

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
