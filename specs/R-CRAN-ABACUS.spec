%global __brp_check_rpaths %{nil}
%global packname  ABACUS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Apps Based Activities for Communicating and UnderstandingStatistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-shiny >= 1.3.1
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-shiny >= 1.3.1

%description
A set of Shiny apps for effective communication and understanding in
statistics. The current version includes properties of normal
distribution, properties of sampling distribution, one-sample z and t
tests, two samples independent (unpaired) t test and analysis of variance.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
