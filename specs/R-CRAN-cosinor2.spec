%global packname  cosinor2
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Extended Tools for Cosinor Analysis of Rhythms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.0.3
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-cosinor >= 1.1
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-cowplot >= 0.9.3
BuildRequires:    R-CRAN-matrixStats >= 0.52.2
BuildRequires:    R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-Hmisc >= 4.0.3
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-cosinor >= 1.1
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-cowplot >= 0.9.3
Requires:         R-CRAN-matrixStats >= 0.52.2
Requires:         R-CRAN-purrr >= 0.2.5

%description
Statistical procedures for calculating population–mean cosinor,
non–stationary cosinor, estimation of best–fitting period, tests of
population rhythm differences and more. See Cornélissen, G. (2014).
<doi:10.1186/1742-4682-11-16>.

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
