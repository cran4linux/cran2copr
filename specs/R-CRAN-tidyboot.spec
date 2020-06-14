%global packname  tidyboot
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Tidyverse-Compatible Bootstrapping

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-tidyr >= 0.7.2
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rlang >= 0.1.6
BuildRequires:    R-CRAN-modelr >= 0.1.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-tidyr >= 0.7.2
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rlang >= 0.1.6
Requires:         R-CRAN-modelr >= 0.1.1

%description
Compute arbitrary non-parametric bootstrap statistics on data in tidy data
frames.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
