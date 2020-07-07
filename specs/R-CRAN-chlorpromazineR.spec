%global packname  chlorpromazineR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Convert Antipsychotic Doses to Chlorpromazine Equivalents

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch

%description
As different antipsychotic medications have different potencies, the doses
of different medications cannot be directly compared. Various strategies
are used to convert doses into a common reference so that comparison is
meaningful. Chlorpromazine (CPZ) has historically been used as a reference
medication into which other antipsychotic doses can be converted, as
"chlorpromazine-equivalent doses". Using conversion keys generated from
widely-cited scientific papers (Gardner et. al 2010
<doi:10.1176/appi.ajp.2009.09060802>, Leucht et al. 2016
<doi:10.1093/schbul/sbv167>), antipsychotic doses are converted to CPZ (or
any specified antipsychotic) equivalents. The use of the package is
described in the included vignette. Not for clinical use.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
