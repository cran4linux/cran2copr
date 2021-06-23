%global __brp_check_rpaths %{nil}
%global packname  bunching
%global packver   0.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.4
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate Bunching

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-BB >= 2014.10.1
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-BB >= 2014.10.1
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-stats 

%description
Implementation of the bunching estimator for kinks and notches. Allows for
flexible estimation of counterfactual (e.g. controlling for round number
bunching, accounting for other bunching masses within bunching window,
fixing bunching point to be minimum, maximum or median value in its bin,
etc.). It produces publication-ready plots in the style followed since
Chetty et al. (2011) <DOI:10.1093/qje/qjr013>, with lots of functionality
to set plot options.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
