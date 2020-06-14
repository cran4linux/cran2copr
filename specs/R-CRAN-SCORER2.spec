%global packname  SCORER2
%global packver   0.99.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.0
Release:          2%{?dist}
Summary:          SCORER 2.0: an algorithm for distinguishing parallel dimeric andtrimeric coiled-coil sequences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch

%description
This package contains the functions necessary to run the SCORER 2.0
algorithm. SCORER 2.0 can be used to differentiate between parallel
dimeric and trimeric coiled-coil sequence, which are the two most more
frequent coiled-coil structures observed naturally. As such, SCORER 2.0 is
particularly useful for researchers looking to characterize novel
coiled-coil sequences. It may also be used to assist in the structural
characterization of synthetic coiled-coil sequences. Also included in this
package are functions that allows the user to retrain the SCORER 2.0
algorithm using user-defined training data.

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
%{rlibdir}/%{packname}/INDEX
