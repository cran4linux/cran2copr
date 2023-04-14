%global __brp_check_rpaths %{nil}
%global packname  cvequality
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Tests for the Equality of Coefficients of Variation fromMultiple Groups

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Contains functions for testing for significant differences between
multiple coefficients of variation. Includes Feltz and Miller's (1996)
<DOI:10.1002/(SICI)1097-0258(19960330)15:6%3C647::AID-SIM184%3E3.0.CO;2-P>
asymptotic test and Krishnamoorthy and Lee's (2014)
<DOI:10.1007/s00180-013-0445-2> modified signed-likelihood ratio test. See
the vignette for more, including full details of citations.

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
