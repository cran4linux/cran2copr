%global __brp_check_rpaths %{nil}
%global packname  cointmonitoR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Consistent Monitoring of Stationarity and CointegratingRelationships

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cointReg >= 0.2.0
BuildRequires:    R-CRAN-matrixStats >= 0.14.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-cointReg >= 0.2.0
Requires:         R-CRAN-matrixStats >= 0.14.1
Requires:         R-stats 
Requires:         R-graphics 

%description
We propose a consistent monitoring procedure to detect a structural change
from a cointegrating relationship to a spurious relationship. The
procedure is based on residuals from modified least squares estimation,
using either Fully Modified, Dynamic or Integrated Modified OLS. It is
inspired by Chu et al. (1996) <DOI:10.2307/2171955> in that it is based on
parameter estimation on a pre-break "calibration" period only, rather than
being based on sequential estimation over the full sample. See the
discussion paper <DOI:10.2139/ssrn.2624657> for further information. This
package provides the monitoring procedures for both the cointegration and
the stationarity case (while the latter is just a special case of the
former one) as well as printing and plotting methods for a clear
presentation of the results.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
