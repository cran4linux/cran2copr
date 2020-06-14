%global packname  TwoRegression
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Process Data from Wearable Research Devices Using Two-RegressionAlgorithms

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils >= 3.2.4
BuildRequires:    R-stats >= 3.2.4
BuildRequires:    R-CRAN-seewave >= 2.0.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-dplyr >= 0.5.0
Requires:         R-utils >= 3.2.4
Requires:         R-stats >= 3.2.4
Requires:         R-CRAN-seewave >= 2.0.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-dplyr >= 0.5.0

%description
Application of two-regression algorithms for wearable research devices. It
provides an easy way for users to read in device data files and apply an
appropriate two-regression algorithm. More information is available from
Hibbing PR, LaMunion SR, Kaplan AS, & Crouter SE (2017)
<doi:10.1249/MSS.0000000000001532>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
