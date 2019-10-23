%global packname  cotram
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Count Transformation Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mlt >= 1.0.5
BuildRequires:    R-CRAN-basefun >= 1.0.5
BuildRequires:    R-CRAN-variables >= 1.0.2
BuildRequires:    R-CRAN-tram >= 0.2.6
Requires:         R-CRAN-mlt >= 1.0.5
Requires:         R-CRAN-basefun >= 1.0.5
Requires:         R-CRAN-variables >= 1.0.2
Requires:         R-CRAN-tram >= 0.2.6

%description
Count transformation models featuring parameters interpretable as discrete
hazard ratios, odds ratios, reverse-time discrete hazard ratios, or
transformed expectations. An appropriate data transformation for a count
outcome and regression coefficients are simultaneously estimated by
maximising the exact discrete log-likelihood using the computational
framework provided in package 'mlt', technical details are given in
Hothorn et al. (2018) <DOI:10.1111/sjos.12291>.

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
%doc %{rlibdir}/%{packname}/application
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/README.txt
%doc %{rlibdir}/%{packname}/simulation
%{rlibdir}/%{packname}/INDEX
