%global packname  lqr
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Robust Linear Quantile Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ghyp 
BuildRequires:    R-CRAN-spatstat 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-ghyp 
Requires:         R-CRAN-spatstat 

%description
It fits a robust linear quantile regression model using a new family of
zero-quantile distributions for the error term as in Galarza et.al.(2017)
<doi:10.1002/sta4.140>. This family of distribution includes skewed
versions of the Normal, Student's t, Laplace, Slash and Contaminated
Normal distribution. It also performs logistic quantile regression for
bounded responses as shown in Bottai et.al.(2009) <doi:10.1002/sim.3781>.
It provides estimates and full inference. It also provides envelopes plots
for assessing the fit and confidences bands when several quantiles are
provided simultaneously.

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
