%global packname  gofMC
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Goodness of Fit Noise Analysis Using Monte Carlo Techniques

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Goodness-of-fit metrics, such as R-Squared, RMSE, etc., share a
sensitivity to noise, dependent on the degrees of freedom.  Some metrics,
such as R-Squared, decrease with increasing dof and some, such as RMSE,
increase with increasing dof.  This package calculates the noise baseline
(ceiling) by random sampling, calculating the metric’s value for each
sample and counting the number of samples below a desired level, 95% by
default. If one’s measure is above (below) the calculation corresponding
to the desired level, then the measurement is distinguishable from noise.
In addition, the ratio of the measurement to the calculated level provides
a way to compare measurements of different degrees of freedom.

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
%{rlibdir}/%{packname}/INDEX
