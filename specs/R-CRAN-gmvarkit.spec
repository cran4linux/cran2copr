%global packname  gmvarkit
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Estimate Gaussian Mixture Vector Autoregressive Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.4.0
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-grDevices >= 3.4.0
BuildRequires:    R-CRAN-pbapply >= 1.3.4
BuildRequires:    R-CRAN-Brobdingnag >= 1.2.5
BuildRequires:    R-CRAN-mvnfast >= 0.2.5
Requires:         R-parallel >= 3.4.0
Requires:         R-stats >= 3.4.0
Requires:         R-graphics >= 3.4.0
Requires:         R-grDevices >= 3.4.0
Requires:         R-CRAN-pbapply >= 1.3.4
Requires:         R-CRAN-Brobdingnag >= 1.2.5
Requires:         R-CRAN-mvnfast >= 0.2.5

%description
Unconstrained and constrained maximum likelihood estimation of Gaussian
Mixture Vector Autoregressive (GMVAR) model, quantile residual tests,
graphical diagnostics, simulations, and forecasting. Leena Kalliovirta,
Mika Meitz, Pentti Saikkonen (2016) <doi:10.1016/j.jeconom.2016.02.012>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
