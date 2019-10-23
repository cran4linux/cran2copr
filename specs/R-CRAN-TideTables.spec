%global packname  TideTables
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Tide Analysis and Prediction of Predominantly Semi-Diurnal Tides

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-chron >= 2.3.47
BuildRequires:    R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-chron >= 2.3.47
Requires:         R-CRAN-data.table >= 1.9.6

%description
Tide analysis and prediction of predominantly semi-diurnal tides with two
high waters and two low waters during one lunar day (~24.842 hours, ~1.035
days). The analysis should preferably cover an observation period of at
least 19 years. For shorter periods, for example, the nodal cycle can not
be taken into account, which particularly affects the height calculation.
The main objective of this package is to produce tide tables.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
