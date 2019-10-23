%global packname  phtt
%global packver   3.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.2
Release:          1%{?dist}
Summary:          Panel Data Analysis with Heterogeneous Time Trends

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-pspline 
Requires:         R-CRAN-pspline 

%description
The package provides estimation procedures for panel data with large
dimensions n, T, and general forms of unobservable heterogeneous effects.
Particularly, the estimation procedures are those of Bai (2009) and Kneip,
Sickles, and Song (2012), which complement one another very well: both
models assume the unobservable heterogeneous effects to have a factor
structure. The method of Bai (2009) assumes that the factors are
stationary, whereas the method of Kneip et al. (2012) allows the factors
to be non-stationary. Additionally, the 'phtt' package provides a wide
range of dimensionality criteria in order to estimate the number of the
unobserved factors simultaneously with the remaining model parameters.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
