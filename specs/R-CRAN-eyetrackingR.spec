%global packname  eyetrackingR
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          2%{?dist}
Summary:          Eye-Tracking Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0
BuildRequires:    R-CRAN-zoo >= 1.7.12
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-broom >= 0.3.7
BuildRequires:    R-CRAN-tidyr >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
Requires:         R-CRAN-ggplot2 >= 2.0
Requires:         R-CRAN-zoo >= 1.7.12
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-broom >= 0.3.7
Requires:         R-CRAN-tidyr >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-lazyeval >= 0.1.10

%description
A set of tools that address tasks along the pipeline from raw data to
analysis and visualization for eye-tracking data. Offers several popular
types of analyses, including linear and growth curve time analyses,
onset-contingent reaction time analyses, as well as several non-parametric
bootstrapping approaches.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
