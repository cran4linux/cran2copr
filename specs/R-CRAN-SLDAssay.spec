%global packname  SLDAssay
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          3%{?dist}
Summary:          Software for Analyzing Limiting Dilution Assays

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch

%description
Calculates maximum likelihood estimate, exact and asymptotic confidence
intervals, and exact and asymptotic goodness of fit p-values for
concentration of infectious units from serial limiting dilution assays.
This package uses the likelihood equation, exact goodness of fit p-values,
and exact confidence intervals described in Meyers et al. (1994)
<http://jcm.asm.org/content/32/3/732.full.pdf>. This software is also
implemented as a web application through the Shiny R package
<https://iupm.shinyapps.io/sldassay/>.

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
