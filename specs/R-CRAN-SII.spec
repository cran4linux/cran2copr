%global __brp_check_rpaths %{nil}
%global packname  SII
%global packver   1.0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Calculate ANSI S3.5-1997 Speech Intelligibility Index

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
This package calculates ANSI S3.5-1997 Speech Intelligibility Index (SII),
a standard method for computing the intelligibility of speech from
acoustical measurements of speech, noise, and hearing thresholds. This
package includes data frames corresponding to Tables 1 - 4 in the ANSI
standard as well as a function utilizing these tables and user-provided
hearing threshold and noise level measurements to compute the SII score.
The methods implemented here extend the standard computations to allow
calculation of SII when the measured frequencies do not match those
required by the standard by applying interpolation to obtain values for
the required frequencies -- Development of this package was funded by the
Center for Bioscience Education and Technology (CBET) of the Rochester
Institute of Technology (RIT).

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
