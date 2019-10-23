%global packname  sure
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Surrogate Residuals for Ordinal and General Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 

%description
An implementation of the surrogate approach to residuals and diagnostics
for ordinal and general regression models; for details, see Liu and Zhang
(2017) <doi:10.1080/01621459.2017.1292915>. These residuals can be used to
construct standard residual plots for model diagnostics (e.g.,
residual-vs-fitted value plots, residual-vs-covariate plots, Q-Q plots,
etc.). The package also provides an 'autoplot' function for producing
standard diagnostic plots using 'ggplot2' graphics. The package currently
supports cumulative link models from packages 'MASS', 'ordinal', 'rms',
and 'VGAM'. Support for binary regression models using the standard 'glm'
function is also available.

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
%{rlibdir}/%{packname}/INDEX
