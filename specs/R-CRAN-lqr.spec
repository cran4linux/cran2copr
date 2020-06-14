%global packname  lqr
%global packver   2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.11
Release:          2%{?dist}
Summary:          Robust Linear Quantile Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-numDeriv 

%description
It fits a robust linear quantile regression model using a new family of
zero-quantile distributions for the error term. This family of
distribution includes skewed versions of the Normal, Student's t, Laplace,
Slash and Contaminated Normal distribution. It also performs logistic
quantile regression for bounded responses as shown in Bottai et.al.(2009)
<doi:10.1002/sim.3781>. It provides estimates and full inference. It also
provides envelopes plots for assessing the fit and confidences bands when
several quantiles are provided simultaneously.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
