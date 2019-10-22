%global packname  nlstimedist
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Non-Linear Model Fitting of Time Distribution of BiologicalPhenomena

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-minpack.lm >= 1.2.0
BuildRequires:    R-CRAN-nlstools >= 1.0.2
BuildRequires:    R-CRAN-broom >= 0.5.0
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-lazyeval >= 0.2.0
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-minpack.lm >= 1.2.0
Requires:         R-CRAN-nlstools >= 1.0.2
Requires:         R-CRAN-broom >= 0.5.0
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-lazyeval >= 0.2.0

%description
Fit biologically meaningful distribution functions to time-sequence data
(phenology), estimate parameters to draw the cumulative distribution
function and probability density function and calculate standard
statistical moments and percentiles.

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
