%global __brp_check_rpaths %{nil}
%global packname  IAT
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Cleaning and Visualizing Implicit Association Test (IAT) Data

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.2.0
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
Requires:         R-stats >= 3.2.0
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-lazyeval >= 0.1.10

%description
Implements the standard D-Scoring algorithm (Greenwald, Banaji, & Nosek,
2003) for Implicit Association Test (IAT) data and includes plotting
capabilities for exploring raw IAT data.

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
