%global packname  growthcurver
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Simple Metrics to Summarize Growth Curves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-grDevices >= 3.4.0
BuildRequires:    R-CRAN-minpack.lm >= 1.1
Requires:         R-stats >= 3.4.0
Requires:         R-graphics >= 3.4.0
Requires:         R-grDevices >= 3.4.0
Requires:         R-CRAN-minpack.lm >= 1.1

%description
This is a simple package that fits the logistic equation to microbial
growth curve data (e.g., repeated absorbance measurements taken from a
plate reader over time). From this fit, a variety of metrics are provided,
including the maximum growth rate, the doubling time, the carrying
capacity, the area under the logistic curve, and the time to the
inflection point.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
